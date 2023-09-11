import tkinter as tk
from dir_cleaner import move_files_n_dirs_by_extension
from unzip_file import unzip


window = tk.Tk()
window.title("Utils4Yoou")
window.geometry("400x550")


clean_button = tk.Button(window, text ="Choose directory to clean", command= move_files_n_dirs_by_extension)
clean_button.place(x= 120 , y= 50)

unzip_button = tk.Button(window, text = "Choose file to unzip", command= unzip)



window.mainloop()