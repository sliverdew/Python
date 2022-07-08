# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np
import sys
import importlib
import re

importlib.reload(sys)


name = []
neirong = []
file = ''

file = pd.read_csv('20w.txt',sep=',',encoding='utf-8',engine='python',names=['name', 'comment'])
df = pd.DataFrame(file) 

for i in range(len(df)):
	df.loc[i,'comment'] = df.loc[i,'comment'].replace(' ','')
	df.loc[i,'comment'] = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",df.loc[i,'comment'])
	print(df.loc[i,'comment'])

result1 = df.loc[:,'name'].value_counts()
result2 = df.loc[:,'comment'].value_counts()

df1 = pd.DataFrame({'name':result1.index, 'count':result1.values})
df2 = pd.DataFrame({'comment':result2.index, 'count':result2.values})



writer = pd.ExcelWriter('result.xlsx')
df1.to_excel(writer,"name")
df2.to_excel(writer,"comment")
writer.save() 
