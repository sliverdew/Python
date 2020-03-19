#!/bin/sh
import os
import xlwt
import pandas as pd

def sea_file(path):
	file = []
	path1 = ''
	files = os.listdir(path)
	for f in files:
		if f.endswith('.csv'):
			path1 = path + '\\' + f
			file.append(path1)
			#print(path1)
	return file

def SFR(file):
	SFR_file = ''
	H_value = 9999999
	V_value = 9999999
	Corner_value = 9999999
	CA = 0
	#找到lwph这个文件
	for f in file:
		if 'lwph' in f:
			SFR_file = f
			#print(SFR_file)
			break
	s_file = pd.read_csv(SFR_file,encoding='utf-8')
	df = pd.DataFrame(s_file) #使用pandas操作csv

	for i in range(len(df)-1):
		if 'above ctr' in df['Location'][i+1]:
			if H_value > int(df['MTF50'][i+1]):
				H_value = int(df['MTF50'][i+1])
			CA = float(df['Chr Aber'][i+1])
			print(CA)
		if 'below ctr' in df['Location'][i+1]:
			if V_value > int(df['MTF50'][i+1]):
				V_value = int(df['MTF50'][i+1])
		if 'of ctr' in df['Location'][i+1]:
			if Corner_value > int(df['MTF50'][i+1]):
				Corner_value = int(df['MTF50'][i+1])
	print(H_value,V_value,Corner_value)
	return H_value,V_value,Corner_value,CA


def ColorCheck(file):
	CC_file = []
	CC_name = []
	CC_dict = {}
	sat = []
	Cmean = []
	Cmax = []
	Emean = []
	Emax = []
	WB = []
	SNR = []
	#找到colorcheck的所有文件
	for f in file:
		if 'color' in f:
			CC_file.append(f)
	#print(CC_file)
	for n in CC_file:
		CC_name.append(int(n.split('_')[-2]))
	CC_name.sort()
	#print(CC_name)
	for l in range(len(CC_name)):
		c_file = pd.read_csv(CC_file[l],encoding='utf-8',header=None,sep = '\t',skip_blank_lines = False)
		df = pd.DataFrame(c_file) 
		sat.append((c_file.loc[144])[0].split(',')[1])
		Cmean.append((c_file.loc[148])[0].split(',')[1])
		Cmax.append((c_file.loc[150])[0].split(',')[1])
		Emean.append((c_file.loc[151])[0].split(',')[1])
		Emax.append((c_file.loc[153])[0].split(',')[1])
		#print(CC_name[l],sat[l],dC[l],dE[l])
		#------获取白平衡值--------#
		wbs = 0
		wbc = 0
		for j in range(7,10):
			if wbs < float((c_file.loc[j])[0].split(',')[9]):
				wbs = float(((c_file.loc[j])[0].split(',')[9]))
			if wbc < float(((c_file.loc[j])[0].split(',')[10])):
				wbc = float(((c_file.loc[j])[0].split(',')[10]))
		WB.append(wbs)
		#print(WB[l])
		#------获取SNR值--------#
		SNR.append(c_file.loc[57][0].split(',')[1:5])
		#print(SNR[l])
	print(CC_name,Cmean,Cmax,Emean,Emax,sat,WB,SNR)
	return CC_name,Cmean,Cmax,Emean,Emax,sat,WB,SNR

def Shading(file):
	CS_file = []
	CS_name = []
	WL = []
	WLB = []
	RG_MIN = []
	RG_MAX = []
	BG_MIN = []
	BG_MAX = []
	WORST = []
	MEAN = []
	#找到全部shading文件
	for f in file:
		if 'LF_Y' in f:
			CS_file.append(f)
	#print(SC_file)
	for n in CS_file:
		CS_name.append(n.split('_')[-3])
	CS_name.sort()
	#print(SC_name)
	for s in range(len(CS_name)):
		s_file = pd.read_csv(CS_file[s],encoding='utf-8',header=None,sep = '\t',skip_blank_lines = False)
		df = pd.DataFrame(s_file)
		worst = s_file.loc[14][0].split(',')[1]
		#worstb = s_file.loc[14][0].split(',')[1]
		#mean = s_file.loc[13][0].split(',')[1]
		#meanb = s_file.loc[15][0].split(',')[1]
		WORST.append(worst)
		#MEAN.append(mean + '(' + meanb + '%' + ')')
		RG_MAX.append(s_file.loc[36][0].split(',')[2])
		RG_MIN.append(s_file.loc[37][0].split(',')[2])
		BG_MAX.append(s_file.loc[36][0].split(',')[6])
		BG_MIN.append(s_file.loc[37][0].split(',')[6])
		print(WORST[s],RG_MAX[s],RG_MIN[s],BG_MAX[s],BG_MIN[s])
	return CS_name,WORST,RG_MAX,RG_MIN,BG_MAX,BG_MIN

def GreyStep(file):
	GS_file = ''
	gs_list = []
	step = 0
	for f in file:
		if 'grey' in f:
			GS_file = f
	g_file = pd.read_csv(GS_file,encoding='utf-8',header=None,sep = '\t',skip_blank_lines = False)
	df = pd.DataFrame(g_file)
	for i in range(20):
		gs_list.append(float(g_file.iloc[11+i][0].split(',')[1]))
		print(gs_list[i])
	for j in range(len(gs_list)-1):
		if (gs_list[j] - gs_list[j+1] > 8):
			step += 1
	print(step)

	return step

def Distortion(file):
	dis_file = ''
	dis = ''
	for f in file:
		if 'distor' in f:
			dis_file = f
	#print(dis_file)
	d_file = pd.read_csv(dis_file,encoding='utf-8',header=None,sep = '\t',skip_blank_lines = False)
	print(d_file.loc[8])
	dis = abs(float(d_file.loc[8][0].split(',')[1]))
	print(dis)
	return dis



#主函数
if __name__ == '__main__':
	file = []
	path = r'K:\module1\Results'
	file = sea_file(path)
	file_name = ''
	H_value = V_value = Corner_value = CA = 0
	H_value,V_value,Corner_value,CA = SFR(file)
	CC_name = sat = Cmean = Cmax = Emean = Emax = WB = SNR = []
	CC_name,Cmean,Cmax,Emean,Emax,sat,WB,SNR= ColorCheck(file)
	CS_name = WORST = RG_MAX = RG_MIN = BG_MAX = BG_MIN = []
	CS_name,WORST,RG_MAX,RG_MIN,BG_MAX,BG_MIN= Shading(file)
	step = 0
	step = GreyStep(file)
	dis = 0
	dis = Distortion(file)

	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('Summary')

	#写SFR
	worksheet.write(0,0,'SFR')
	worksheet.write(0,1,'Horizontal')
	worksheet.write(0,2,'Vertical')
	worksheet.write(0,3,'Corner')
	worksheet.write(1,1,H_value)
	worksheet.write(1,2,V_value)
	worksheet.write(1,3,Corner_value)
	#workbook.save('RGB_test.xls')

	#写colorcheck
	worksheet.write(2,0,'COLORCHECK')
	worksheet.write(6,0,'WB')
	worksheet.write(7,0,'SNR')
	for c in range(0,5*len(CC_name),5):
		worksheet.write(c+2,1,CC_name[c//5])
		worksheet.write(c+2,2,'color saturation')
		worksheet.write(c+3,2,'MEAN(ΔC)')
		worksheet.write(c+4,2,'MAX(ΔC)')
		worksheet.write(c+5,2,'MEAN(ΔE)')
		worksheet.write(c+6,2,'MAX(ΔE)')

		worksheet.write_merge(c+2,c+2,3,6,float(sat[c//5]))
		worksheet.write_merge(c+3,c+3,3,6,float(Cmean[c//5]))
		worksheet.write_merge(c+4,c+4,3,6,float(Cmax[c//5]))
		worksheet.write_merge(c+5,c+5,3,6,float(Emean[c//5]))
		worksheet.write_merge(c+6,c+6,3,6,float(Emax[c//5]))
	#workbook.save('RGB_test.xls')
	#写AWB
	worksheet.write(37,0,'AWB')
	for w in range(len(CC_name)):
		worksheet.write(37+w,1,CC_name[w])
		worksheet.write_merge(37+w,37+w,2,5,WB[w])
	#workbook.save('RGB_test.xls')
	
	#写SNR
	worksheet.write(44,0,'SNR')
	for r in range(len(CC_name)):
		worksheet.write(44+r,1,CC_name[r])
		for snr in range(4):
			worksheet.write(44+r,snr+2,float(SNR[r][snr]))

	#workbook.save('RGB_test.xls')
	
	#写shading
	worksheet.write(51,0,'Shading')
	for s in range(len(CS_name)):
		worksheet.write(51+s,1,CS_name[s])
		worksheet.write_merge(51+s,51+s,2,5,float(WORST[s]))

	#workbook.save('RGB_test.xls')

	#写Color Shading
	worksheet.write(56,0,'Color Shading')
	for s in range(len(CS_name)):
		worksheet.write(56+4*s,1,CS_name[s])
		worksheet.write_merge(56+4*s,56+4*s+1,2,3,float(RG_MAX[s]))
		worksheet.write_merge(56+4*s,56+4*s+1,4,5,float(RG_MIN[s]))
		worksheet.write_merge(58+4*s,58+4*s+1,2,3,float(BG_MAX[s]))
		worksheet.write_merge(58+4*s,58+4*s+1,4,5,float(BG_MIN[s]))

	#workbook.save('RGB_test.xls')

	#写Grayscale
	worksheet.write(76,0,'Grayscale')
	worksheet.write_merge(76,76,1,4,step)
	#workbook.save('RGB_test.xls')
	
	#写distortion
	worksheet.write(77,0,'Lens distortion')
	worksheet.write_merge(77,77,1,4,dis)

	#写CA
	worksheet.write(78,0,'CA')
	worksheet.write_merge(78,78,1,4,CA)

	file_name = path + '\\' + 'RGB_test.xls'
	workbook.save(file_name) 