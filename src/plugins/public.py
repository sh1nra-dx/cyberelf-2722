import random
import re

from PIL import Image
from nonebot import on_command, on_message, on_notice, require, get_driver, on_regex
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Message, Event, Bot
from src.libraries.maimaidx.image import *
from random import randint


help = on_command('help')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''CybeRELF#2722 implements mai-bot

可用命令如下：
> XXXmaimaiXXX什么： 随机一首歌
> 随个[dx/标准][绿黄红紫白]<难度>： 随机一首指定条件的乐曲
> 查歌<乐曲标题的一部分>： 查询符合条件的乐曲
> [绿黄红紫白]id<歌曲编号>： 查询乐曲信息或谱面信息
> 定数查歌 <定数>：查询定数对应的乐曲
> 定数查歌 <定数下限> <定数上限>
> 分数线 <难度+歌曲id> <分数线>：详情请输入“分数线 帮助”查看
> b40/b50：从账户中获取40或50条最佳歌曲记录并制作成图表
查询前请先前往 https://www.diving-fish.com/maimaidx/prober 注册查分器，并按照操作指南导入数据'''
    await help.send(Message([{
        "type": "text",
        "data": {
            "text": f"{help_str}"
        }
    }]))


async def _group_poke(bot: Bot, event: Event, state: dict) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


poke = on_notice(rule=_group_poke, priority=10, block=True)


@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if event.__getattribute__('group_id') is None:
        event.__delattr__('group_id')
    await poke.send(Message([{
        "type": "poke",
        "data": {
            "qq": f"{event.sender_id}"
        }
    }]))

