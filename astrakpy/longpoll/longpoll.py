from astrakpy.longpoll.models import BaseMessageHandler, AnyMessageHandler
from astrakpy.exceptions import AstrakServerSideError
from astrakpy.models.message import Message

import typing


class LongPoll:
    def __init__(self, app):
        self.app = app
        self.loop = app.loop
        self.handlers = []
        self.types = {
            "new_message": self.handle_new_message
        }

    def register_message_event(self, message: str, react: typing.Coroutine):
        self.handlers.append(BaseMessageHandler(message, "new_message", react))

    def register_any_message_event(self, react: typing.Coroutine):
        self.handlers.append(AnyMessageHandler(react))

    async def _run_polling(self):
        while True:
            try:
                resp = await self.app.api_method("events/polling")
            except AstrakServerSideError:
                continue
            for handler in self.handlers:
                if isinstance(handler, AnyMessageHandler):  # noqa
                    await self.handle_any_message(resp, handler)
                elif handler.react_on_type == resp["type"]:
                    await self.types[resp["type"]](resp, handler)

    async def handle_new_message(self, resp, handler):
        if handler.react_on_message == resp["event"]["text"]:
            await self.handle_any_message(resp, handler)

    async def handle_any_message(self, resp, handler):
        self.loop.create_task(
            handler.on_event_void(
                Message(
                    self.app,
                    text=resp["event"]["text"],
                    created_at=resp["event"]["created_at"],
                    from_id=resp["event"]["from_id"],
                    message_id=resp["event"]["message_id"],
                )
            )
        )

    def run_polling(self):
        self.loop.create_task(self._run_polling())
