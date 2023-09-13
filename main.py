import tkinter as tk
from tkinter import ttk
from dir_cleaner import move_files_n_dirs_by_extension
from unzip_file import unzip
from tkinter import filedialog


window = tk.Tk()
window.title("Utils4Yoou")
window.geometry("600x750")
window.resizable(False, False)

n = ttk.Notebook(window)
n.pack(fill="both", expand= True)

def file_choose(filename):
    selected_directory = filedialog.askdirectory()
    filename.config(state=tk.NORMAL)  
    filename.delete("1.0", tk.END)  
    filename.insert(tk.END, selected_directory)  
    filename.config(state=tk.DISABLED)

def clear_label(label_name):
    label_name.config(state=tk.NORMAL)
    label_name.delete("1.0", tk.END)
    label_name.config(state=tk.DISABLED)

def clean_directory():
    input_directory = first_file.get("1.0", "end-1c")  
    output_directory = second_file.get("1.0", "end-1c")  
    move_files_n_dirs_by_extension(input_directory, output_directory)
    clear_label(first_file)
    clear_label(second_file)

def unzip_your_past():
    input_directory = third_file.get("1.0", "end-1c")  
    output_directory = fourth_file.get("1.0", "end-1c")  
    unzip(input_directory, output_directory)
    clear_label(third_file)
    clear_label(fourth_file)

first = tk.Frame(n)
second = tk.Frame(n)
n.add(first, text = "Directory cleaner")
n.add(second, text = "Unzip your problems")

first_file = tk.Text(first, height=1, width=50)
first_file.place(x=30, y=53)
first_file.config(state=tk.DISABLED)

second_file = tk.Text(first, height=1, width=50)
second_file.place(x=30, y = 113)
second_file.config(state=tk.DISABLED)

third_file = tk.Text(second, height=1, width=50)
third_file.place(x=30, y=53)
third_file.config(state=tk.DISABLED)

fourth_file = tk.Text(second, height=1, width=50)
fourth_file.place(x=30, y=113)
fourth_file.config(state=tk.DISABLED)


text_label = tk.Label(first, text="Directory to clean: ", font=("Arial", 16), fg="black")
text_label.place(x = 30, y = 20)

text_label_2 = tk.Label(first, text="Directory to output sorted data: ", font=("Arial", 16), fg="black")
text_label_2.place(x = 30, y = 80)

text_label_3 = tk.Label(second, text="Choose file to unzip", font=("Arial", 16), fg="black")
text_label_3.place(x = 30, y = 20)

text_label_4 = tk.Label(second, text="Choose destination directory", font=("Arial", 16), fg="black")
text_label_4.place(x = 30, y = 75)


browse_button = tk.Button(first, text ="Browse...", command= lambda: file_choose(first_file), width= 10, height= 1)
browse_button.place(x = 440 , y  = 51)

browse_button2 = tk.Button(first, text = "Browse", command = lambda: file_choose(second_file), width= 10, height= 1)
browse_button2.place(x = 440,y = 111)

browse_button3 = tk.Button(second, text ="Browse...", command= lambda: file_choose(third_file), width= 10, height= 1)
browse_button3.place(x = 440 , y  = 51)

browse_button4 = tk.Button(second, text ="Browse...", command= lambda: file_choose(fourth_file), width= 10, height= 1)
browse_button4.place(x = 440 , y  = 111)

clean_button = tk.Button(first, text="Clean...", command=clean_directory, width=10, height=1)
clean_button.place(x=230, y=200)

unzip_button = tk.Button(second, text = "unzip...", command= unzip_your_past, width= 10, height= 1)
unzip_button.place(x = 230, y = 200)

window.mainloop()