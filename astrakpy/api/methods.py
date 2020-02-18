import typing
from astrakpy.api.models import (
    UserAuthModel,
    TokenValidatorModel,
    MessageModel,
    DialogModel,
    DialogMessageModel,
)


class Users:
    def __init__(self, app):
        self.app = app
        self.method = "users/"

    async def register(self, username, password) -> UserAuthModel:
        return UserAuthModel(
            **(
                await self.app.api_method(
                    self.method + "register",
                    params={"username": username, "password": password},
                    fill_token=False,
                )
            )
        )

    async def login(self, username, password) -> UserAuthModel:
        return UserAuthModel(
            **(
                await self.app.api_method(
                    self.method + "login",
                    params={"username": username, "password": password},
                    fill_token=False,
                )
            )
        )

    async def check(self, token: str = None):
        if token is None:
            token = self.app.token

        return TokenValidatorModel(
            **(
                await self.app.api_method(
                    self.method + "check", params={"token": token}
                )
            )
        )


class Messages:
    def __init__(self, app):
        self.app = app
        self.method = "messages/"

    async def send(self, text, to) -> MessageModel:
        return MessageModel(
            **(
                await self.app.api_method(
                    self.method + "send", params={"text": text, "to": to}
                )
            )
        )

    async def dialogs(self) -> typing.List[DialogModel]:
        dialogs: typing.List[DialogModel] = []
        for dialog in await self.app.api_method(self.method + "dialogs"):
            dialogs.append(DialogModel(**dialog))
        return dialogs

    async def dialog(self, id: int) -> typing.List[DialogMessageModel]:
        messages: typing.List[DialogMessageModel] = []
        for message in await self.app.api_method(
            self.method + "dialog", params={"id": id}
        ):
            messages.append(DialogMessageModel(**message))
        return messages
