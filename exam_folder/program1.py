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
# download file
# a file
url = "https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view"
# output = "/home/woc/Pravin/Trainee/python_training/exam_python_first/"
# gdown.download(url, output, quiet=False)

# same as the above, but with the file ID

# id = "1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu"

# same as the above, and you can copy-and-paste a URL from Google Drive with fuzzy=True
#----------------------------------------
# url = "https://drive.google.com/file/d/0B9P1L--7Wd2vNm9zMTJWOGxobkU/view"
# gdown.download(id=id, output=output, quiet=False, fuzzy=True)