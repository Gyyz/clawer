PYTHONIOENCODING='utf-8'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib, sys, os
import re
import time
import codecs
import json
import traceback
import datetime
import pickle as pk
chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get('https://www.globaldelight.com/halloween/?source=boommac')
driver.refresh()
page = driver.page_source.encode('utf-8')
bsObj = BeautifulSoup(page, 'html')
bsObj.findAll('a', {'class': 'buy btn btn-default btn-lg btn-dl buybtn WindowsClass'})[0]['data-coupon']