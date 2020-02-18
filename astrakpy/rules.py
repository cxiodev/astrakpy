from abc import ABC, abstractmethod
from astrakpy.models.message import Message
import typing


class AbstractRule(ABC):
    title = None

    @abstractmethod
    async def check(self, message: Message, check_param: typing.Any) -> bool:
        pass


class TextRule(AbstractRule):
    title = "text"

    async def check(self, message: Message, text: typing.AnyStr) -> bool:
        return message.text.lower() == text


class TextContainsRule(AbstractRule):
    title = "text_contains"

    async def check(self, message: Message, text: typing.AnyStr) -> bool:
        return text in [word.lower() for word in message.text]


class TextStarswithRule(AbstractRule):
    title = "startswith"

    async def check(self, message: Message, text: typing.AnyStr) -> bool:
        return message.text.startswith(text)


standart_rules = {
    TextRule.title: TextRule,
    TextContainsRule.title: TextContainsRule,
    TextStarswithRule.title: TextStarswithRule,
}
