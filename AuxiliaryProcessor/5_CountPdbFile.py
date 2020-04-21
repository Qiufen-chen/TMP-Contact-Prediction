import os

def readFile(rootdir):
    """
    purpose:列出文件夹下所有的目录与文件，并计数
    :param rootdir:
    :return:
    """
    count = 0
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            print(path)
            count = count + 1



        # 如果是二级目录，则用该段代码
        # files_list = os.listdir(path)
        # for j in range(0, len(files_list)):
        #     files_path = os.path.join(path, files_list[j])
        #     if os.path.isfile(files_path):
        #         print(files_path)
        #         count = count + 1

    return count

if __name__ == '__main__':
    # 列表所在目录
    root_path = 'E:/730_Matrix/1000_Matrix/'
    num_result = readFile(root_path)
    print("1000_Matrix文件夹的总文件数为：" + str(num_result))
