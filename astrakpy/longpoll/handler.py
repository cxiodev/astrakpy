from astrakpy.models import Message
import typing

from astrakpy.rules import AbstractRule


class Handler:
    def __init__(self, react: typing.Callable, **rules: typing.List[AbstractRule]):
        self.react = react
        self.rules = rules

    async def __call__(self, message: Message):
        await self.react(message)
