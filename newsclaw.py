PYTHONIOENCODING='utf-8'
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import urllib2, sys, os
import re
import time
import codecs
import json
import traceback
import datetime
import pickle as pk

#=============================================
def get_contents(keyset):

	print('START NEWS CLAWING')
	hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',}
	assert isinstance(keyset, dict), 'Dict Content Error'
	for key in keyset.keys():
		if ('/' in key) or key == '.com':
			continue
		tmpc = keyset[key]
		if  not os.path.exists(key):
			os.mkdir(key)
		for i,item in enumerate(tmpc):
			assert len(item) == 2, 'Error in Element Length'
			urlsite = item[1]
			with open('%s/%d.txt'%(key,i), 'w') as filout:
				try:
					print('Clawing Site: %s'%urlsite)		  
					req = urllib2.Request(urlsite, headers=hdr)
					page = urllib2.urlopen(req)
					bsObj = BeautifulSoup(page, "lxml")
					filout.write('###TITLE###: %s\n'%item[0].encode('utf-8'))
					filout.write('###URL###: %s\n'%urlsite.encode('utf-8'))
					filout.write('###NEWS###: %s\n')
					for inner_block in bsObj.findAll(['p','li']):
						news = inner_block.text
						filout.write(news.encode('utf-8')+'\n')
				except Exception, e:
					traceback.print_exc()
	print('END NEWS CLAWING')
	return 1

#==============================================
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print 'Usage: python newsclaw.py url_pickl_file'
	urldic = pk.load(open(sys.argv[1],'r'))
	if get_contents(urldic):
		print '###SUCCESS###'






