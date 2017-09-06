#!/usr/bin/python
# -*- coding: UTF-8 -*-
from xml.dom import minidom
import re
from pyadb import adb
import time
import os
px=0
py=0
adb.shell('am start com.android.settings/.Settings$AccessibilitySettingsActivity')
time.sleep(5)
adb.shell('uiautomator dump /sdcard/set.xml')
time.sleep(2)
adb.pull('/sdcard/set.xml', os.getcwd())
dom = minidom.parse('set.xml')
root = dom.documentElement
nodes = root.getElementsByTagName('node')
for node in nodes:
    text = node.getAttribute('text')
    if text == '语言和输入法':
        bound = node.getAttribute('bounds')
        print(bound)
        x,y = eval(re.sub("\]\[","],[",bound))
        px = (x[0]+y[0])/2
        py = (x[1]+y[1])/2
        print (px,py)
adb.shell('input tap ' + str(px) + ' ' + str(py))
adb.shell('input keyevent 20')
adb.shell('input keyevent 66')
adb.shell('input keyevent 66')
time.sleep(1)
adb.shell('input keyevent 66')
count = 0
i=1
while(i<13):
    for co in range(0,count):
        adb.shell('input keyevent 93')
    for j in range(0,i):
        adb.shell('input keyevent 20')
    adb.shell('input keyevent 66')
    time.sleep(1)
    adb.shell('input keyevent 66')
    if i == 12:
        i=1
        count+=1
    else:
        i+=1