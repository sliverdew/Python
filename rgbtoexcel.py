#!/bin/sh
import os
import xlwt
import pandas as pd
import shutil
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

def copy_file(path_rgb):
	path_py = path_rgb + '\\' + 'py'
	path_result = path_rgb + '\\' + 'Results'
	file = []
	path1 = ''
	files = os.listdir(path_result)
	for f in files:
		if f.endswith('.csv'):
			path1 = path_result + '\\' + f
			file.append(path1)
		# adding exception handling
			source = path1
			f_lower = f.lower()
			print(f_lower)
			if 'd65' in f_lower :
				target = path_py + '\\' + f_lower.replace('d65','1')
			elif 'tl84' in f_lower and 'lowlight' not in f_lower:
				target = path_py + '\\' + f_lower.replace('tl84','2')
			elif 'cwf' in f_lower and 'lowlight' not in f_lower:
				target = path_py + '\\' + f_lower.replace('cwf','3')
			elif '_a_' in f_lower:
				target = path_py + '\\' + f_lower.replace('_a_','_4_')
			elif 'd50' in f_lower:
				target = path_py + '\\' + f_lower.replace('d50','5')
			elif 'tl84' in f_lower and 'lowlight' in f_lower:
				target = path_py + '\\' + f_lower.replace('tl84_lowlight','6')
			elif 'cwf' in f_lower and 'lowlight' in f_lower:
				target = path_py + '\\' + f_lower.replace('cwf_lowlight','7')
			else:
				target = path_py + '\\' + f
			shutil.copy(source, target)
def SFR(file):
	SFR_file = ''
	Cn_V = 0
	Cn_H = 0
	Ct_V = 0
	Ct_H = 0
	CA = 0
	#找到lwph这个文件
	for f in file:
		if 'lwph' in f:
			SFR_file = f
			print(SFR_file)
			break
	if SFR_file == '':
		return 0

	s_file = pd.read_csv(SFR_file,encoding='utf-8')
	df = pd.DataFrame(s_file) #使用pandas操作csv

	for i in range(len(df)-1):
		if 'above ctr' in df['Location'][i+1] and 'Horizontal' in df['H/V'][i+1]:
			Ct_H = int(df['MTF50'][i+1])

			CA = float(df['Chr Aber'][i+1])

		if 'below ctr' in df['Location'][i+1] and 'Vertical' in df['H/V'][i+1]:
			Ct_V = int(df['MTF50'][i+1])

		if 'of ctr' in df['Location'][i+1] and 'Horizontal' in df['H/V'][i+1]:
			Cn_H = int(df['MTF50'][i+1])

		if 'of ctr' in df['Location'][i+1] and 'Vertical' in df['H/V'][i+1]:
			Cn_V = int(df['MTF50'][i+1])

	print(Ct_V,Ct_H,Cn_V,Cn_H,CA)
	return Ct_V,Ct_H,Cn_V,Cn_H,CA

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
	if len(CC_file) == 0:
		return 0
	for n in CC_file:
		CC_name.append(int(n.split('_')[-2]))
	CC_name.sort()
	CC_file.sort()
	print(CC_file)
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
	#print(CC_name,Cmean,Cmax,Emean,Emax,sat,WB,SNR)
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
		if 'lf_y' in f:
			CS_file.append(f)
	#print(SC_file)
	if len(CS_file) == 0:
		return 0
	for n in CS_file:
		CS_name.append(n.split('_')[-3])
	CS_name.sort()
	CS_file.sort()
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
		#print(WORST[s],RG_MAX[s],RG_MIN[s],BG_MAX[s],BG_MIN[s])
	return CS_name,WORST,RG_MAX,RG_MIN,BG_MAX,BG_MIN

def GreyStep(file):
	GS_file = ''
	gs_list = []
	step = 0
	for f in file:
		if 'gray' in f:
			GS_file = f
	if GS_file == '':
		return 0
	g_file = pd.read_csv(GS_file,encoding='utf-8',header=None,sep = '\t',skip_blank_lines = False)
	df = pd.DataFrame(g_file)
	for i in range(20):
		gs_list.append(float(g_file.iloc[11+i][0].split(',')[1]))
		#print(gs_list[i])
	for j in range(len(gs_list)-1):
		if (gs_list[j] - gs_list[j+1] > 8):
			step += 1
	#print(step)

	return step

def Distortion(file):
	dis_file = ''
	dis = ''
	for f in file:
		if 'distor' in f:
			dis_file = f
	if dis_file == '':
		return 0
	#print(dis_file)
	d_file = pd.read_csv(dis_file,encoding='utf-8',header=None,sep = '\t',skip_blank_lines = False)
	#print(d_file.loc[8])
	dis = str(abs(float(d_file.loc[8][0].split(',')[1]))) + '%'
	#print(dis)
	return dis

#计算depth_rms
def depth_rms(path):
	Sn = []
	file = []
	glbal = []
	normal = []
	average = []
	in_rms = []

	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('depth_rms')

	for root, dirs, files in os.walk(path, topdown=False):
		for fi in files:
			if fi.endswith('.txt'):
				file.append(root + '\\' +fi)
				Sn.append(root.split('\\')[-2])
				print(file,Sn)
	for j in range(len(file)):
		with open(file[j],"r") as f:
			lines = f.readlines()
			glbal.append(lines[2].split(':')[1].strip())
			normal.append(lines[3].split(':')[1].strip())
			average.append(lines[7].split(':')[1].strip())
			in_rms.append(lines[9].split(':')[1].strip())
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('depth')
	worksheet.write(0,0,'Sn')
	worksheet.write(0,1,'Global integrity')
	worksheet.write(0,2,'Normal integrity')
	worksheet.write(0,3,'Central average')
	worksheet.write(0,4,'inliers_rms')
	for n in range(len(file)):
		worksheet.write(n+1,0,Sn[n])
		worksheet.write(n+1,1,glbal[n])
		worksheet.write(n+1,2,normal[n])
		worksheet.write(n+1,3,average[n])
		worksheet.write(n+1,4,in_rms[n])

	file_name = path + '\\' + 'depth_test.xls'
	workbook.save(file_name)



#主函数
if __name__ == '__main__':
	file = []
	path_rgb = r'C:\Users\kris\Desktop\R2011301200801499\rgb'
	path_py = path_rgb + '\\' +'py'
	path_depth = r'C:\Users\kris\Desktop\R2011301200801499\depth2'
	copy_file(path_rgb)
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('Summary')
	file = sea_file(path_py)
	file_name = ''
	rowx = 0
	Ct_V = Ct_H = Cn_V = Cn_H = CA = 0
	if SFR(file) != 0:
		Ct_V,Ct_H,Cn_V,Cn_H,CA = SFR(file)
	CC_name = sat = Cmean = Cmax = Emean = Emax = WB = SNR = []
	if ColorCheck(file) != 0:
		CC_name,Cmean,Cmax,Emean,Emax,sat,WB,SNR= ColorCheck(file)
	CS_name = WORST = RG_MAX = RG_MIN = BG_MAX = BG_MIN = []
	if Shading(file) != 0:
		CS_name,WORST,RG_MAX,RG_MIN,BG_MAX,BG_MIN= Shading(file)
	step = 0
	if GreyStep(file) != 0:
		step = GreyStep(file)
	dis = 0
	if Distortion(file) != 0:
		dis = Distortion(file)

	depth_rms(path_depth)

	#写SFR
	if SFR(file) != 0:
		worksheet.write(rowx,0,'SFR')
		worksheet.write_merge(rowx,rowx,1,2,'Horizontal')
		worksheet.write_merge(rowx,rowx,3,4,'Vertical')

		worksheet.write_merge(rowx+1,rowx+1,1,2,Ct_H)
		worksheet.write_merge(rowx+1,rowx+1,3,4,Ct_V)
		worksheet.write_merge(rowx+2,rowx+2,1,2,Cn_H)
		worksheet.write_merge(rowx+2,rowx+2,3,4,Cn_V)

		rowx = 3

	#写colorcheck
	if ColorCheck(file) != 0:
		worksheet.write(rowx,0,'COLORCHECK')
		for c in range(len(CC_name)):
			worksheet.write(rowx+5*c,1,CC_name[c])

			worksheet.write_merge(rowx+5*c,rowx+5*c,2,5,float(sat[c]))
			worksheet.write_merge(rowx+1+5*c,rowx+1+5*c,2,5,float(Cmean[c]))
			worksheet.write_merge(rowx+2+5*c,rowx+2+5*c,2,5,float(Cmax[c]))
			worksheet.write_merge(rowx+3+5*c,rowx+3+5*c,2,5,float(Emean[c]))
			worksheet.write_merge(rowx+4+5*c,rowx+4+5*c,2,5,float(Emax[c]))
		rowx = rowx + 5 * len(CC_name)

		#写AWB
		worksheet.write(rowx,0,'AWB')
		for w in range(len(CC_name)):
			worksheet.write(rowx+w,1,CC_name[w])
			worksheet.write_merge(rowx+w,rowx+w,2,5,WB[w])
		rowx = rowx + len(CC_name)

		#写SNR
		worksheet.write(rowx,0,'SNR')
		for r in range(len(CC_name)):
			worksheet.write(rowx+r,1,CC_name[r])
			for snr in range(4):
				worksheet.write(rowx+r,snr+2,float(SNR[r][snr]))
		rowx = rowx + len(CC_name)

	
	#写shading
	if Shading(file) != 0:
		worksheet.write(rowx,0,'Shading')
		for s in range(len(CS_name)):
			worksheet.write(rowx+s,1,CS_name[s])
			worksheet.write_merge(rowx+s,rowx+s,2,5,float(WORST[s]))
		rowx = rowx + len(CS_name)

	#写Color Shading
		worksheet.write(rowx,0,'Color Shading')
		for s in range(len(CS_name)):
			worksheet.write(rowx+4*s,1,CS_name[s])
			worksheet.write_merge(rowx+4*s,rowx+4*s+1,2,3,float(RG_MAX[s]))
			worksheet.write_merge(rowx+4*s,rowx+4*s+1,4,5,float(RG_MIN[s]))
			worksheet.write_merge(rowx+2+4*s,rowx+2+4*s+1,2,3,float(BG_MAX[s]))
			worksheet.write_merge(rowx+2+4*s,rowx+2+4*s+1,4,5,float(BG_MIN[s]))
		rowx = rowx + 4*len(CS_name)

	#写Grayscale
	if GreyStep(file) != 0:
		worksheet.write(rowx,0,'Grayscale')
		worksheet.write_merge(rowx,rowx,1,4,step)
		rowx = rowx + 1

	#写distortion
	if Distortion(file) != 0:
		worksheet.write(rowx,0,'Lens distortion')
		worksheet.write_merge(rowx,rowx,1,4,dis)
		rowx = rowx + 1

	#写HOV
	worksheet.write_merge(rowx,rowx,1,4,'65/55/30/')
	rowx = rowx + 1

	#写CA
	if SFR(file) != 0:
		worksheet.write(rowx,0,'CA')
		worksheet.write_merge(rowx,rowx,1,4,CA)
	
	#全部写完啦
	file_name = path_rgb + '\\' + 'RGB_test.xls'
	workbook.save(file_name) 
