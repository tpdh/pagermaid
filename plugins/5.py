from pagermaid.listener import listener
from pagermaid.utils import alias_command, obtain_message
from requests import get
import json
@listener(is_plugin=True, outgoing=True, command=alias_command("qq"),
          description='查询qq绑定手机号及其其他信息')
async def qqapi(context):
    a = await obtain_message(context)
    try:      
        qq = json.loads(get('https://zy.xywlapi.cc/qqcx?qq='+a).text)
        if qq['status'] == 200:
            await context.edit('查询qq：`'+a+'`\nqq绑定：`'+qq['phone']+'`\nq绑地区：`'+qq['phonediqu']+
            '`\n绑定lol：`'+qq['lol']+'`\n绑定微博：`'+qq['wb']+'`\nqq老密：`'+qq['qqlm']+'`')
        if qq['status'] == 500:
            await context.edit('未找到此qq号的绑定手机号')
    except:
        await context.edit('呜呜呜出错了~，请再试一试吧')

@listener(is_plugin=True, outgoing=True, command=alias_command("qp"),
          description='查询手机绑定qq号及其其他信息')
async def qpapi(context):
    b = await obtain_message(context)
    try:
        qp = json.loads(get('https://zy.xywlapi.cc/qqphone?phone='+b).text)
        if qp['status'] == 200:
            await context.edit('查询手机号：`'+b+'`\n绑定qq：`'+qp['qq']+'`\nq绑地区：`'+qp['phonediqu']+'`')
        if qp['status'] == 500:
            await context.edit('未找到此手机号的绑定qq号')
    except:
        await context.edit('呜呜呜出错了~，请再试一试吧')
