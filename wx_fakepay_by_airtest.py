# -*- encoding=utf8 -*-

from airtest.core.api import *
import os
import time
import datetime

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
count = 0
file_name = ''
file_folder_A = r'C:\snap_A\\'
file_folder_B = r'C:\snap_B\\'
if not os.path.exists(file_folder_A):
    os.mkdir(file_folder_A)
if not os.path.exists(file_folder_B):
    os.mkdir(file_folder_B)

input('输入回车开始运行')

while True:
    poco("com.tencent.wxpay.imagefacesign:id/pay").click()
    count += 1
    try :
        wait(Template(r"tpl1594621775657.png", record_pos=(0.0, -0.266), resolution=(800, 1280)))
    except:
        if poco("com.tencent.wxpayface:id/tv_sdk_face_error_content").exists():
            keyevent("4")
    else:
        file_name = str(count) + '_' + str(datetime.datetime.now()).replace(" ", "_").split('.')[0].replace("-", "_").replace(':','') + '.png'
        print(file_name)
        if count % 2 == 1:
            os.system('adb shell screencap -p /sdcard/%s'%file_name)
            os.system('adb pull /sdcard/%s %s'%(file_name,file_folder_A))
        else :
            os.system('adb shell screencap -p /sdcard/%s'%file_name)
            os.system('adb pull /sdcard/%s %s'%(file_name,file_folder_B))  
        print("test count %d"%count)
        keyevent("4")