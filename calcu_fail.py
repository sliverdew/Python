#/bin/sh
import re
import os

def iter_files(Dir):
	contents = []
	content = ''
	results = []
	result = ''
	#遍历根目录
	for root,dirs,files in os.walk(Dir):
		for file in files:
			count1 = 0
			count2 = 0
			file_name = os.path.join(root,file)
			with open(file_name,mode='rb+') as f:
				content = f.read()
				content = content.decode('utf-8','ignore') #按UTF-8格式解码，这里需要txt文件以ANSI格式编码
				pat1 = re.compile("decoded symbol")
				pat2 = re.compile("QR  Identify the results")
				results1 = pat1.findall(content) #根据正则表达式筛选全部内容
				results2 = pat2.findall(content)
				for result1 in results1:
					count1 += 1
				for result2 in results2:
					count2 += 1
			print(file_name,count1,count2)
if __name__ == "__main__":
	path = r"C:\Users\kris\Desktop\changduceshi"
	iter_files(path)
