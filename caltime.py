#/bin/sh
import re
import os

def iter_files(Dir):
	contents = []
	content = ''
	results = []
	result = ''
	count = []
	#遍历根目录
	for root,dirs,files in os.walk(Dir):
		for file in files:
			file_name = os.path.join(root,file)
			with open(file_name,mode='rb+') as f:
				content = f.read()
				content = content.decode('utf-8','ignore') #按UTF-8格式解码，这里需要txt文件以ANSI格式编码
				pat1 = re.compile("decoded symbol.+\s.+frames = \d+")
				results = pat1.findall(content) #根据正则表达式筛选全部内容
				for result in results:
					#print(result.split(' ')[-1])
					count.append(int(result.split(' ')[-1]))
			avg = sum(count)/(len(count)*1.0)
			print(file,len(count),avg)
			count.clear()

if __name__ == "__main__":
	path = r"C:\Users\kris\Desktop\changduceshi"
	iter_files(path)
