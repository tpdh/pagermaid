from pagermaid.utils import obtain_message , alias_command
from pagermaid.listener import listener
@listener(is_plugin=True, outgoing=True, command=alias_command("uid"),
description="永久标记用户，防止改用户名",parameters='<keyword>')
async def uid(context):
    try:
        await context.edit('#标记 tg://openmessage?user_id='+await obtain_message(context))
    except:
        await context.edit('出错了')