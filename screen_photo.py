#/bin/sh
#
#python screen_photo.py选择执行方式
#1.65距离，选出65距离文件夹下第一张照片
#2.全距离，选出全距离文件夹下第一张照片
#3.全距离全角度，在全距离文件夹下，每隔7张照片选下一个角度，误差较大。
#4.主函数下可以修改原始目录路径和目的目录路径
#5.cp_angle函数内可以修改选取角度照片时的间隔张数
#--by wwl 20191211
import os
import xlwt
import re
import shutil
import filetype
#遍历文件夹   
def iter_files(rootDir,file_list,dir_list):
	#遍历根目录
	for root,dirs,files in os.walk(rootDir):
		for file in files:
			file_name = os.path.join(root,file)
			file_list.append(file_name)
			dir_list.append(root)
			#print(file_name)
#筛选rgb文件夹
def get_rgb_list(file_list,dir_list):
	n = 0
	for n in range(len(file_list)):
		if re.search('rgb',dir_list[n]) == None:
			continue
		else:
			rgb_dir_list.append(dir_list[n])
			rgb_file_list.append(file_list[n])

#筛选rgb文件夹下的第一个文件
def target(rgb_file_list,rgb_dir_list):
	count = 0
	each = 0
	co = 0
	for co in range(len(rgb_dir_list)-1,-1,-1):
		if rgb_dir_list[co] == rgb_dir_list[co-1]:
			#rgb_dir_list.remove(rgb_dir_list[co])
			del rgb_file_list[co]
		else :
			count += 1
	#检查筛选结果
	#for each in range(len(rgb_file_list)):
		#print(rgb_file_list[each])
	#print(count)

def cp_65(rgb_file_list):
	c_file_list = rgb_file_list
	dst_file_name = ''
	time = ''
	name = ''
	q = 0
	p = 0
	for q in range(len(rgb_file_list)-1,-1,-1):
		if re.search('\d+-35',rgb_file_list[q]) == None:
			del(c_file_list[q])
		else :
			continue
	for p in range(len(c_file_list)):
		try:
			time = re.search('\d{8}',c_file_list[p])
			name = re.search('\w+\d+-\d+(-\d)*',c_file_list[p])
			#print (time.group(0),name.group(0))
			dst_file_name = dstDir + '\\' + time.group(0) + '_' + name.group(0) + '.jpg'
			print(dst_file_name)
			shutil.copyfile(rgb_file_list[p],dst_file_name)
		except OSError:
			pass
		continue
def cp_all(rgb_file_list):
	dst_file_name = ''
	time = ''
	name = ''
	p = 0
	for p in range(len(rgb_file_list)):
		try :
			time = re.search('\d{8}',rgb_file_list[p])
			name = re.search('\w+\d+-\d+(-\d)*',rgb_file_list[p])
			#print (time.group(0),name.group(0))
			if re.search('\d+-35',rgb_file_list[p]) == None:
				dst_file_name = dstDir + '\\' + time.group(0) + '_' + name.group(0) + '.jpg'
				print(dst_file_name)
				shutil.copyfile(rgb_file_list[p],dst_file_name)
		except OSError:
			pass
		continue
def str_add(A,num):
	A1 = 0 #加法前数字长度
	B = ''
	A1 = len(str(int(A)+num))
	B = A[0:len(A)-A1] + str((int(A)+num)) #叠加后恢复原始数字
	return B

def cp_angle(rgb_file_list):
	dst_file_name = ''
	time = ''
	name = ''
	dirs = ''
	p = 0
	u = 1
	for p in range(len(rgb_file_list)):
		try :
			time = re.search('\d{8}',rgb_file_list[p]).group(0)
			dirs = re.search('\w+\d+-\d+(-\d)*',rgb_file_list[p]).group(0)
			name = re.findall('\d{8}',rgb_file_list[p])[1]
			for u in range(1,5):
				#print(name,str_add(name,u*7))
				dst_file_name = dstDir + '\\' + time + '_' + dirs + '_'+ str_add(name,u*7) + '.jpg'
				len_root = len(rgb_file_list[p]) - 12
				#print(len_root)
				root_file_name = rgb_file_list[p][0:len_root] + str_add(rgb_file_list[p][-12:-4],u*7) + '.jpg'
				print(root_file_name)
				shutil.copyfile(root_file_name,dst_file_name)
		except OSError:
			pass
		continue

if __name__ == "__main__":
	#原始目录路径
	rootDir = r"K:\FaceCapture\RK"
	#目的目录路径
	dstDir = r"D:\RK -all -angle"
    #用来存放所有的文件路径
	file_list = []
    #用来存放所有的目录路径
	dir_list = []
    #用来存放所有的rgb目录路径
	rgb_dir_list = []
    #用来存放所有的rgb文件路径
	rgb_file_list = []
	#用来存放所有的65距离文件路径
	c_file_list = []
	li = {'A':cp_65,'B':cp_all,'C':cp_angle}
	print ("请输入要筛选的文件，A：65距离 B：全距离 C: 全距离全角度")
	switch = li.get(input('>'))
	iter_files(rootDir,file_list,dir_list)
	get_rgb_list(file_list,dir_list)
	target(rgb_file_list,rgb_dir_list)
	switch(rgb_file_list)



