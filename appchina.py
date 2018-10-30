# -*- coding:utf-8 -*-
import requests
import re
import os
from time import ctime
from pyquery import PyQuery as pyq

maxnum = 5
apk_url_head = 'http://www.appchina.com'
apk_url_tear = ''
apk_url = ''
apk_down = ''
apk_down_url = ''
os.makedirs("d:\workspace")
os.chdir("d:\workspace")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

def changepage(url,total_page):
        now_page = int(re.search('30(\d)', url).group(1))
        print (now_page)
        page_group = []
        for i in range(now_page,9):
            link = re.sub('30\d','30%s'%i,url,re.S)
            page_group.append(link)
        for j in range(10,total_page):
        	link = re.sub('3\d+','3%s'%j,url,re.S)
        	page_group.append(link)
        return page_group

url = 'http://www.appchina.com/category/301/1_1_1_1_0_0_0.html'
all_links = changepage(url,16)
testfile = "test.txt"
#print (ctime())
#print (all_links)
for i in all_links:
	#print(i)
	num = 0
	res = requests.get(i, headers=headers)
	query1 = pyq(res.text)
	item = query1('.has-border.app')
	for it in item:
		if num < maxnum:
			num += 1
			apk_url_tear = pyq(it).find('.has-border.download-now').attr('href')
			apk_url = apk_url_head + apk_url_tear
			#print(apk_url)
			apk = requests.get(apk_url,headers=headers)
			apk_down = pyq(apk.text).find('.download_app').attr('onclick')
			apk_name = pyq(apk.text).find('.app-name').text()
			if apk_down:
				apk_down_url = (re.search('http.*(?=\')', apk_down).group(0))
				print(apk_down_url)
				r = requests.get(apk_down_url)
				with open(apk_name+'.apk','wb') as code:
					code.write(r.content)
			else:
				continue
		else:
			break