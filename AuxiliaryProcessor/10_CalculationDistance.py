#!/usr/bin/env python
#coding:utf-8


import os
import numpy as np
import math

def make_dir(path):
    """
    purpose: Created path folder
    :param path:
    :return:
    """
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + " Created folder sucessful!")
        return True
    else:
        print("This path is exist！")
        return False


def get_matrix(dir1,dir2):
     file_num = 0
     for (root, dirs, files) in os.walk(dir1):  #列出windows目录下的所有文件和文件名
          for filename1 in files:
               file_num = file_num + 1
               with open(os.path.join(root, filename1), 'r') as f1:
                    #line = f1.readline()
                    num = 0
                    for i in f1:
                         num = num + 1
                    print(num)   # 计算多少行


               file = open(os.path.join(root) + '/' + filename1)

               for (root2, dirs, files) in os.walk(dir2):
                    #print(os.path.join(root2) + '/' + filename1)
                    #file = open(os.path.join(root2) + '/' + filename1,'w')
                    if num > 1000 and num <= 2340:
                         initial_matrix = np.zeros((2340,2340))
                         str1 = [0 for i in range(num)]
                         k = 0
                         for i in file:
                              #print(i[3:11])
                              str1[k] = i[0:48]
                              k = k + 1
                         for i in range(0, num):
                              #print(k)
                              x_1 = float(str1[i][20:28])
                              y_1 = float(str1[i][30:38])
                              z_1 = float(str1[i][40:48])
                              # x_1 = float((str1[i][5:13]).strip(''))
                              # y_1 = float((str1[i][15:23]).strip(''))
                              # z_1 = float((str1[i][25:33]).strip(''))
                              for j in range(0, num):
                                   #print(j)
                                   x_2 = float(str1[j][20:28])
                                   y_2 = float(str1[j][30:38])
                                   z_2 = float(str1[j][40:48])
                                   # x_2 = float((str1[i][5:13]).strip(''))
                                   # y_2 = float((str1[i][15:23]).strip(''))
                                   # z_2 = float((str1[i][25:33]).strip(''))
                                   # 计算氨基酸之间的欧氏距离
                                   ans = math.sqrt(pow(x_1-x_2,2) + pow(y_1-y_2,2) + pow(z_1-z_2,2))
                                   if ans <= 8:
                                        initial_matrix[i][j] = 1
                         print(initial_matrix)
                         np.save(os.path.join(root2) + '/' + str(filename1).split('.')[0], initial_matrix)

# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
     file_path1 = 'E:/735_ATOM/727/'
     # file_path1 = 'E:/735_ATOM/3_格式特殊/12/'
     file_path2 = 'E:/730_Matrix/2340_Matrix/'
     make_dir(file_path1)
     make_dir(file_path2)
     get_matrix(file_path1,file_path2)











               
                   



