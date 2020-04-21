# -*- coding: utf-8 -*-
"""
    File Name：files_dealer
    Description: 1.pdb-xml to three-dim_files
    Author: Gong Yingli
    Time：Thu Sep 26 12:44:04 2019
    "
    Author:qiufen-chen
    Modification：2020/04/15
    "
"""


import os
import numpy as np
from xml.etree.ElementTree import parse

########################################################################
class pdb_xml_dealer(object):
    
    def __init__(self):
        self.alpha = []
        self.residue = {'ALA': 'A', 'ARG': 'R', 'ASN': 'N', 'ASP': 'D', 'CYS': 'C', 'GLN': 'Q', 'GLU': 'E',
                        'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K', 'MET': 'M', 'PHE': 'F',
                        'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W', 'TYR': 'Y', 'VAL': 'V'}
        
   
    def pdb_xml_dealer(self,fileName):
        """
        description:
        :param fileName: 一行一个的pdbid文件
        :return:
        """
        with open(fileName) as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                pdbid = line
                if(os.path.exists('E:/pdbtm.enzim.hu/XML_file/' + pdbid + '.xml') == False):
                    print(pdbid + '.xml', 'not found!')
                    continue
                if(os.path.exists('E:/ContactPredictionProject/Total_NonRedundant_Data/database/' + pdbid + '.pdb') == False):
                    print(pdbid + '.pdb', 'not found!')
                    continue
                parser = parse('E:/pdbtm.enzim.hu/XML_file/' + pdbid + '.xml')
                root = parser.getroot()            
                if root.findall('{http://pdbtm.enzim.hu}CHAIN') == []:
                    print(pdbid, 'no chain!')
                    continue
                #find the alpha chain
                for item in root.findall('{http://pdbtm.enzim.hu}CHAIN'):
                    if item.get('TYPE') != 'alpha':
                        continue
                    chainId = item.get('CHAINID')
                    self.alpha.append(pdbid+'_'+chainId)
                    
                    #from the pdb files to extract residues and its' nos
                    resName = []
                    resNo = []
                    x_1 = []
                    y_1 = []
                    z_1 = []
                    with open('E:/ContactPredictionProject/Total_NonRedundant_Data/database/' + pdbid + '.pdb') as pdb_file:
                        model = 0
                        flag_resName = ''
                        flag_resNo = ''
                        flag_x = ''
                        flag_y = ''
                        flag_z = ''
                        pdbline = pdb_file.readline()
                        while pdbline:
                            if pdbline[:6] == 'ENDMDL' and model == 1:
                                break
                            #if pdbline[:6] != 'ATOM  ' and pdbline[:6] != 'HETATM':
                            if pdbline[:6] != 'ATOM  ':
                                pdbline = pdb_file.readline()
                                continue
                            if pdbline[21] != chainId or pdbline[12:16] != ' CA ':
                                pdbline = pdb_file.readline()
                                continue
                            model = 1
                            if pdbline[17:20] in self.residue.keys():
                                res_name = self.residue[pdbline[17:20]]
                            else:
                                res_name = 'X'
                            res_no = pdbline[22:26].strip()
                            x = pdbline[31:38].strip()
                            y = pdbline[39:46].strip()
                            z = pdbline[47:54].strip()
                            if flag_resName != res_name or flag_resNo != res_no:
                                resName.append(res_name)
                                resNo.append(res_no)
                                x_1.append(x)
                                y_1.append(y)
                                z_1.append(z)


                            flag_resName = res_name
                            flag_resNo = res_no
                            flag_x = x
                            flag_y = y
                            flag_z = z



                            pdbline = pdb_file.readline()
                    
                    #from the xml files to extract topo labels
                    dic = {}
                    for reg in item.findall('{http://pdbtm.enzim.hu}REGION'):
                        start = reg.get('pdb_beg')
                        end = reg.get('pdb_end')
                        flag = 0
                        for index in resNo:
                            if index == start:
                                flag = 1
                            if flag == 1:
                                dic[index] = reg.get('type')
                            if index == end:
                                break

                    #merge the sequences and the labels  
                    wstr_list = []
                    for index in range(0,len(resName)):
                        if resNo[index] in dic.keys():
                            label = dic[resNo[index]]
                        else:
                            label = '$'
                        wstr_list.append(str(resName[index]).ljust(5) + str(label).ljust(5) + str(resNo[index]).ljust(10) + str(x_1[index]).ljust(10) + str(y_1[index]).ljust(10) + str(z_1[index]).ljust(10))
                    #print(pdbid+'_'+chainId,wstr_list)
                    with open('E:/pdbtm.enzim.hu/3D_file/11/' + pdbid+'_'+chainId + '.txt','w+') as three_file:
                        for three_line in wstr_list:
                            three_file.write(three_line)
                            three_file.write('\n')
                          
        #self.record()
                
    def record(self):
        #with open('alpha_list.txt','w') as file:
        with open('') as file:
            for chain in self.alpha:
                file.write(chain + '\n')

if __name__ == '__main__':
    # 3D_file = 'E:/pdbtm.enzim.hu/3D_file/'
    # xml_file = 'E:/pdbtm.enzim.hu/XML_file/'
    # pdb_file = 'E:/ContactPredictionProject/Total_NonRedundant_Data/database/'
    id_file = 'E:/ContactPredictionProject/2_non-RedundantAlphaDAta/2_Non-redundantAlphaList.txt'
    dealer = pdb_xml_dealer()
    dealer.pdb_xml_dealer(id_file)
