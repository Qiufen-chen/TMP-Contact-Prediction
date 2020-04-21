"""
purpose:删除不在列表里的文件
author: qiufen-chen
date:2020/03/25
"""
import os

def readTxt(file_path):
    list_source = []
    file = open(file_path, 'r')
    for line in file.readlines():
        # 使用strip()函数去掉每行结束的\n
        list_source.append(line.strip('\n'))
    file.close()
    return list_source

def readFile(rootdir, result_list):

    count = 0
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        file_list = os.listdir(path)
        for j in range(0, len(file_list)):
            file_path = os.path.join(path, file_list[j])

            # 如果文件的完整路径为：D:/test/test.py
            # filepath为文件的目录,即D:/test
            # filename为文件的名字,即test
            # extension为文件的扩展名,即.py

            (filepath, tempfilename) = os.path.split(file_path)
            (filename, extension) = os.path.splitext(tempfilename)
            if filename not in result_list:
                os.remove(file_path)
                print(file_path + "删除成功！")
                count = count + 1
    print(count)



if __name__ == '__main__':
    # 列表所在目录
    root1_path = 'E:/730_Matrix/2340_Matrix_list.txt'
    # 原始数据所在目录
    root2_path = 'E:/730_Sequence/'
    list_result = readTxt(root1_path)
    readFile(root2_path, list_result)



