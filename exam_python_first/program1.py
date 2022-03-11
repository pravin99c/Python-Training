from ast import withitem
from typing_extensions import final
import zipfile
import gdown
from zipfile import ZipFile
import random
import glob
import string
import os
import shutil

from pyparsing import Word
url = "https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view"
output = "/home/woc/Pravin/Trainee/python_training/exam_python_first/"
id = "1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu"
gdown.download(id=id, output=output, quiet=False, fuzzy=True)

# extract zip file
#-----------------------------------------------------------------

folder_zip_path = '/home/woc/Pravin/Trainee/python_training/exam_python_first/'

with zipfile.ZipFile('/home/woc/Pravin/Trainee/python_training/exam_python_first/Exam.zip', 'r') as zip_ref:
    zip_ref.extractall(folder_zip_path)

#_-----------------------------------------------
# create out put folder

try:
    folder_path = folder_zip_path + 'Output/'
    os.mkdir(folder_path)
except:
    pass
finally:
    path_folder = folder_path + 'text.txt'

    open_file = open(path_folder,"w+")

    root = folder_zip_path + 'Exam/'

    for root, dirs, files in os.walk(root):  
        for f in files:
            open_file.write(os.path.join(root, f) + '\n')
            
    open_file.close()


read_file = open(path_folder)

lines_list = read_file.read().splitlines()
# print(lines_list)

s=10
words_list = []
for i in range(20): 
    ran = ''.join(random.choices(string.ascii_uppercase, k = s))    
    words_list.append(str(ran))

for file in lines_list:
    open_file_write = open(file,'w')
    for i in words_list:
        random_name = i
    open_file_write.write(random_name)
    open_file_write.close()
    # print(file.split('Exam')[1])
    change = file.split('Exam')[1]
    path2 = '/home/woc/Pravin/Trainee/python_training/exam_python_first/Output/allfile/'
    completeName = os.path.join(path2, file.split('text.txt')[1]+change.replace('/','_'))
    os.rename(file,completeName)
   



