#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json, pyprind, sys, shutil, re
from bs4 import BeautifulSoup
base_url = "http://www.gomaji.com/"
json_arr = {} # 最終結果json

def parsePage(url, location, resType):
    res = requests.get(url)
    childSoup = BeautifulSoup(res.text)

    for i, img in zip(childSoup.select('ul.deal16 li.box-shadow2px'), childSoup.select('ul.deal16 li.box-shadow2px img')):
        href = i.find('a')['href']# 把a的href屬性的值抓出來
        href = base_url+href
        d = getResProf(href) # getResPro這個函式會進入到某一間餐廳的簡介，簡介寫的資料比較完整，但是格式並沒有固定，出錯機率極高

        restaurant = i.find('a').find('div','boxc').find('h2')# find可以找到他的child那一層
        restaurant = purgeResName(restaurant.text.strip(), d)
        savePict(img, restaurant)
        d["url"] = href
        d['restaurant'] = restaurant

def savePict(img, restaurant):
    imageUrl = img['src']
    img = requests.get(imageUrl,stream=True)
    with open(restaurant+'.jpg', 'wb') as f:
        shutil.copyfileobj(img.raw, f)

if __name__  ==  "__main__":
    parsePage("http://www.gomaji.com/index.php?city=Taichung&tag_id=12")
