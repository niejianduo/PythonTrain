from urllib import request,response,parse
from requests import Request
import json
import time
import random
import hashlib
import operator

while True:
    content = input('请输入需要翻译的内容(退出q/Q):')
    if(content != 'Q' and content != 'q') :
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        head = {}
        head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36]'

        data = {}
        S = 'fanyideskweb'
        n = content
        r = str(int(time.time() * 1000) + random.randint(1, 10))
        D = 'ebSeFb%=XZ%T[KZ)c(sy!'

        sign = hashlib.md5((S + n + r + D).encode('utf-8')).hexdigest()

        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = r
        data['sign'] = sign
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_CLICKBUTTION'
        data['typoResult'] = 'false'

        data = parse.urlencode(data).encode('utf-8')
        request1 = request.Request(url=url, data=data, method='POST')
        response1 = request.urlopen(request1)
        html=response1.read().decode('utf-8')
        target = json.loads(html)
        result = target['translateResult'][0][0]['tgt']
        print ('翻译的结果是:',result)
    else:
        print('退出翻译器')
        break