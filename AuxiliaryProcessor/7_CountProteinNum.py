"""
purpose: Count how many proteins are left after the redundancy is removed
author: qiufen-chen
date: 2020/03/17
"""

import os
import re

def count_seq_num(file_path):
    """
    purpose: 打开要操作的文件，一行一行进行读取，并计数
    :param file_path:
    :return:
    """
    with open(file_path, encoding='utf-8') as file_obj:
        lines = file_obj.readlines()

        count = 0
        list_proteins = []
        for line in lines:
            if line[0] == '>':
                col = re.split(">|_", line)
                if col[1] not in list_proteins:
                    list_proteins.append(col[1])
                    count = count + 1

        #print(list_proteins)
        # 将行列表按列输出
        for i in range(0,len(list_proteins)):
            print(list_proteins[i])

        return count

# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root_file = 'E:\\Contact_Prediction_Projects\\统计\\Fasta\\Result.fas'
    num = count_seq_num(root_file)

    print(num)