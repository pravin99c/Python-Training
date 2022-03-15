"""
Exam q1 = https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view?usp=sharing (Demo url)
=>Take as an Input Downloadable URL link of Gdrive zip and output folder path where you can store all the results.
=>Download this file using python
=>There is a hierarchy of folders add all of that hierarchy in a text file
E.g. Folder/text.txt
       Folder - Copy (3)/Folder/text.txt
=>Create a file that can generate random names
=>Add Random names in all the text files
=>Create one Folder named output and add all the text files inside that folder. (All text file names are the same use your logic how can you create difference) 
"""
import zipfile
import gdown
from zipfile import ZipFile
import random
import glob
import string
import os
import shutil

# from pyparsing import Word
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
# create output folder and create zip file to test.txt file

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


# create random world and write text.txt file to append random world or copy all text.txt file with new folder 
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
   



