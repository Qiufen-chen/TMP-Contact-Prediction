"""
purpose: Count the number of sequences after using the CD HIT tool to eliminate redundancy
author: qiufen-chen
date: 2020/03/16
"""

import os

def count_seq_num(file_path):
    """
    purpose: 打开要操作的文件，一行一行进行读取，并计数
    :param file_path:
    :return:
    """
    with open(file_path, encoding='utf-8') as file_obj:
        lines = file_obj.readlines()

        count = 0
        for line in lines:
            if line[0] == '>':
                print(line)
                count = count + 1

        return count

# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    root_file = 'E:/730_Fasta/2340_SeqInfo.fasta'
    num = count_seq_num(root_file)

    print(num)

