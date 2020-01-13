#/bin/sh
#
import os
import shutil
def iter_files(rootDir,file_list,dir_list):
	#遍历根目录
	for root,dirs,files in os.walk(rootDir):
		for file in files:
			file_name = os.path.join(root,file)
			file_list.append(file_name)
			dir_list.append(root)
			#print(file_name)
def cp_all(file_list,dir_list,dstDir):
	dst_file_name = ''
	p = 0
	q = 0
	for p in range(len(file_list)-1,-1,-1):
		try:
			dst_file_name = dstDir + file_list[p][14:]
			dst_file = dstDir + dir_list[p][14:]
			#print(dst_file)
			if not os.path.isdir(dst_file):
				os.makedirs(dst_file)
			shutil.copyfile(file_list[p],dst_file_name)
			del file_list[p]
		except OSError:
			pass
		continue
	for q in range(len(file_list)):
		print (file_list[q])

if __name__ == "__main__":
	#原始目录路径
	rootDir = r"K:\FaceCapture"
	#目的目录路径
	dstDir = r"K:\FaceCapture_new"
	#用来存放所有的文件路径
	file_list = []
	#用来存放所有的目录路径
	dir_list = []
	#用来存放所有的rgb目录路径
	rgb_dir_list = []
	#用来存放所有的rgb文件路径
	iter_files(rootDir,file_list,dir_list)
	cp_all(file_list,dir_list,dstDir)

