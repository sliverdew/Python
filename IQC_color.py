# -*- coding: UTF-8 -*-

import cv2
import os
import re
import time
import math


pic_path = input("图片所在文件夹：")
flag = input("设置判断色偏的阈值（默认为1.5）：")

if flag == '':
	flag = 1.5
flag = float(flag)


def color_cast(pic_path,file,each_pic_path,flag):
	frame = cv2.imread(each_pic_path)  # 读入pic
	#cv2.imshow("capture", frame)      #显示
	#计算色偏值
	img = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
	l_channel, a_channel, b_channel = cv2.split(img)
	h,w,_ = img.shape
	da = a_channel.sum()/(h*w)-128
	db = b_channel.sum()/(h*w)-128
	histA = [0]*256
	histB = [0]*256
	for q in range(h):
		for j in range(w):
			ta = a_channel[q][j]
			tb = b_channel[q][j]
			histA[ta] += 1
			histB[tb] += 1
	msqA = 0
	msqB = 0
	for y in range(256):
		msqA += float(abs(y-128-da))*histA[y]/(w*h)
		msqB += float(abs(y - 128 - db)) * histB[y] / (w * h)
	result = math.sqrt(da*da+db*db)/math.sqrt(msqA*msqA+msqB*msqB)

	#筛出色偏图片
	print("%s    d/m = %s" %(each_pic_path,round(result,2)), file = f)
	if result > flag:
		sn_list = each_pic_path.split('\\')
		for i in sn_list:
			if re.search(r'^R\d{16}',i):
				sn = i
		err_dir = pic_path + '\\' + 'err_pic'
		if os.path.exists(err_dir) != True:
			os.makedirs(err_dir)

		err_pic_path = pic_path + '\\' + 'err_pic' + '\\' + str(sn) + '.jpg'
		print('sn: %s   偏色值:%f，超过色偏的阈值' %(file,result))
		os.system('copy %s %s' %(each_pic_path,err_pic_path))	
	else:
		print('%s 偏色值:%f' %(file,result))
	cv2.waitKey(1)
	#cv2.destroyAllWindows()   #销毁显示窗口

if __name__ == '__main__':

	begin = time.time()
	f = open("%s\\color_cast.txt" %(pic_path), "w")
	for root,dirs,files in os.walk(pic_path):
		for file in files:
				if file.endswith(".jpg"):
					each_pic_path = str(os.path.join(root,file))
					if "rgb" in each_pic_path:
						color_cast(pic_path,file,each_pic_path,flag)
	f.close()
	end = time.time()
	print('----finish in %d seconds----' % (end - begin))
