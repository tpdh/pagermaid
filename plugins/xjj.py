import random
from requests import get
from pagermaid.listener import listener
from pagermaid.utils import alias_command
from os import remove
import os
os.environ["http_proxy"] = "http://192.168.2.207:7890"
os.environ["https_proxy"] = "http://192.168.2.207:7890"

@listener(is_plugin=True, outgoing=True, command=alias_command("xjj"),
          description="随机小姐姐写真")
async def ghs(context):
    await context.edit("拍小姐姐写真中 . . .")
    status = False
    for _ in range(10):  # 最多重试10次
        website = random.randint(0, 0)
        filename = "xjj" + str(random.random())[2:] + ".png"
        try:
            if website == 0:
                img = get("https://acg.toubiec.cn/random.php")
            if img.status_code == 200:
                with open(filename, 'wb') as f:
                    f.write(img.content)
                await context.edit("写真我拍好辣，上传中 . . .")
                await context.client.send_file(context.chat_id, filename, caption="小姐姐来辣~⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄)")
                status = True
                break  # 成功了就赶紧结束啦！
        except:
            try:
                remove(filename)
            except:
                pass
            continue
    try:
        remove(filename)
    except:
        pass
    try:
        await context.delete()
    except:
        pass
    if not status:
        await context.client.send_message(context.chat_id, "出错了呜呜呜 ~ 试了好多好多次都无法访问到服务器（没有颜色搞啦！） 。")
