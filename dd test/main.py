# -*- coding: UTF-8 -*-
import os
import xlwt
import re
import wx
import UI_main
import threading
from tkinter import messagebox

test_count = 3

class main_window(UI_main.MyFrame1): 

	def SetPerformance(self,event):
		os.system('adb shell "echo performance | tee $(find /sys/ -name *governor)"')

	def Start_Test(self,event):
		t1 = threading.Thread(target=main_test,args=(main_win,))
		t1.start()


def TestEmmc(ct):

	worksheet1.write(5,0,r'EMMC')
	worksheet1.write(6,0,'4G-READ')
	worksheet1.write(7,0,'4G-WRITE')
	worksheet1.write(8,0,'1G-READ')
	worksheet1.write(9,0,'1G-WRITE')

	for j in range(ct):

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')
#跑4G
		EMMC4_w = os.popen('adb shell "time dd if=/dev/zero of=/media/test%d.dbf bs=2M count=2048 conv=fsync"'%j)
		EMMC4_w_result = EMMC4_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_w_result)
		emmc4_w = re.search('，\d+ MB/s',EMMC4_w_result).group().split('，')[1].split(' ')[0]
		print(emmc4_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC4_r = os.popen('adb shell "time dd if=/media/test%d.dbf of=/dev/null bs=2M"'%j)
		EMMC4_r_result = EMMC4_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		emmc4_r = re.search('，\d+ MB/s',EMMC4_r_result).group().split('，')[1].split(' ')[0]
		print(EMMC4_r_result)
		print(emmc4_r)

		os.system('adb shell "rm /media/test%d.dbf"'%j)

		worksheet1.write(6,j+1,emmc4_r)
		worksheet1.write(7,j+1,emmc4_w)

#跑1G
	for i in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_w = os.popen('adb shell "time dd if=/dev/zero of=/media/test%d.dbf bs=512k count=2048 conv=fsync"'%i)
		EMMC1_w_result = EMMC1_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_w_result)
		emmc1_w = re.search('，\d+ MB/s',EMMC1_w_result).group().split('，')[1].split(' ')[0]
		print(emmc1_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_r = os.popen('adb shell "time dd if=/media/test%d.dbf of=/dev/null bs=512k"'%i)
		EMMC1_r_result = EMMC1_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_r_result)
		emmc1_r = re.search('，\d+ MB/s',EMMC1_r_result).group().split('，')[1].split(' ')[0]
		print(emmc1_r)

		os.system('adb shell "rm /media/test%d.dbf"'%i)

		worksheet1.write(8,i+1,emmc1_r)
		worksheet1.write(9,i+1,emmc1_w)

	workbook.save('DD test.xls')

def USB20(node,ct):
	os.system('adb shell "umount %s"'%node)
	os.system('adb shell "mount %s /sdcard"'%node)

	worksheet1.write(10,0,r'USB2.0')
	worksheet1.write(11,0,'4G-READ')
	worksheet1.write(12,0,'4G-WRITE')
	worksheet1.write(13,0,'1G-READ')
	worksheet1.write(14,0,'1G-WRITE')

	for j in range(ct):

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')
#跑4G
		EMMC4_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=2M count=2048 conv=fsync"'%j)
		EMMC4_w_result = EMMC4_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_w_result)
		emmc4_w = re.search('，\d+ MB/s',EMMC4_w_result).group().split('，')[1].split(' ')[0]
		print(emmc4_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC4_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=2M"'%j)
		EMMC4_r_result = EMMC4_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_r_result)
		emmc4_r = re.search('，\d+ MB/s',EMMC4_r_result).group().split('，')[1].split(' ')[0]
		print(emmc4_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%j)

		worksheet1.write(11,j+1,emmc4_r)
		worksheet1.write(12,j+1,emmc4_w)

#跑1G
	for i in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=512k count=2048 conv=fsync"'%i)
		EMMC1_w_result = EMMC1_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_w_result)
		emmc1_w = re.search('，\d+ MB/s',EMMC1_w_result).group().split('，')[1].split(' ')[0]
		print(emmc1_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=512k"'%i)
		EMMC1_r_result = EMMC1_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_r_result)
		emmc1_r = re.search('，\d+ MB/s',EMMC1_r_result).group().split('，')[1].split(' ')[0]
		print(emmc1_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%i)

		worksheet1.write(13,i+1,emmc1_r)
		worksheet1.write(14,i+1,emmc1_w)

	workbook.save('DD test.xls')

def USB30(node,ct):

	os.system('adb shell "umount %s"'%node)
	os.system('adb shell "mount %s /sdcard"'%node)

	worksheet1.write(15,0,r'USB3.0')
	worksheet1.write(16,0,'4G-READ')
	worksheet1.write(17,0,'4G-WRITE')
	worksheet1.write(18,0,'1G-READ')
	worksheet1.write(19,0,'1G-WRITE')

	for j in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')
#跑4G
		EMMC4_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=2M count=2048 conv=fsync"'%j)
		EMMC4_w_result = EMMC4_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_w_result)
		emmc4_w = re.search('，\d+ MB/s',EMMC4_w_result).group().split('，')[1].split(' ')[0]
		print(emmc4_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC4_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=2M"'%j)
		EMMC4_r_result = EMMC4_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_r_result)
		emmc4_r = re.search('，\d+ MB/s',EMMC4_r_result).group().split('，')[1].split(' ')[0]
		print(emmc4_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%j)

		worksheet1.write(16,j+1,emmc4_r)
		worksheet1.write(17,j+1,emmc4_w)

#跑1G
	for i in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=512k count=2048 conv=fsync"'%i)
		EMMC1_w_result = EMMC1_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_w_result)
		emmc1_w = re.search('，\d+ MB/s',EMMC1_w_result).group().split('，')[1].split(' ')[0]
		print(emmc1_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=512k"'%i)
		EMMC1_r_result = EMMC1_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_r_result)
		emmc1_r = re.search('，\d+ MB/s',EMMC1_r_result).group().split('，')[1].split(' ')[0]
		print(emmc1_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%i)

		worksheet1.write(18,i+1,emmc1_r)
		worksheet1.write(19,i+1,emmc1_w)

	workbook.save('DD test.xls')

def SATASSD(node,ct):
	os.system('adb shell "umount %s"'%node)
	os.system('adb shell "mount %s /sdcard"'%node)

	worksheet1.write(20,0,r'SATA-SSD')
	worksheet1.write(21,0,'4G-READ')
	worksheet1.write(22,0,'4G-WRITE')
	worksheet1.write(23,0,'1G-READ')
	worksheet1.write(24,0,'1G-WRITE')

	for j in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')
#跑4G
		EMMC4_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=2M count=2048 conv=fsync"'%j)
		EMMC4_w_result = EMMC4_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_w_result)
		emmc4_w = re.search('，\d+ MB/s',EMMC4_w_result).group().split('，')[1].split(' ')[0]
		print(emmc4_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC4_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=2M"'%j)
		EMMC4_r_result = EMMC4_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_r_result)
		emmc4_r = re.search('，\d+ MB/s',EMMC4_r_result).group().split('，')[1].split(' ')[0]
		print(emmc4_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%j)

		worksheet1.write(21,j+1,emmc4_r)
		worksheet1.write(22,j+1,emmc4_w)

#跑1G
	for i in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=512k count=2048 conv=fsync"'%i)
		EMMC1_w_result = EMMC1_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_w_result)
		emmc1_w = re.search('，\d+ MB/s',EMMC1_w_result).group().split('，')[1].split(' ')[0]
		print(emmc1_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=512k"'%i)
		EMMC1_r_result = EMMC1_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_r_result)
		emmc1_r = re.search('，\d+ MB/s',EMMC1_r_result).group().split('，')[1].split(' ')[0]
		print(emmc1_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%i)

		worksheet1.write(23,i+1,emmc1_r)
		worksheet1.write(24,i+1,emmc1_w)

	workbook.save('DD test.xls')

def PCIESSD(node,ct):
	os.system('adb shell "umount %s"'%node)
	os.system('adb shell "mount %s /sdcard"'%node)

	worksheet1.write(25,0,r'PCIE-SSD')
	worksheet1.write(26,0,'4G-READ')
	worksheet1.write(27,0,'4G-WRITE')
	worksheet1.write(28,0,'1G-READ')
	worksheet1.write(29,0,'1G-WRITE')

	for j in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')
#跑4G
		EMMC4_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=2M count=2048 conv=fsync"'%j)
		EMMC4_w_result = EMMC4_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_w_result)
		emmc4_w = re.search('，\d+ MB/s',EMMC4_w_result).group().split('，')[1].split(' ')[0]
		print(emmc4_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC4_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=2M"'%j)
		EMMC4_r_result = EMMC4_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_r_result)
		emmc4_r = re.search('，\d+ MB/s',EMMC4_r_result).group().split('，')[1].split(' ')[0]
		print(emmc4_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%j)

		worksheet1.write(26,j+1,emmc4_r)
		worksheet1.write(27,j+1,emmc4_w)

#跑1G
	for i in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=512k count=2048 conv=fsync"'%i)
		EMMC1_w_result = EMMC1_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_w_result)
		emmc1_w = re.search('，\d+ MB/s',EMMC1_w_result).group().split('，')[1].split(' ')[0]
		print(emmc1_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=512k"'%i)
		EMMC1_r_result = EMMC1_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_r_result)
		emmc1_r = re.search('，\d+ MB/s',EMMC1_r_result).group().split('，')[1].split(' ')[0]
		print(emmc1_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%i)

		worksheet1.write(28,i+1,emmc1_r)
		worksheet1.write(29,i+1,emmc1_w)

	workbook.save('DD test.xls')

def SDCARD(node,ct):

	os.system('adb shell "umount %s"'%node)
	os.system('adb shell "mount %s /sdcard"'%node)

	worksheet1.write(30,0,r'SDCARD')
	worksheet1.write(31,0,'4G-READ')
	worksheet1.write(32,0,'4G-WRITE')
	worksheet1.write(33,0,'1G-READ')
	worksheet1.write(34,0,'1G-WRITE')

	for j in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')
#跑4G
		EMMC4_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=2M count=2048 conv=fsync"'%j)
		EMMC4_w_result = EMMC4_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_w_result)
		emmc4_w = re.search('，\d+ MB/s',EMMC4_w_result).group().split('，')[1].split(' ')[0]
		print(emmc4_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC4_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=2M"'%j)
		EMMC4_r_result = EMMC4_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC4_r_result)
		emmc4_r = re.search('，\d+ MB/s',EMMC4_r_result).group().split('，')[1].split(' ')[0]
		print(emmc4_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%j)

		worksheet1.write(31,j+1,emmc4_r)
		worksheet1.write(32,j+1,emmc4_w)

#跑1G
	for i in range(ct):
		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_w = os.popen('adb shell "time dd if=/dev/zero of=/sdcard/test%d.dbf bs=512k count=2048 conv=fsync"'%i)
		EMMC1_w_result = EMMC1_w._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_w_result)
		emmc1_w = re.search('，\d+ MB/s',EMMC1_w_result).group().split('，')[1].split(' ')[0]
		print(emmc1_w)

		os.system('adb shell "echo 3 > /proc/sys/vm/drop_caches"')

		EMMC1_r = os.popen('adb shell "time dd if=/sdcard/test%d.dbf of=/dev/null bs=512k"'%i)
		EMMC1_r_result = EMMC1_r._stream.buffer.read().decode(encoding='utf-8',errors='ignore')
		print(EMMC1_r_result)
		emmc1_r = re.search('，\d+ MB/s',EMMC1_r_result).group().split('，')[1].split(' ')[0]
		print(emmc1_r)

		os.system('adb shell "rm /sdcard/test%d.dbf"'%i)

		worksheet1.write(33,i+1,emmc1_r)
		worksheet1.write(34,i+1,emmc1_w)

	workbook.save('DD test.xls')

def main_test(main_win):
#写当前运行频率
	CPU0 = os.popen('adb shell "cat /sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq"')
	cpu0 = CPU0.read()
	CPU4 = os.popen('adb shell "cat /sys/devices/system/cpu/cpufreq/policy4/cpuinfo_cur_freq"')
	cpu4 = CPU4.read()
	CPU6 = os.popen('adb shell "cat /sys/devices/system/cpu/cpufreq/policy6/cpuinfo_cur_freq"')
	cpu6 = CPU6.read()
	GPU = os.popen('adb shell "cat /sys/devices/platform/fb000000.gpu/devfreq/fb000000.gpu/cur_freq"')
	gpu = GPU.read()
	worksheet1.write(0,0,r'运行频率')
	worksheet1.write(1,0,'CPU0：')
	worksheet1.write(1,1,cpu0)
	worksheet1.write(2,0,'CPU4：')
	worksheet1.write(2,1,cpu4)
	worksheet1.write(3,0,'CPU6：')
	worksheet1.write(3,1,cpu6)
	worksheet1.write(4,0,'GPU：')
	worksheet1.write(4,1,gpu)
	workbook.save('DD test.xls')

	EMMC_flag = main_win.m_checkBox23.GetValue()
	USB20_flag = main_win.m_checkBox24.GetValue()
	USB30_flag = main_win.m_checkBox25.GetValue()
	SATASSD_flag = main_win.m_checkBox26.GetValue()
	PCIE_flag = main_win.m_checkBox27.GetValue()
	Sdcard_flag = main_win.m_checkBox28.GetValue()

	if EMMC_flag:
		TestEmmc(int(main_win.m_textCtrl32.GetValue()))
	if USB20_flag:
		USB20(main_win.m_textCtrl23.GetValue(),int(main_win.m_textCtrl33.GetValue()))
	if USB30_flag:
		USB30(main_win.m_textCtrl24.GetValue(),int(main_win.m_textCtrl34.GetValue()))
	if SATASSD_flag:
		SATASSD(main_win.m_textCtrl25.GetValue(),int(main_win.m_textCtrl35.GetValue()))
	if PCIE_flag:
		PCIESSD(main_win.m_textCtrl26.GetValue(),int(main_win.m_textCtrl36.GetValue()))
	if Sdcard_flag:
		SDCARD(main_win.m_textCtrl37.GetValue(),int(main_win.m_textCtrl38.GetValue()))

	messagebox.showinfo("提示","测试结束啦")


if __name__ == '__main__':

	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet1 = workbook.add_sheet('DD TEST')

	app = wx.App()
	main_win = main_window(None)
	main_win.Show()
	app.MainLoop()

	#SetPerformance()
	#TestEmmc()
	#USB20('/dev/sda1')
	#USB30('/dev/sdb1')
	#SATASSD('/dev/sda1')
	#PCIESSD('/dev/nvme0n1p1')