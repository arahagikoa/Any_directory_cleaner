import os
import shutil
from tkinter import filedialog

def move_files_n_dirs_by_extension():
    src_dir = filedialog.askdirectory()
    dir_sort = filedialog.askdirectory() 
    sort_path = os.path.join(src_dir, dir_sort)
    
    if not os.path.exists(sort_path):
        os.makedirs(sort_path) #check if we can create a directory, if this directory exists it will no delete it, just add more files to it
    
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        try:
            if os.path.isfile(item_path):
                if '.' in item:
                    #if file has extension create a path 
                    file_extension = item.split(".")[-1].lower()
                    dir_path = os.path.join(sort_path, file_extension)
                else:

                    dir_path = os.path.join(sort_path, "NoExtension")
                #creating diretory for specific extension
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                
                dest_path = os.path.join(dir_path, item)
                shutil.move(item_path, dest_path)
                print(f"Moved {item} to {dest_path}")
        except PermissionError:
            print(f"Skipped {item} due to PermissionError (file in use).")

#clean_path = filedialog.askdirectory()
#print(f"Selected directory to clean: {clean_path}")
#move_files_n_dirs_by_extension(clean_path)
