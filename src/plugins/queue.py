from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message

def build_queue(name, number, date):
    item = '''[{name}]
当前人数：{number}人
更新时间：{date}
'''
    return {
        "type": "text",
        "data": {
            "text": f"{item}"
        }
    }

queue_stats = on_command('queue_stats ', aliases={'mai几卡'})

@queue_stats.handle()
async def _(bot: Bot, event: Event, state: T_State):
    await queue_stats.send(Message([
        build_queue('疯狂牛仔城', 3, '2022-02-07 19:00:00'),
        build_queue('天空之城', 8, '2022-02-07 17:53:27'),
        {
            "type": "text",
            "data": {
                "text": f"*上述信息为开发测试数据，和实际排队人数无关。"
            }
        },
    ]))
