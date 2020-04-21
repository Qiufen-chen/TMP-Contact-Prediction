"""
purpose：将TXT文件里的特定字符替换成想要的，并保存修改
"""
import os
def readFile(rootdir):
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            file_data = ""
            with open(path, "r") as f:
                  for line in f:
                        if line[5:7].strip() == 'H':
                            line = line.replace(line[5:7].strip(), '1')
                        else:
                            line = line.replace(line[5:7].strip(), '0')
                        file_data += line

            with open(path, "w") as f:
                  f.write(file_data)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    dir = 'E:/3D_file/'
    readFile(dir)