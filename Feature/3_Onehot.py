#!/usr/bin/env python
#coding:utf-8
"""
purpose：提取onehot编码
"""


import os
import numpy as np
import math
from numpy import argmax

dir1 = "E:/730_Sequence/total_Sequence/"          #文件夹名称
if os.path.exists(dir1):
    print("dir exists")
else:
    print("no exists")

dir2 = "E:/ContactPredictionProject/project/Feature/Onehot_Feature/total_onehot/"          #文件夹名称
if os.path.exists(dir2):
    print("dir exists")
else:
    print("no exists")

file_num = 0
for (root, dirs, files) in os.walk(dir1):  #列出windows目录下的所有文件和文件名
    for file_name in files:
        file_num = file_num + 1

        with open(os.path.join(root, file_name), 'r') as f1:
            line = f1.readline()  
            num = len(line)
            print(num)
            print(line)
        
        
        
        for (root2, dirs, files) in os.walk(dir2):
            a = np.zeros((2340, 21))
        
            # define universe of possible input values
            alphabet = 'ARDCQEHIGNLKMFPSTWYV'
            # define a mapping of chars to integers
            char_to_int = dict((c, i) for i, c in enumerate(alphabet))
            int_to_char = dict((i, c) for i, c in enumerate(alphabet))
                
            # integer encode input data
            integer_encoded = [char_to_int[char] for char in line]
            print(integer_encoded) 
            
            
            numb = 0
            for i in integer_encoded:
                #print(i)
                a[numb][i] = 1
                numb = numb + 1
            print(num)

            for j in range(numb,2340):
                a[j][20] = 1
            print(a)

            #print(a)
            np.save(os.path.join(root2) + '/' + file_name, a)





########################################################

            #from numpy import argmax
            
            ## define input string
            #data = 'hello world'
            #print(data)
            ## define universe of possible input values
            #alphabet = 'abcdefghijklmnopqrstuvwxyz '
            ## define a mapping of chars to integers
            #char_to_int = dict((c, i) for i, c in enumerate(alphabet))
            #int_to_char = dict((i, c) for i, c in enumerate(alphabet))
            
            ## integer encode input data
            #integer_encoded = [char_to_int[char] for char in data]
            #print(integer_encoded)
            
            ## one hot encode
            #onehot_encoded = list()
            
            #for value in integer_encoded:
                #letter = [0 for _ in range(len(alphabet))]
                #letter[value] = 1
                #onehot_encoded.append(letter)
                #print(onehot_encoded)
                ## invert encoding
                #inverted = int_to_char[argmax(onehot_encoded[0])]
                #print(inverted)
