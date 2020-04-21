import PDBParser
import os

# ----------------------------------------------------------------------------------------------
def func():
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


def get_dictlist(filepath):
    """
    purpose：创建字典列表
    :param filepath:
    :return: 列表
    """
    dict_chain = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return dict_chain

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
                header = line['idCode']
    return header

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

def get_atom_CA(result_all,dict_header, list_chain, dict_chain):
    """
    purpose:根据已知的目标链，提取其链上氨基酸CA原子坐标，每一条链保存进一个文件里
    :param header:
    :param list_chain:
    :param list_atom:
    :return:
    """
    id_list = []
    for chain in list_chain:
        chain_id = chain
        chainID = dict_header + '_' + chain_id
        id_list.append(chainID)

    for key, value in result_all.items():
        if key == "ATOM":
            for line in value:
                if line['name'] == 'CA':
                    for i in range(len(id_list)):

                        if id_list[i] in dict_chain and ((str(id_list[i]).split('_')[-1]) == line['chainID']):
                            #atomInfo = str(line['resName']) + '  '  + str(line['x']) + '  ' + str(line['y']) + '  ' +str(line['z'])
                            atomInfo = str(line['resName']).ljust(5)  + str(line['x']).ljust(10)  + str(line['y']).ljust(10) + str(line['z']).ljust(10)

                            # 左对齐打印
                            print('{:<9}\t'.format(atomInfo), end='\n')
                            #print(atomInfo)


                            savefilepath = "C:\\Users\\KerryChen\\OneDrive\\桌面\\11\\"
                            dirname = 'ATOM'
                            new_Filepath = savefilepath + "/" + str(dirname) + "/"
                            mkdir(new_Filepath)
                            new_filename = str(id_list[i]) + ".txt"

                            with open(new_Filepath + new_filename, 'a+') as file_object:
                                file_object.writelines(str(atomInfo) + '\n')

def readFile(rootdir, file_path):
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
                purpose_id = get_dictlist(file_path)
                header_id = get_header(result)
                chain_id = get_list_chain(result)
                get_atom_CA(result, header_id, chain_id, purpose_id)






if __name__ == "__main__":
    file1_path = 'C:/Users/KerryChen/OneDrive/桌面/11/'
    file2_path = 'E:\\ContactPredictionProject\\project\\AuxiliaryProcessor\\TM_Num_list.txt'
    readFile(file1_path,file2_path)







