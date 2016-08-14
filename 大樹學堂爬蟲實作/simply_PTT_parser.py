import requests
from pyquery import PyQuery as pq
re=requests.get('https://www.ptt.cc/bbs/joke/M.1425175878.A.BF4.html')
re=re.text.replace(':','')
d=pq(re)
for i in d('.push-content'):
    with open ('test.json','a',encoding='UTF-8') as f:
        f.write(d(i).text()+'\n')