#把PTT八卦版的標題爬回來，可以通過18進的門檻
import requests
from bs4 import BeautifulSoup
payload={"from":"/bbs/Gossiping/index.html","yes":"yes"}
s=requests.session()
res = s.post('https://www.ptt.cc/ask/over18',data=payload)
res = s.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text)
#print(res.text)
for i in soup.select('.r-ent'):
	print(i.select('.title')[0].text,i.select('.author')[0].text)