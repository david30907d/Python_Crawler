#!/usr/bin/python3
import requests, json
from bs4 import BeautifulSoup
import shutil
import os

path = input("Please input the path you want to store these image:")
try:
    os.chdir(path)
    #means cd path
except:
    print('path error')
targetURL = input("Please input the url that you want to Parse:")
res =requests.get(targetURL)
soup = BeautifulSoup(res.text)
for i in soup.select('img'):
    try:
        fname = i['src'].split('/')[-1]
        fname = fname+".jpg"
        imageUrl = i['src']
        ires = requests.get(imageUrl,stream=True)
        f = open(fname,'wb')
        shutil.copyfileobj(ires.raw,f)
        f.close()
        del ires
    except Exception as e:
        print(i)
        print(e)