import subprocess
import os
import shutil
from tkinter import filedialog

#unzip file

def unzip():
    file = filedialog.askopenfilename()
    extraction_directory = filedialog.askdirectory()
    if "." in file:
        file_extension = file.split(".")[-1]
        commands = {
            "zip": "unzip {} -d {}".format(file, extraction_directory),
            "gz": "gunzip {} {}".format(file, extraction_directory),
            "tar": "tar -xvf {} -C {}".format(file, extraction_directory),
            "tar.gz": "tar -xzvf {} -C {}".format(file, extraction_directory),
            "tar.bz2": "tar -xjvf {} -C {}".format(file, extraction_directory),
            "7z": "7z x {} -o{}".format(file, extraction_directory)
        }
        for key, value in commands.items():
            if file_extension == key:
                result = subprocess.run(value, shell = True, stdout=subprocess.PIPE, text=True) 
                return result.stdout

unzip()