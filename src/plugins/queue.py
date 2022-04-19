import re

from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message

from src.libraries.queue.service import get_all, get_one, add_player, del_player
from src.libraries.queue.msg_builder import build_msg

all_stats = on_command('all_stats ', aliases={'机厅几卡'})

@all_stats.handle()
async def _(bot: Bot, event: Event, state: T_State):
    result = get_all(group_uim=event.get_session_id())
    msg = []
    if not result['error']:
        for data in result['list']:
            msg.append(build_msg(data))
        msg.append({
            "type": "text",
            "data": {
                "text": f"*若要增减排队人数，请使用“<机厅别名>[+/-]<人数>”。\n如：nzc+2"
            }
        })
    else:
        msg.append({
            "type": "text",
            "data": {
                "text": f""
            }
        })
    await all_stats.send(Message(msg))

one_stat = on_regex(r"^(.+)几卡$")

@one_stat.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "^(.+)几卡$"
    res = re.match(regex, str(event.get_message()).lower()).groups()
    command = res[0]
    result = get_one(command, group_uim=event.get_session_id())
    msg = []
    if not result['error']:
        msg.append(build_msg(result['info']))
        msg.append({
            "type": "text",
            "data": {
                "text": f"*若要增减排队人数，请使用“<机厅别名>[+/-]<人数>”。\n如：nzc+2"
            }
        })
    else:
        msg.append({
            "type": "text",
            "data": {
                "text": f""
            }
        })
    await one_stat.send(Message(msg))

player_cal = on_regex(r"^(.+)(\+|\-)(\d+)$")

@player_cal.handle()
async def _(bot: Bot, event: Event, state: T_State):
    regex = "^(.+)(\+|\-)(\d+)$"
    res = re.match(regex, str(event.get_message()).lower()).groups()
    command = res[0]
    number = res[2]
    if res[1] == '+':
        result = add_player(command, number, group_uim=event.get_session_id())
    elif res[1] == '-':
        result = del_player(command, number, group_uim=event.get_session_id())
    else:
        result = get_one(command, group_uim=event.get_session_id())
    msg = []
    if not result['error']:
        msg.append(build_msg(result['info']))
        msg.append({
            "type": "text",
            "data": {
                "text": f"*若要增减排队人数，请使用“<机厅别名>[+/-]<人数>”。\n如：nzc+2"
            }
        })
    else:
        msg.append({
            "type": "text",
            "data": {
                "text": f""
            }
        })
    await player_cal.send(Message(msg))
