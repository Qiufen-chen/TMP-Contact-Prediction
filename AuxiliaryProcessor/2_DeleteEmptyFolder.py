"""
purpose: Delete empty folders
author: qiufen-chen
date: 2020/0306
"""

import os
def del_emp_dir(path):
    for (root, dirs, files) in os.walk(path):
        for item in dirs:
            dir = os.path.join(root, item)
            try:
                os.rmdir(dir)  #os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
                print(dir)
            except Exception as e:
                print('Exception',e)

if __name__ == '__main__':
    dir = 'E:\\pdbtm.enzim.hu\\data\\database\\'
    del_emp_dir(dir)