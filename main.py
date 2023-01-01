import os

def rewrite_file(path_1=None, path_2=None, path_3=None):
    if path_1 or path_2 or path_3 is None:
        path_1 = '1.txt'
        path_2 = '2.txt'
        path_3 = '3.txt'
        new_file = "rewrite_file.txt"
        file1_path = os.path.join(os.getcwd(), path_1)
        file2_path = os.path.join(os.getcwd(), path_2)
        file3_path = os.path.join(os.getcwd(), path_3)
        with open(file1_path, 'r', encoding='UTF-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='UTF-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='UTF-8') as f3:
            file3 = f3.readlines()
        with open(new_file, 'w', encoding='UTF-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
                f_total.write(path_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
                f_total.write(path_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
                f_total.write(path_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path_1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path_2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path_3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    return
print(rewrite_file())