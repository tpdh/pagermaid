from os import close, remove
import requests, sys, chardet, urllib.request
from lxml import etree
from pagermaid.listener import listener
from pagermaid.utils import alias_command
from pagermaid.utils import obtain_message
@listener(is_plugin=True, outgoing=True, command=alias_command("bai"),
description="回复一个关键词或自己输入，使用百度引擎搜索\n(只有你想不到的，就没有我能搜得到的🤪)",parameters='<keyword>')
async def baidu(context):
    header={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.baidu.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57'
}
    await context.message.edit('侦测到有情况！正在尝试搜索。。。')
    try:
        keyword = await obtain_message(context)
    except:
            await context.message.edit('搜索东西不带参数?李在赣神魔??')
    try:
        for _ in range(3):
            res = requests.get('https://www.baidu.com/s?wd='+keyword+'&pn=10', headers=header)
            if res.status_code == 200:
                break
    except:
        await context.message.edit('卧豁，完蛋了的嘛，试了好几次都没有访问到百度搜索引擎😱😱😱')
        sys.exit(0)
    try:
        res_xpath = etree.HTML(res.text)
    except:
        await context.message.edit('没有安装lxml库就想用？？？')
    with open ('b.txt','w+',encoding='utf-8')as f:
        for i in range(11,21):
            try:
                url = res_xpath.xpath('//div[@id='+str(i)+']//h3/a/@href')[0]
                title = ''.join(res_xpath.xpath('//div[@id='+str(i)+']//h3//text()'))
            except:
                    continue
            urlc = '('+url+')';titlec = '['+title+']'
            f.write(titlec);f.write(urlc+'\n\n')
    file = open("b.txt", 'r', encoding='utf-8')
    await context.edit('**🛸百度一下🔍，你就知道🚀**\n\n搜索对象🔎：`'+keyword+'`\n\n'+file.read())
    file.close()
    remove("b.txt")
                