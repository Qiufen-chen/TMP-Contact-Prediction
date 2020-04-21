#!/usr/bin/env python
#coding:utf-8
"""
purpose:提取序列,一个文件放置一行
author：qiufen-chen
date：2020/04/17
"""

import os
def makeDir(dir):

    if os.path.exists(dir):
        print("文件夹已存在！")
    else:
        os.mkdir(dir)
        print("文件夹创建成功！")

# 不用字符替换
# lib1=('G','A','V','L','I','P','F','Y','W','S','T','C','M','N','Q','D','E','K','R','H')
# lib2=("GLY","ALA","VAL","LEU","ILE","PRO","PHE","TYR","TRP","SER","THR","CYS","MET","ASN","GLN","ASP","GLU","LYS","ARG","HIS")
  
def getSeq(dir1, dir2):
    file_num = 0
    for (root, dirs, files) in os.walk(dir1):  #列出windows目录下的所有文件和文件名
        for file_name in files:
            file_num = file_num + 1
            print(file_name)
            #print(os.path.join(root) + '/' + file_name)

            file_1 = open(os.path.join(root) + '/' + file_name)
            # line = file_1.readline()  # 注意readline和readlines的区别
            # print(line)
            for (root2, dirs, files) in os.walk(dir2):
                #print(os.path.join(root2) + '/' + filename1)
                file_2 = open(os.path.join(root2) + '/' + file_name, 'w')
                for char in file_1:
                    p1 = char[0:3].strip()
                    #print(p1)
                    file_2.write(p1)

                    # for j in range(0, len(lib2)):
                    #     if(p1==lib2[j]):
                    #         print(lib1[j])
                    #         file_2.write(lib1[j])
                    #         break
# ---------------------------------------------------------------------
if __name__ == "__main__":
    dir1 = 'E:\\735_ATOM\\731\\'
    makeDir(dir1)
    dir2 = 'E:/734_Seq/375'
    makeDir(dir2)
    getSeq(dir1, dir2)

            









#################################################################################
#!/usr/bin/env python
#coding:utf-8

#f = open("E:/start/5.pdb")
#file = open('E:/start/5eeee.pdb','w')
#lib3=("GLY","ALA","VAL","LEU","ILE","PRO","PHE","TYR","TRP","SER","THR","CYS","MET","ASN","GLN","ASP","GLU","LYS","ARG","HIS")  
#lib1=('G','A','V','L','I','P','F','Y','W','S','T','C','M','N','Q','D','E','K','R','H')  
#for i in f:
    ##file.write(i[5:8]+' ')
    #for j in range(len(lib3)):
        #if(lib3[j]==i[5:8]):  
            #file.write(lib1[j]+'\n') 
            #print (format(str,lib1[j])) 
    #break      
  
#f.close()
#file.close()

############################################################
#f = open("E:/start/pdbb/1q8h.pdb", "r")  
#file= open('E:/start/5eeee.pdb', 'w')  
#lib1=('G','A','V','L','I','P','F','Y','W','S','T','C','M','N','Q','D','E','K','R','H')  
#lib2=("GLY","ALA","VAL","LEU","ILE","PRO","PHE","TYR","TRP","SER","THR","CYS","MET","ASN","GLN","ASP","GLU","LYS","ARG","HIS")  
  
#for i in f:    
    #p1 = i[0:3]
    #print(p1)
    #for j in range(len(lib2)):  
        #if(p1==lib2[j]):  
            #print(lib1[j])
            #file.write(lib1[j])
            #break     
#f.close()  
#file.close()
################################################################################################