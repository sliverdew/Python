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
	os.chdir("d:\workspace")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

url = 'https://sj.qq.com/myapp/category.htm?orgame=1'

driver=webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)

dl_btn =  driver.find_element_by_class_name('toggle more')
dl_btn.click()
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