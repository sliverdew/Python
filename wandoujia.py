# -*- coding:utf-8 -*-
import requests
import re
import os
from time import ctime
from pyquery import PyQuery as pyq
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

path = "d:\workspace"
if os.path.isdir(path):
	os.chdir("d:\workspace")
else :
	os.makedirs("d:\workspace")
	os.chdir()("d:\workspace")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

url = 'https://www.wandoujia.com/category/app?pos=w/crumb/appcategory'

res = requests.get(url, headers=headers)
query1 = pyq(res.text)
for item in query1('.cate-link').items():
	now_dir = path + '\\' + item.text()
	if os.path.isdir(now_dir):
		os.chdir(now_dir)
	else :
		os.makedirs(now_dir)
		os.chdir(now_dir)

driver=webdriver.Chrome()
driver.get('https://www.wandoujia.com/category/app')
driver.implicitly_wait(10)
for j in range(14):
	print('now:category list page')
	try:
		category_button = driver.find_elements_by_class_name('cate-link')
		cate_button = category_button[j]
		cate_button.click()
	except TimeoutException:
		driver.refresh()
		time.sleep(5)
		category_button = driver.find_elements_by_class_name('cate-link')
		cate_button = category_button[j]
		cate_button.click()
	print('now:apk list page')
	time.sleep(5)
	for i in range(24):
		print('now:apk list page')
		try:
			apk_button = driver.find_elements_by_class_name('detail-check-btn')
			apk_detail = apk_button[i]
			apk_detail.click()
			print('click,now:apk detail page')
		except TimeoutException:
			driver.back()
			continue
		time.sleep(5)
		try:
			checkbutton = driver.find_element_by_class_name('check-box')
			checkbutton.click()
		except TimeoutException:
			driver.back()
			continue
		time.sleep(5)
		try:
			dl_btn =  driver.find_element_by_class_name('normal-dl-btn ')
			dl_btn.click()
		except TimeoutException:
			driver.back()
			continue
		time.sleep(30)
		driver.back()
	driver.back()


'''
	item_url = item.attr.href
	print(item_url)
	item_res = requests.get(item_url, headers=headers)
	query2 = pyq(item_res.text)
	for apk in query2('.detail-check-btn').items():
		apk_url = apk.attr.href
		apk_res = requests.get(apk_url, headers=headers)
		apk_down = pyq(apk_res.text).find('.normal-dl-btn').attr('href')
		print(apk_down)
		apk_name = pyq(apk_res.text).find('.app-name').text()
		print(apk_name)
		r = requests.get(apk_down)
		with open(apk_name+'.apk','wb') as code:
			code.write(r.content)'''
