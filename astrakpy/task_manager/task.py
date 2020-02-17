import typing


class Task:
    def __init__(self, name: str, react: typing.Coroutine):
        self.name = name
        self.react = react

    def run(self, loop):
        loop.create_task(self.react)
