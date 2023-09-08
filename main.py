import os
import shutil

desktop = os.path.expanduser(r"C:\Users\kmlkr\OneDrive\Pulpit")

list_of_exts_n_dirs = {
    "pdf": r"C:\Users\kmlkr\OneDrive\Pulpit\Stuff\pdfs",
    "lnk": r"C:\Users\kmlkr\OneDrive\Pulpit\Stuff\short",
    "exe": r"C:\Users\kmlkr\OneDrive\Pulpit\Stuff\exe",
    "txt": r"C:\Users\kmlkr\OneDrive\Pulpit\Stuff\otheroffice"
}

for dir_path in list_of_exts_n_dirs.values():
    os.makedirs(dir_path, exist_ok=True)


def move_files_by_extension(src_dir, dest_dir):
    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1].lower()
            for extension, dir_path in list_of_exts_n_dirs.items():
                if file_extension == extension:
                    dest_path = os.path.join(dir_path, filename)
                    shutil.move(file_path, dest_path)
                    print(f"Moved {filename} to {dir_path}")


for extension, dest_dir in list_of_exts_n_dirs.items():
    move_files_by_extension(desktop, dest_dir)
