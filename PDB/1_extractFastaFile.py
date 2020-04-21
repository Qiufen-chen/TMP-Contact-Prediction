"""
purpose：创建一个标准fasta文件，开头以 ‘>id_链’ 的方式，下一行是序列
author： qiufen-chen
date： 2020/03/09
modification: 2020/03/13
"""

import PDBParser
import os, datetime,textwrap

start = datetime.datetime.now()

# ----------------------------------------------------------------------------------------------
def func():
    pass

# ----------------------------------------------------------------------------------------------
def get_list_chain(result_all):
    """
    purpose: 获取list_chain
    :param result_all:
    :return: list_chain
    """
    for key, value in result_all.items():
        list_chain = []
        if key == 'ATOM':
            for line_1 in value:
                if line_1['chainID'] not in list_chain:
                    list_chain.append(line_1['chainID'])
            return list_chain

# ----------------------------------------------------------------------------------------------
def get_header(result_all):
    """
    purpose: 获取fasta的头信息，取header的 idCode 和 classification字段
    :param result_all:
    :return: header
    """

    for key, value in result_all.items():
        if key == 'HEADER':
            for line in value:
                header = '>' + line['idCode']
    return header

# ----------------------------------------------------------------------------------------------
def get_atom_list(result_all):
    """
    purpose:获取去重后的氨基酸序列
    :param result_all:
    :return: list_atom
    """
    for key, value in result_all.items():
        list_atom = []
        if key == "ATOM":
            for line in value:

                # 去重，需要判断是否名称，链，序号都相同，只要有一个不同就追加
                atomInfor = [line['resName'], line['chainID'], line['resSeq']]
                if atomInfor not in list_atom:
                    list_atom.append(atomInfor)
            return list_atom

# ----------------------------------------------------------------------------------------------
def get_atom_seq(header, list_chain, list_atom):
    """
    purpose:根据找到的位点，提取其所在链的全部氨基酸，并将其转换成fasta格式，输出文件
    :param result_all:
    :return:
    """

    list_resName = ['GLY', 'ALA', 'VAL', 'LEU', 'ILE', 'PHE', 'TRP', 'TYR', 'ASP', 'ASN', \
                    'GLU', 'LYS', 'GLN', 'MET', 'SER', 'THR', 'CYS', 'PRO', 'HIS', 'ARG']
    list_abbreviation = ['G', 'A', 'V', 'L', 'I', 'F', 'W', 'Y', 'D', 'N', \
                         'E', 'K', 'Q', 'M', 'S', 'T', 'C', 'P', 'H', 'R']

    for chain in list_chain:
        chain_id = ''
        fasta_stru = ''
        for item in list_atom:
            resName = item[0]
            chainID = item[1]
            resSeq = item[2]
            if chainID == chain:
                if resName in list_resName:
                    for i in range(len(list_resName)):
                        if resName == list_resName[i]:
                            resName = list_abbreviation[i]
                            fasta_stru = fasta_stru + resName
                    chain_id = chain

        if (len(fasta_stru) >= 30 and str(chain_id) != '' ):
            print(header + '_' + chain_id + ' ' + str(len(fasta_stru)))
            seqInfor = header + '_' + chain_id + '\n' + fasta_stru


            savefilepath = "E:\\ContactPredictionProject\\3_Remain_Data\\"
            dirname = 'Fasta'
            new_Filepath = savefilepath + "/" + str(dirname) + "/"
            mkdir(new_Filepath)
            new_filename = 'RemainSeqInfo' + ".fasta"

            with open(new_Filepath + new_filename, 'a+') as file_object:
                file_object.writelines(seqInfor + '\n' + '\n')


        else:
            pass


# ----------------------------------------------------------------------------------------------
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


# ----------------------------------------------------------------------------------------------
def save_file(seqInfor):
    """
    purpose: 保存文件
    :param seqInfor:
    :return:
    """

    savefilepath = "E:\\ContactPredictionProject\\3_Remain_Data\\"
    dirname = 'Fasta'
    new_Filepath = savefilepath + "/" + str(dirname) + "/"
    mkdir(new_Filepath)
    new_filename = 'AtomSeqInfo_2' + ".fasta"
    count = 0
    with open(new_Filepath + new_filename, 'a+') as file_object:
        file_object.writelines(seqInfor + '\n')
        #global count
        count = count + 1
    return count


# ----------------------------------------------------------------------------------------------
def print_stru(header,fasta_stru):
    print(header)
    print(textwrap.fill(fasta_stru, width=60))


# ----------------------------------------------------------------------------------------------
def readFile(rootdir):
    """
    purpose:列出文件夹下所有的目录与文件，并解析
    :param rootdir:
    :return:
    """

    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        files_list = os.listdir(path)
        for j in range(0, len(files_list)):
            files_path = os.path.join(path, files_list[j])
            if os.path.isfile(files_path):

                ppb = PDBParser.ParserBase(func)
                result = ppb.parser(files_path, target='ALL')
                header_get = get_header(result)
                chain_get = get_list_chain(result)

                atom_get = get_atom_list(result)

                get_atom_seq(header_get, chain_get, atom_get)
                #count_num = save_file(sequence)
                #print(count)


# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    rootdir = 'E:\\ContactPredictionProject\\Total_Remain_Data\\'
    #rootdir = 'C:\\Users\\qiufen\\Desktop\\待删除文件\\'
    readFile(rootdir)
    end = datetime.datetime.now()
    print("alltime = ", end="")
    print(end - start)