from urllib import request,parse
import chardet

if __name__=='__main__':

    url = 'https://www.cnblogs.com/zywscq/p/5441145.html'
    rsp = request.urlopen(url,timeout=20)
    print(type(rsp))

    print("URL:{0}".format(rsp.geturl()))
    print("Info:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))
    html = rsp.read()

    cs=chardet.detect(html)
    print(type(cs))
    print(cs)
    #使用get来获取网页的编码方式，保证解码不会出错，如果获取不到就设为utf-8
    html=html.decode(cs.get("encoding",'utf-8'))

    print(html)