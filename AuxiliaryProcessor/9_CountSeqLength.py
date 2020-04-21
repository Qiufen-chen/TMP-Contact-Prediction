#!/usr/bin/env python
#coding:utf-8


import os

dir1 = "E:/730_Seq/"          #文件夹名称
if os.path.exists(dir1):
    print("dir exists")
else:
    print("no exists")
    
filenum = 0   
l0l1 = 0
l1l2 = 0
l2l3 = 0
l3l4 = 0
l4l5 = 0
l5l6 = 0
l6l7 = 0
l7l8 = 0
l8l9 = 0
l9ll = 0
l10l11 = 0
l11l12 = 0

for (root, dirs, files) in os.walk(dir1):  #列出windows目录下的所有文件和文件名
    for filename1 in files:
        filenum = filenum + 1

        # 如果文件有很多行，用该段代码
        # with open(os.path.join(root, filename1), 'r') as f1:
        #     num = 0
        #     for i in f1:
        #         num = num+1
        #     print(filename1, num)

        # 如果文件里只有一行，则用该段代码
        with open(os.path.join(root, filename1), 'r') as f1:
            line = f1.readline()
            num = len(line)
            print(filename1, num)


        if num > 0 and num < 100:
            l0l1 = l0l1 + 1
        if num >=100 and num < 200:
            l1l2 = l1l2 + 1
        if num >= 200 and num < 300:
            l2l3 = l2l3 + 1
        if num >= 300 and num < 400:
            l3l4 = l3l4 + 1
        if num >= 400 and num < 500:
            l4l5 = l4l5 + 1
        if num >= 500 and num < 600:
            l5l6 = l5l6 + 1
        if num >= 600 and num < 700:
            l6l7 = l6l7 + 1
        if num >= 700 and num < 800:
            l7l8 = l7l8 + 1
        if num >= 800 and num < 900:
            l8l9 = l8l9 + 1
        if num >= 900 and num < 1000:
            l9ll = l9ll + 1
        if num >= 1000 and num < 1100:
            l10l11 = l10l11 + 1
        if num >= 1100:
            l11l12 = l11l12 + 1
            
            
    print("********************************************************")
    print(filenum)
    print("num > 0 and num < 100: ", l0l1)
    print("num >=100 and num < 200: ", l1l2)
    print("num >=200 and num < 300: ", l2l3)
    print("num >=300 and num < 400: ", l3l4)
    print("num >=400 and num < 500: ", l4l5)
    print("num >=500 and num < 600: ", l5l6)
    print("num >=600 and num < 700: ", l6l7)
    print("num >=700 and num < 800: ", l7l8)
    print("num >=800 and num < 900: ", l8l9)
    print("num >=900 and num < 1000: ", l9ll)
    print("num >=1000 and num < 1100: ", l10l11)
    print("num >=1100: ", l11l12)
 
    
                   







