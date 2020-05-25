"""AstrakPy core. Everything is based on this module."""
from astrakpy.api import API
from astrakpy.exceptions import AstrakError, AstrakServerSideError
from astrakpy.logging import Logging
from astrakpy.longpoll.longpoll import LongPoll
from aiohttp import ClientSession, ClientError
import asyncio
import ujson

from astrakpy.task_manager import TaskManager


class AstrakPy:
    def __init__(self, login: str = None, password: str = None, token: str = None):
        self.url = "https://astrak.me/api/"
        self.loop = asyncio.get_event_loop()
        self.login = login
        self.password = password
        self.token = token

    async def api_method(
        self, method: str, params: dict = None, fill_token: bool = True
    ) -> dict:
        if params is None:
            params = {}

        if fill_token:
            if self.token is None:
                Logging.warning("You wasn`t logged in! Logging...")
                await self.auth()
                Logging.info("Logged in.")
            params.update({"token": self.token})

        async with ClientSession(json_serialize=ujson.dumps) as client:
            async with client.post(self.url + method, data=params) as rq:
                try:
                    resp = await rq.json()
                    try:
                        if resp["code"] < 0:
                            raise AstrakError(f"[{resp['code']}] {resp['response']}")
                    except KeyError:
                        return resp
                except ClientError:
                    raise AstrakServerSideError(
                        "Something was wrong... Seems like server-side error."
                    )
        return resp

    async def auth(self):
        if self.login is None:
            raise AstrakError("Login was None.")
        if self.password is None:
            raise AstrakError("Password was None.")

        self.token = (
            await self.api_method(
                "users/login",
                {"username": self.login, "password": self.password},
                fill_token=False,
            )
        )["token"]

    def get_api(self):
        api = API(self)
        API.set_current(api)
        return api

    def get_longpoll(self):
        return LongPoll(self)

    def get_task_manager(self):
        return TaskManager(self)
