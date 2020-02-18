"""Re-created rapid version of aioastrak."""
from astrakpy.longpoll.handler import Handler
from astrakpy import rules
from astrakpy.exceptions import AstrakServerSideError
from astrakpy.models.message import Message
from astrakpy.logging import Logging

import typing


class LongPoll:
    def __init__(self, app):
        self.app = app
        self.loop = app.loop
        self.message_handlers: typing.List[Handler] = []

    async def _handle_new_message(self, event):
        for handler in self.message_handlers:
            for rule in handler.rules:
                if rule in rules.standart_rules:
                    if await rules.standart_rules[rule]().check(
                        message=Message(
                            self,
                            text=event["event"]["text"],
                            message_id=event["event"]["message_id"],
                            from_id=event["event"]["from_id"],
                            to_id=event["event"]["to_id"],
                            created_at=event["event"]["created_at"],
                        ),
                        text=handler.rules[rule],
                    ):
                        return True, handler
            return False, None

    async def _handle_event(self, event):
        executed, handler = await self._handle_new_message(event)
        if executed:
            message = Message(app=self.app, **event["event"])
            return await handler(message)

    def on_message(self, **_rules):
        def decorator(func: typing.Callable) -> typing.Callable:
            handler = Handler(func, **_rules)
            self.message_handlers.append(handler)
            return func

        return decorator

    async def listen(self):
        while True:
            try:
                event = await self.app.api_method("events/polling")
            except AstrakServerSideError:
                Logging.warning("Polling timeout, refreshing...")
                continue
            Logging.info("New event - " + str(event))
            yield event

    async def run_polling(self):
        Logging.info("Running longpoll system...")
        async for event in self.listen():
            self.loop.create_task(self._handle_event(event))
