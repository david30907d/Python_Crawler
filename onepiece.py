#!/usr/bin/python3
# -*- coding: utf8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import shutil, requests

def savePict(url, name):
    img = requests.get(url,stream=True)
    with open(name, 'wb') as f:
        shutil.copyfileobj(img.raw, f)
url = "http://v.comicbus.com/online/comic-653.html?ch=620"

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url)

with open('source.html','w') as f:
	soup = BeautifulSoup(driver.page_source)
	savePict(soup.select('#TheImg')[0]['src'], 'test.jpg')
	f.write(driver.page_source)
driver.close()
