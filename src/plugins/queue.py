import re

from nonebot import on_command, on_regex
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message

from src.libraries.queue.service import get_all, get_one, set_player
from src.libraries.queue.msg_builder import build_msg
from src.libraries.dbutil import has_group, get_group_uim

all_stats = on_command('all_stats ', aliases={'机厅几卡'})

@all_stats.handle()
async def _(bot: Bot, event: Event, state: T_State):
    group_uim = get_group_uim(event)
    if has_group(group_uim, 'queue'):
        result = get_all(group_uim)
        msg = []
        if not result['error']:
            for data in result['list']:
                msg.append(build_msg(data))
            msg.append({
                "type": "text",
                "data": {
                    "text": "*若要调整排队人数，请使用“<机厅别名>=<人数>”。\n如：nzmai=2"
                }
            })
        else:
            msg.append({
                "type": "text",
                "data": {
                    "text": result['msg']
                }
            })
        await all_stats.send(Message(msg))

one_stat = on_regex(r"^(.+)几卡$")

@one_stat.handle()
async def _(bot: Bot, event: Event, state: T_State):
    group_uim = get_group_uim(event)
    if has_group(group_uim, 'queue'):
        regex = "^(.+)几卡$"
        res = re.match(regex, str(event.get_message()).lower()).groups()
        command = res[0]
        result = get_one(command, group_uim)
        msg = []
        if not result['error']:
            msg.append(build_msg(result['info']))
            msg.append({
                "type": "text",
                "data": {
                    "text": "*若要调整排队人数，请使用“<机厅别名>=<人数>”。\n如：nzmai=2"
                }
            })
        else:
            msg.append({
                "type": "text",
                "data": {
                    "text": result['msg']
                }
            })
        await one_stat.send(Message(msg))

player_cal = on_regex(r"^(.+)=(\d+)$")

@player_cal.handle()
async def _(bot: Bot, event: Event, state: T_State):
    group_uim = get_group_uim(event)
    if has_group(group_uim, 'queue'):
        regex = "^(.+)=(\d+)$"
        res = re.match(regex, str(event.get_message()).lower()).groups()
        command = res[0]
        number = res[1]
        result = set_player(command, number, group_uim)
        msg = []
        if not result['error']:
            msg.append(build_msg(result['info']))
            msg.append({
                "type": "text",
                "data": {
                    "text": "*若要调整排队人数，请使用“<机厅别名>=<人数>”。\n如：nzmai=2"
                }
            })
        else:
            msg.append({
                "type": "text",
                "data": {
                    "text": result['msg']
                }
            })
        await player_cal.send(Message(msg))
