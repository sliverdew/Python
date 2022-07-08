#!/bin/sh
import os
import re
import subprocess
from threading import Timer
import xlwt

def get_ip():
	command_ip = 'adb shell ifconfig'
	with os.popen(command_ip, "r") as p:
		t = p.read()
	t1 = re.search('eth0.+\s{5}.+',t).group(0)
	t2 = re.search('inet addr:\d+\.\d+\.\d+\.\d+',t1).group(0)
	t3 = t2.split(':')[1]
	print(t1)
	print(t2)
	print(t3)
	return t3

def iperf_TCP_TX(host_ip,dut_ip,time):
	command_server = 'iperf -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'adb shell iperf -c %s -i 1 -w 1M -t %d' %(host_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('TCP_TX finish')
		os.system('adb shell killall iperf')

def iperf_TCP_TX_l64(host_ip,dut_ip,time):
	command_server = 'iperf -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'adb shell iperf -c %s -i 1 -w 1M -t %d -l 64' %(host_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('TCP_TX_l64 finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]

def iperf_TCP_RX(host_ip,dut_ip,time):
	command_server = 'adb shell iperf -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'iperf -c %s -i 1 -w 1M -t %d' %(dut_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('TCP_RX finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]

def iperf_TCP_RX_l64(host_ip,dut_ip,time):
	command_server = 'adb shell iperf -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'iperf -c %s -i 1 -w 1M -t %d -l 64' %(dut_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('TCP_RX_l64 finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]


def iperf_UDP_TX(host_ip,dut_ip,time):
	command_server = 'iperf -u -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'adb shell iperf -c %s -i 1 -t %d -u -b 100M' %(host_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('UDP_TX finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]

def iperf_UDP_TX_l64(host_ip,dut_ip,time):
	command_server = 'iperf -u -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'adb shell iperf -c %s -i 1 -t %d -u -b 100M -l 64' %(host_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('UDP_TX_l64 finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]

def iperf_UDP_RX(host_ip,dut_ip,time):
	command_server = 'adb shell iperf -u -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'iperf -c %s -i 1 -t %d -u -b 100M' %(dut_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('UDP_RX finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]

def iperf_UDP_RX_l64(host_ip,dut_ip,time):
	command_server = 'adb shell iperf -u -s'
	iperf_server = subprocess.Popen(command_server,shell=True,stdout=subprocess.PIPE)
	command_client = 'iperf -c %s -i 1 -t %d -u -b 100M -l 64' %(dut_ip,time)
	iperf_client = subprocess.Popen(command_client,shell=True,stdout=subprocess.PIPE)

	timer_server = Timer(60, iperf_server.kill)
	timer_client = Timer(60, iperf_client.kill)
	try:
		timer_server.start()
		timer_client.start()
		result = iperf_client.communicate()
	finally:
		timer_server.cancel()
		timer_client.cancel()
		print('UDP_RX finish')
		os.system('adb shell killall iperf')

	#print(result[0])
	r1 = re.search('0.0-(6|5).+ sec.+\s*.+',str(result[0]))
	print(r1)
	r2 = re.search('\d+\.*\d+ .bits/sec',r1.group(0))
	print(r2)
	return r2.group(0).split(' ')[0]

def ping(host_ip,dut_ip):
	command = 'adb shell ping -s 65507 -c 100 %s' %host_ip
	iperf_server = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	timer_ping = Timer(60,iperf_server.kill)

	try:
		timer_ping.start()
		result = iperf_server.communicate()
	finally:
		timer_ping.cancel()

	print(result[0])
	return str(result[0]).split(',')[-2].split(' ')[1]

if __name__ == '__main__':
	host_ip = input('请输入PC端IP：')
	time = 60
	TCP_receive = ''
	TCP_send = ''
	UDP_receive = ''
	UDP_send = ''
	TCP_l64_receive = ''
	TCP_l64_send = ''
	UDP_l64_receive = ''
	UDP_l64_send = ''
	PING = ''
	Q = ''
	flag = 0
	workbook = xlwt.Workbook(encoding = 'utf-8')
	worksheet = workbook.add_sheet('Summary')
	while True:
		Q = input(u"请输入当前网线型号，或输入q退出:")
		if Q.lower() == 'q':
			os._exit()
		else :
			flag += 1
			worksheet.write_merge(0,0,2*flag-2,2*flag-1,Q)
			dut_ip = get_ip()
			if dut_ip == ' ':
				print(u'未能获取设备ip，请检查')
				worksheet.write(1,2*flag-1,'fail')
				workbook.save('eth0_test.xls')
				continue
			else:
				worksheet.write(1,2*flag-1,'ok')
				TCP_send = iperf_TCP_TX(host_ip,dut_ip,time)
				TCP_l64_send = iperf_TCP_TX_l64(host_ip,dut_ip,time)
				TCP_receive = iperf_TCP_RX(host_ip,dut_ip,time)
				TCP_l64_receive = iperf_TCP_RX_l64(host_ip,dut_ip,time)
				UDP_send = iperf_UDP_TX(host_ip,dut_ip,time)
				UDP_l64_send = iperf_UDP_TX_l64(host_ip,dut_ip,time)
				UDP_receive = iperf_UDP_RX(host_ip,dut_ip,time)
				UDP_l64_receive = iperf_UDP_RX_l64(host_ip,dut_ip,time)
				PING = ping(host_ip,dut_ip)
				print(u'这是第 %d 次执行,TCP接收：%s,TCP_l64接收：%s,TCP发送：%s,TCP_l64发送：%s,UDP接收：%s,UDP_l64接收：%s,UDP发送：%s,UDP_l64发送：%s,丢包率：%s' %(flag,TCP_receive,TCP_l64_receive,TCP_send,TCP_l64_send,UDP_receive,UDP_l64_receive,UDP_send,UDP_l64_send,PING))
				worksheet.write(2,2*flag-1,TCP_send)
				worksheet.write(3,2*flag-1,TCP_receive)
				worksheet.write(4,2*flag-1,TCP_l64_send)
				worksheet.write(5,2*flag-1,TCP_l64_receive)
				worksheet.write(6,2*flag-1,UDP_send)
				worksheet.write(7,2*flag-1,UDP_receive)
				worksheet.write(8,2*flag-1,UDP_l64_send)
				worksheet.write(9,2*flag-1,UDP_l64_receive)
				worksheet.write(10,2*flag-1,PING)

			workbook.save(r'.\eth0_test.xls')
