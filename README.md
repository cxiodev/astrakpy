<h1 align="center">Welcome to astrakpy 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: GNU GPL V3 " src="https://img.shields.io/badge/License-GNU GPL V3 -yellow.svg" />
  </a>
</p>

> Powerful asynchronous Astrak Me library.

## Installing

+ Install Python 3.6 or higher
+ Open terminal and write:
```shell script
python -m pip install https://github.com/triedgriefdev/astrakpy/archive/master.zip
```

## Updating

While installing just add `-U` flag.

## Usage
+ Simple API Usage
```python
from astrakpy import AstrakPy

# app = AstrakPy(token="token")
app = AstrakPy("username", "password")


async def logic():
    print(await app.api_method("users/check"))


if __name__ == '__main__':
    tm = app.get_task_manager()
    tm.add_task("Logic", logic())
    tm.run()

```
+ Simple longpoll bot
```python
from astrakpy import AstrakPy
from astrakpy.models.message import Message

# app = AstrakPy(token="token")
app = AstrakPy("username", "password")
lp = app.get_longpoll()


@lp.on_message(text="hi")
async def handle_echo(msg: Message):
    await msg.answer(f"Hi id{msg.from_id}, I`m id{msg.to_id}.\n"
                     f"Your message was deliviried at {msg.created_at}.")

if __name__ == '__main__':
    tm = app.get_task_manager()
    tm.add_task("LongPoll", lp.run_polling())
    tm.run()

```

## Author

👤 **triedgriefdev**

* Website: https://triedgrief.codes
* Github: [@triedgriefdev](https://github.com/triedgriefdev)

## Show your support

Give a ⭐ if this project helped you!