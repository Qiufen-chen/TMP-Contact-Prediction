"""
purpose: 批量删除某文件夹及其子文件夹下的.gz文件，可参照下实现批量删除别的类型的文件。
author:qiufen-chen
date:2020/03/09
"""
import os

# ------------------------------------------------------------------------------------------
def readFiles(file_dir):
    """
    purpose: 读取文件
    :param file_dir:
    :return:
    """
    for root, dirs, files in os.walk(file_dir):
        return files, dirs, root

# ------------------------------------------------------------------------------------------
def deleteFiles(files, dirs, root):
    """
    purpose: 删除文件
    :param files:
    :param dirs:
    :param root:
    :return:
    """
    for file in files:
        # 以.gz结尾的数据
        if file.endswith('.gz'):
            print('Delete:', file)
            os.remove(os.path.join(root, file))

    for dir in dirs:
        fi, di, ro = readFiles(root + "\\" + dir)
        deleteFiles(fi, di, ro)

# ------------------------------------------------------------------------------------------
if __name__ == '__main__':
    files, dirs, root = readFiles(u"E:\\ContactPredictionProject\\data\\总文件")
    deleteFiles(files, dirs, root)
