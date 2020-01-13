#/bin/sh
import os
A = '00003559'
A1 = 0 #加法前数字长度
B = ''
A1 = len(str(int(A)+6))
B = A[0:len(A)-A1] + str((int(A)+6)) #叠加后恢复原始数字
print(B)
C = 'G:\FaceCapture\RK\20191029\C\C0001\C0001-35\rgb\00003559.jpg'
print(C[-12:-4:1])
