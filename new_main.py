import os
import shutil

desktop = os.path.expanduser(r"C:\Users\kmlkr\OneDrive\Pulpit")



def move_files_n_dirs_by_extension(src_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        try:
            if os.path.isfile(item_path):
                file_extension = item.split(".")[-1].lower()
                dir_path = os.path.join(src_dir, file_extension)
                if os.path.exists(dir_path):
                    dest_path = os.path.join(dir_path, item)
                    shutil.move(item_path, dest_path)
                    print(f"Moved {item} to {dest_path}")
                else:
                    os.makedirs(dir_path)
                    dest_path = os.path.join(dir_path, item)
                    shutil.move(item_path, dest_path)
                    print(f"Moved {item} to {dest_path}")
        except PermissionError:
            print(f"Skipped {item} due to PermissionError (file in use).")


move_files_n_dirs_by_extension(desktop)
