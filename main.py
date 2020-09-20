from os import listdir
from os.path import isfile, join
import os
import shutil
import re


def download_folder_sorter(myPath):
    files = [f for f in listdir(myPath) if isfile(join(myPath,f))]

    for file in files:
        temp = re.search('[a-zA-Z]{3}\d{3}', file)
        course = (temp.group(0) if temp else 'none')
        new_folder = myPath + '/' + course.upper()
        src_path = myPath + '/' + file
        if course == 'none':
            continue
        if os.path.isdir(new_folder):
            pass
        elif course != 'none':
            os.mkdir(new_folder)
        shutil.move(src_path, new_folder)
        print(course)


myPath = r'C:\Users\beyku\Downloads'
download_folder_sorter(myPath)