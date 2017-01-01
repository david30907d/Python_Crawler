#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
import shutil, subprocess, os

path = input("Please input the path you want to store these image:")
try:
    subprocess.call(['mkdir', '-p', path])
    os.chdir(path)
except:
    print('path error')
targetURL = input("Please input the url that you want to Parse:")
res =requests.get(targetURL)
res.encoding =  res.apparent_encoding
soup = BeautifulSoup(res.text)
for index, i in enumerate(soup.select('img')):
    try:
        fname = str(index)+".jpg"
        imageUrl = i['src']
        ires = requests.get(imageUrl,stream=True)
        f = open(fname,'wb')
        shutil.copyfileobj(ires.raw,f)
        f.close()
        del ires
    except Exception as e:
        print(i)

headline = soup.select('h1.head')[0]
headline = headline.text.replace('\'','')
headline = headline.replace('$','')
headline = headline.replace('\n','')
headline = headline.replace(' ','')
headline = headline.replace('/','')
headline = headline.replace('\u3000','')
os.chdir('../')
print(os.getcwd())
subprocess.call(['mv', path, headline])
