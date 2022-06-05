from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message

send_location = on_command('位置测试')

@send_location.handle()
async def _(bot: Bot, event: Event, state: T_State):
    msg = [
        {
            "type": "location",
            "data": {
                "lat": "23.70996",
                "lon": "113.037856",
            },
        },
    ]
    await send_location.send(Message(msg))
