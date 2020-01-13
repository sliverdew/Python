#/bin/sh
import cv2
import base64
import numpy as np
import time
import os
 
from aip import AipBodyAnalysis
 
# 在百度云中申请，每天各接口有 50000 次调用限制.
startTime = time.time()
APP_ID = '18099748'
API_KEY = 'X9GnxnENYzOVLP0znGDStfla'
SECRET_KEY = 'BZt0INzLkM6MYnUjL56im8REBRC5AoUP'
 
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

def body_del(imgfile,dir):
	out_path = ''
	ori_img = cv2.imread(imgfile)
	height, width, _ = ori_img.shape
 
	with open(imgfile, 'rb') as fp:
		img_info = fp.read()
 
	seg_res = client.bodySeg(img_info)
	labelmap = base64.b64decode(seg_res['labelmap'])
	nparr = np.fromstring(labelmap, np.uint8)
	labelimg = cv2.imdecode(nparr,1)
	labelimg = cv2.resize(labelimg,(width,height), interpolation=cv2.INTER_NEAREST)
	new_img = np.where(labelimg==1, 255, labelimg)
	maskfile = imgfile.replace('.jpg', '_mask.png')
	#cv2.imwrite(maskfile, new_img)
	
	res_imgfile = imgfile.replace('.jpg', '_res.jpg')
	out_path = dir + '\\' + res_imgfile[18:]
	result = cv2.bitwise_and(ori_img, new_img)
	cv2.imwrite(out_path, result)
	endTime = time.time()
	print("useTime: ", endTime-startTime)
	print('Done.')

path = r'D:\RK -all -angle'
out_dir = r'D:\handled'
files = []
files = os.listdir(path)
for file in files:
	body_del(path + '\\' + file,out_dir)
	#print(path + '\\' + file)
