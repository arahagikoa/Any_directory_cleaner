import os
import shutil

desktop = os.path.expanduser(r"some path")

list_of_exts_n_dirs = {
    "pdf": r"some path",
    "lnk": r"some path",
    "exe": r"some path",
    "txt": r"some path"
}

for dir_path in list_of_exts_n_dirs.values():
    os.makedirs(dir_path, exist_ok=True)


def move_files_n_dirs_by_extension(src_dir, dest_dir):
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        try:
            if os.path.isfile(item_path):
                file_extension = item.split(".")[-1].lower()
                for extension, dir_path in list_of_exts_n_dirs.items():
                    if file_extension == extension:
                        dest_path = os.path.join(dir_path, item)
                        shutil.move(item_path, dest_path)
                        print(f"Moved {item} to {dir_path}")

        except PermissionError:
            print(f"Skipped {item} due to PermissionError (file in use).")

for extension, dest_dir in list_of_exts_n_dirs.items():
    move_files_n_dirs_by_extension(desktop, dest_dir)
