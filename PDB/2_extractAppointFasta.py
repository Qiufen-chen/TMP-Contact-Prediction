"""
author: qiufen-chen
date: 2020/04/03
Description:需要用到fasta文件和ID的list文件。
            所要提取的序列的ID需要提前写进一个文件中，每行一个。
"""
def main():
    outf = open('E:/730_Fasta/1000_SeqInfo.fasta', 'w')
    dict = {}
    with open('E:/730_Fasta/Total_SeqInfo.fasta', 'r') as fastaf:
        for line in fastaf:
            if line.startswith('>'):
                #print(line)
                name = line.strip().split()[0][1:]
                dict[name] = ''
            else:
                dict[name] += line.replace('\n', '')

    count = 0
    with open('E:/730_Matrix/1000_Matrix_list.txt', 'r') as listf:
        for row in listf:
            row = row.strip()
            for key in dict.keys():

                if key == row:
                    print(key)
                    count = count + 1
                    outf.write('>' + key + '\n')
                    outf.write(dict[key] + '\n' + '\n')
    print(count)
    outf.close()


main()

