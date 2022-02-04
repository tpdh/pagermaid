import random
from requests import get
from pagermaid.listener import listener
from pagermaid.utils import alias_command
from os import remove, replace
from pagermaid.utils import obtain_message
from urllib.parse import quote_plus
@listener(is_plugin=True, outgoing=True, command=alias_command("clash"),
description="回复一个订阅链接，转换成clash订阅")
async def clash(context):
 await context.edit("正在转换订阅")
 try:
  message = await obtain_message(context)
  encode = quote_plus(message.replace('\n', '|').replace('\r', '|'))
 except ValueError:
  await context.edit("出错了呜呜呜 ~ 无效的参数")
  return
 await context.edit("https://sub.mk74.tk/sub?target=clash&url="+ encode +"&insert=false&emoji=true")
@listener(is_plugin=True, outgoing=True, command=alias_command("base64"),
description="回复一个订阅链接，转换成base64通用订阅")
async def clash(context):
 await context.edit("正在转换订阅")
 try:
  message = await obtain_message(context)
  encode = quote_plus(message.replace('\n', '|').replace('\r', '|'))
 except ValueError:
  await context.edit("出错了呜呜呜 ~ 无效的参数")
  return
 await context.edit("https://sub.mk74.tk/sub?target=mixed&url="+ encode +"&insert=false&emoji=true")


