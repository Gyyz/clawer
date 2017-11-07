#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from bs4 import BeautifulSoup
from selenium import webdriver
import pickle

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
url_str = 'http://ddosattacks.net/category/ddos-attacks/page/ /'

with open('titlelist.txt', 'w') as filout:
    for idx in range(108):
    	url_site = urlstring.replace(' ', str(idx))
    	print'###\tBegin Clawing the website %s'%url_site
    	driver.get(url_site)
    	page = driver.page_source.encode('utf-8')
    	bsObj = BeautifulSoup(page, 'lxml')
    	titles = bsObj.find_all('h2')
     	for tit in titles:
        	print tit.text
        	filout.write(tit.text.encode('utf-8')+'\n')

#find the trigger event
trigger_event=soup.find('div', { "class" : "tit-s1" })
news=trigger_event.find_all('a')[0]['href'].strip()
description=trigger_event.find_all('p')[0]['title'].strip()
try:
    driver.get(news)
    news_content= driver.page_source.encode('utf-8')
    with open("jinrongjienews/"+concept["name"]+".txt", 'w') as page:
        page.write(str(news_content))
except:
    print("Cannot get trigger news for: "+concept['name'])
    print("URL: "+news)
f1.write(concept['name']+"||"+news+"||"+description+"\n")

#find related stocks
related_stocks=soup.find(id="stockTbody").find_all("tr")
for stock in related_stocks:
    cols=stock.find_all("td")
    stock_code=cols[1].find('a').contents[0].strip()
    stock_name=cols[2].find('a').contents[0].strip()
    stock_reason=cols[5].find('span').contents
    f2.write(concept['name']+"||"+stock_code+"||"+stock_name+"||"+str(stock_reason)+"\n")
driver.quit()