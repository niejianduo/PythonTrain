from urllib import request,parse
import chardet
import  json

if __name__=='__main__':

    url = 'http://fanyi.baidu.com/translate?zh#en/zh/'
    wd=input("Your input:")
    qs={
        'wd':wd
    }
    qs=parse.urlencode(qs)
    fullurl=url+qs
    rsp = request.urlopen(url,timeout=20)
    html = rsp.read()

    cs=chardet.detect(html)

    #使用get来获取网页的编码方式，保证解码不会出错，如果获取不到就设为utf-8
    html=html.decode(cs.get("encoding",'utf-8'))

    print(html)