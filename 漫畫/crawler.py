#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json, pyprind, sys, shutil, re
from bs4 import BeautifulSoup
base_url = "http://www.gomaji.com/"
json_arr = {} # 最終結果json
header = {"User-Agent":"User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36"}

def dump(fileName):
    with open(fileName, 'w', encoding='UTF-8') as f:
        json.dump(json_arr, f)

def savePict(img, name):
    imageUrl = img['src']
    img = requests.get(imageUrl,stream=True)
    with open(name+'.jpg', 'wb') as f:
        shutil.copyfileobj(img.raw, f)

def parseComic(name, url):
    for i in range(1, 20):
        re = requests.get(url+str(i), headers=header)
        soup = BeautifulSoup(re.text)
        img = soup.select('#curPic')[0]
        print(img)
        # savePict(img, i)


if __name__  ==  "__main__":
    parseComic("onellpiece", "http://comic.sfacg.com/HTML/OnePiece/832/#p=")