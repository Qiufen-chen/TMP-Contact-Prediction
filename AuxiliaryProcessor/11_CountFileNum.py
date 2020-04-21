import os
def count_file_num(dir_path):
    file_num = 0
    for (root, dirs, files) in os.walk(dir_path):  #列出windows目录下的所有文件和文件名
        for file_name in files:
           file_num = file_num + 1
           print(str(file_name).split('.')[0])   # 取文件名，不要后缀
        print("2400_matrix文件夹里的文件个数为：", file_num)


# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    file_path1 = 'E:\\pdbtm.enzim.hu\ATOM\\2400_matrix\\'
    count_file_num(file_path1)
    print("*************************************************")


