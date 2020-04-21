"""
两个txt文件词汇，用换行符分隔。可以用代码将要处理的文件去掉另一个文件所包含的重复内容。
"""
import csv
import re
import io

 #创建字典
def dictlist(filepath):
    dicts = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return dicts

dicts = dictlist('C:/Users/KerryChen/OneDrive/桌面/3D_File/100.txt')  # 这里去重词的路径
f2 = open("C:/Users/KerryChen/OneDrive/桌面/3D_File/635.txt","a+",encoding='utf-8') # 这里为写入的新文件
f = open("C:/Users/KerryChen/OneDrive/桌面/3D_File/735.txt","r+",encoding='utf-8') # 这里为要处理的文件
for line in f:
    if line.strip() not in dicts:
        f2.write(line.strip()+"\n")
f.close()
f2.close()