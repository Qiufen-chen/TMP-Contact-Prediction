"""
purpose: 从ATOM文件里提取fasta序列
author：qiufen-chen
date：2020/04/16
"""
import os

# ---------------------------------------------------------------------
def mkdir(path):
    """
    purpose: Created uncompress path folder
    :param path:
    :return:
    """
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + " Created folder sucessful!")
        return True
    else:
        #print("This path is exist！")
        return False

# ---------------------------------------------------------------------
def getSeq(file_path):
    """
    purpose:得到fasta的序列，放置一行，中间无空格
    :param file_path: 文件的路径
    :return: str_fasta
    """
    with open(file_path) as file:
        str_fasta = ''
        lines = file.readlines()  # 注意readline和readlines的区别
        for line in lines:
            str_fasta = str_fasta + line[0:3].strip()
        return str_fasta

# ---------------------------------------------------------------------
def getHeader(file_path):
    """
    purpose:得到文件名作为fasta文件的头
    :param file_path:文件的路径
    :return:返回文件名
    """
    with open(file_path) as file:
        (filepath, tempfilename) = os.path.split(file_path)
        (filename, extension) = os.path.splitext(tempfilename)
    return filename

# ---------------------------------------------------------------------
def getFasta(header, sequence):
    """
    purpose:得到完整的fasta序列——example:
    >1kyk_A
    GNVVDLAVGVIIGAAFGKIVSSLVADIIMPVMHYGVFIQNVFDFLIVAFAIFMAI
    :param header:
    :param sequence:
    :return:无返回值
    """
    seqInfor = '>' + header + '\n' + sequence
    savefilepath = "E:\\734_Fasta\\"
    dirname = 'Fasta'
    new_Filepath = savefilepath + "/" + str(dirname) + "/"
    mkdir(new_Filepath)
    new_filename = '734_SeqInfo' + ".fasta"

    with open(new_Filepath + new_filename, 'a+') as file_object:
        file_object.writelines(seqInfor + '\n' + '\n')

# ---------------------------------------------------------------------
def readFile(rootdir):
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            header = getHeader(path)
            sequence = getSeq(path)
            getFasta(header, sequence)

# ---------------------------------------------------------------------
if __name__ == "__main__":
    dir = 'E:\\735_ATOM\\731\\'
    readFile(dir)