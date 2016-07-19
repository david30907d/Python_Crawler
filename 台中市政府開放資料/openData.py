import requests, json, pyprind
from bs4 import BeautifulSoup
res = requests.get("http://data.taichung.gov.tw/wSite/lp?ctNode=230&mp=1&idPath=&nowPage=1&pagesize=300")
soup = BeautifulSoup(res.text)
urlBase =  "http://data.taichung.gov.tw/wSite/"
json_arr = []

def parsePage(link):
    res = requests.get(link)
    soup = BeautifulSoup(res.text)
    tmpJson = {'title':soup.select('h3')[0].text}
    for tr in soup.select('tr'):
        d = {tr.find('th').text : tr.find('td').text}
        tmpJson.update(d)
        # print(tmpJson)

    global json_arr
    json_arr.append(tmpJson)

def dump(fileName):
    with open(fileName, 'w', encoding='UTF-8') as f:
        json.dump(json_arr, f)

def getList(soup):
    for li in soup.select('.list li'):
        dataNum = li.select('.number')[0].text
        link = urlBase + li.find('a').get('href')
        # print(dataNum, link)
        parsePage(link)
        ProgreBar.update(1,item_id = dataNum, force_flush=True)#



if __name__  ==  "__main__":
    totNum = int(soup.select('em')[0].text)
    location = "台中"
    ProgreBar = pyprind.ProgBar(totNum, title = "{} 共 {} 筆開放資料要處理" .format( location, totNum)) #建立一個進度條物件
    getList(soup)#爬第1頁的資料
    dump('openDate.json') 
    global json_arr
    json_arr = []
    while True:
        # 如果還有其他頁就繼續爬
        if soup.select('a.next') != []:
            res = requests.get(urlBase + soup.find('a','next')['href']) # get url of next page
            soup = BeautifulSoup(res.text)
            getList(soup)
        else:
            break
    dump('openDate2.json') 

               