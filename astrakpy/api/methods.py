from astrakpy.astrak import AstrakPy
from astrakpy.api.models import UserAuthModel, TokenValidatorModel


class Users:
    def __init__(self, app: AstrakPy):
        self.app: AstrakPy = app
        self.method = "users/"

    async def register(self, username, password) -> UserAuthModel:
        return UserAuthModel(
            **(
                await self.app.api_method(
                    self.method + "register",
                    params={
                        "username": username,
                        "password": password
                    },
                    fill_token=False
                )
            )
        )

    async def login(self, username, password) -> UserAuthModel:
        return UserAuthModel(
            **(
                await self.app.api_method(
                    self.method + "login",
                    params={
                        "username": username,
                        "password": password
                    },
                    fill_token=False
                )
            )
        )

    async def check(self, token: str = None):
        if token is None:
            token = self.app.token

        return TokenValidatorModel(
            **(
                await self.app.api_method(
                    self.method + "check",
                    params={
                        "token": token
                    },
                    fill_token=False  # DO NOT REMOVE
                )
            )
        )


class Messages:  # TODO: Complete...
    def __init__(self, app: AstrakPy):
        self.app: AstrakPy = app
        self.method = "messages/"

    async def send(self, text, to):
        pass
