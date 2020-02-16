import typing


class BaseMessageHandler:
    def __init__(
        self, react_on_message: str, react_on_type: str, on_event_void: typing.Coroutine
    ):
        self.react_on_type = react_on_type
        self.react_on_message = react_on_message
        self.on_event_void = on_event_void


class AnyMessageHandler:
    def __init__(self, on_event_void: typing.Coroutine):
        self.on_event_void = on_event_void
        self.react_on_type = "new_message"
