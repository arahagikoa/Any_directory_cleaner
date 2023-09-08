import os 
import shutil 


desktop = os.path.expanduser(r"C:\Users\kmlkr\OneDrive\Pulpit\Stuff\pdfs")
pdf_dir = os.path.expanduser(r"C:\Users\kmlkr\OneDrive\Pulpit\Stuff\pdfs")

for dir_path in [pdf_dir]:
    os.makedirs(dir_path, exist_ok = True)


def move_files_by_extension(src_dir, dest_dir, extensions):
    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1].lower()
            if file_extension in extensions:
                dest_path = os.path.join(dest_dir, filename)
                shutil.move(file_path, dest_path)
                print (f"Moved {filename} to {dest_dir}")


pdf = ["pdf"]
move_files_by_extension(desktop, pdf_dir, pdf)