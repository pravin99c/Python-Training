
## 1. https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view?usp=sharing (Demo url)
=>Take as an Input Downloadable URL link of Gdrive zip and output folder path where you can store all the results.
=>Download this file using python
=>There is a hierarchy of folders add all of that hierarchy in a text file
E.g. Folder/text.txt
       Folder - Copy (3)/Folder/text.txt
=>Create a file that can generate random names
=>Add Random names in all the text files
=>Create one Folder named output and add all the text files inside that folder. (All text file names are the same use your logic how can you create difference) 


## Input:
    Take as an Input Downloadable URL link of Gdrive zip and output folder path where you can store all the results.
    Download this file using python
    There is a hierarchy of folders add all of that hierarchy in a text file

## Output :
    Folder/text.txt
    Folder - Copy (3)/Folder/text.txt
    Create a file that can generate random names
    Add Random names in all the text files
    Create one Folder named output and add all the text files inside that folder. (All text file names are the same use your logic how can you create difference)

# testcases

| Input | Output |
| ------ | ------ |
| url = "https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view"
output = "/home/woc/Pravin/Trainee/python_training/exam_python_first/"
id = "1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu"
gdown.download(id=id, output=output, quiet=False, fuzzy=True)
 | all folder/text.txt file in new folder |


## Development



