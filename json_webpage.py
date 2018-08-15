import json
import requests
import codecs

res = requests.get('http://disclosure.szse.cn//disclosure/fulltext/plate/szlatest_24h.js')
res.encoding = 'gbk' # 得到的结果转换为 gbk 编码
print(res.text)
all_news = json.loads(res.text[17:-2]) # 从第一个'['取到最后一个']'，可以先将res.text打印出来，查看里面的元素情况，以此来确定取的位置

print(all_news)
with codecs.open ( "new.txt" , 'w' , 'utf-8' ) as f:
    for each_news in all_news:
        url = each_news[1] # 获取公告的URL
        title = each_news[2] # 获取公告的标题
        time = each_news[-1] # 获取公告发布的时间
        content=url+' '+title+' '+time+'\n'
        f.write(content)
        print(content)

