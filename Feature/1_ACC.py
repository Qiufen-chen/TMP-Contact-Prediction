"""
purpose: 提取氨基酸组成——ACC
author：qiufen-chen
date：2020/04/15
"""


from Bio import SeqIO
import numpy as np

def radio(char,seq):
    seq_length = len(seq)
    return seq.count(char)/seq_length

def ACC(fasta_path,outpath):
    for record in SeqIO.parse(fasta_path, "fasta"):
        ID = str(record.name)
        seq =str(record.seq)
        ID =ID.split('>')[0]
        list1 = ('G','A','V','L','I','P','F','W','M','Y','S','T','C','N','Q','D','E','K','R','H')
        Amino_radio = []
        for i in list1:
            Amino_radio.append(round(radio(i, seq), 3))
        np.save(outpath+ID+".npy", Amino_radio)

if __name__ == '__main__':
    fasta_path = 'E:/730_Fasta/2340_SeqInfo.fasta'
    outpath = 'E:/ContactPredictionProject/project/Feature/ACC_Feature/2340_ACC/'
    ACC(fasta_path, outpath)