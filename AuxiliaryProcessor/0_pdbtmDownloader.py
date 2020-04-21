"""
1.规则：
下载pdb文件：'wget http://pdbtm.enzim.hu/data/database/' + PDB_ID[1:3] + '/' + PDB_ID[0:4] + '.pdb.gz'
下载xml文件：'wget http://pdbtm.enzim.hu/data/database/' + PDB_ID[1:3] + '/' + PDB_ID[0:4] + '.xml'

例如：
6eu6的pdb文件: wget http: // pdbtm.enzim.hu / data / database / eu / 6
eu6.pdb.gz
5l25的xml文件: wget http: // pdbtm.enzim.hu / data / database / l2 / 5l
25.xml

2.批量下载
以下是python批量下载的代码：
"""

import os


class xmltmDownloader(object):

    def __init__(self):
        pass

    def main(self, ID_list_file):
        f = open(ID_list_file, "r")
        line = f.readline()
        while line:
            url = "http://pdbtm.enzim.hu/data/database/" + str(line[1:3]) + "/" + str(line[0:4]) + ".xml"
            os.system("wget" + str(url))
            os.system("gzip -d " + str(line[0:4]) + ".xml")
            line = f.readline()


if __name__ == "__main__":
    ID_list_file = './TM_Num_list.txt'
    downloader = xmltmDownloader()
    downloader.main(ID_list_file)
