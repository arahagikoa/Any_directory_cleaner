import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from dir_cleaner import move_files_n_dirs_by_extension
from unzip_file import unzip

def choose_directory(text_widget):
    selected_directory = filedialog.askdirectory()
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    text_widget.insert(tk.END, selected_directory)
    text_widget.config(state=tk.DISABLED)

def clear_text_widget(text_widget):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", tk.END)
    text_widget.config(state=tk.DISABLED)

def clean_directory():
    input_directory = input_dir_text.get("1.0", "end-1c")
    output_directory = output_dir_text.get("1.0", "end-1c")
    move_files_n_dirs_by_extension(input_directory, output_directory)
    clear_text_widget(input_dir_text)
    clear_text_widget(output_dir_text)

def unzip_files():
    input_directory = unzip_input_text.get("1.0", "end-1c")
    output_directory = unzip_output_text.get("1.0", "end-1c")
    unzip(input_directory, output_directory)
    clear_text_widget(unzip_input_text)
    clear_text_widget(unzip_output_text)

window = tk.Tk()
window.title("Utils4You")
window.geometry("600x400")
window.resizable(False, False)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

directory_cleaner_tab = tk.Frame(notebook)
unzip_tab = tk.Frame(notebook)

notebook.add(directory_cleaner_tab, text="Directory Cleaner")
notebook.add(unzip_tab, text="Unzip Files")

# Dir cleaner

input_dir_label = tk.Label(directory_cleaner_tab, text="Directory to clean:", font=("Arial", 12))
input_dir_label.pack(pady=10)

input_dir_text = tk.Text(directory_cleaner_tab, height=1, width=50)
input_dir_text.pack()

output_dir_label = tk.Label(directory_cleaner_tab, text="Output directory:", font=("Arial", 12))
output_dir_label.pack(pady=10)

output_dir_text = tk.Text(directory_cleaner_tab, height=1, width=50)
output_dir_text.pack()

browse_input_button = tk.Button(directory_cleaner_tab, text="Browse...", command=lambda: choose_directory(input_dir_text))
browse_input_button.place(x = 30, y = 40)

browse_output_button = tk.Button(directory_cleaner_tab, text="Browse...", command=lambda: choose_directory(output_dir_text))
browse_output_button.place(x = 30, y = 105)

clean_button = tk.Button(directory_cleaner_tab, text="Clean", command=clean_directory)
clean_button.pack(pady=20)

#Unzip

unzip_input_label = tk.Label(unzip_tab, text="Choose file to unzip:", font=("Arial", 12))
unzip_input_label.pack(pady=10)

unzip_input_text = tk.Text(unzip_tab, height=1, width=50)
unzip_input_text.pack()

unzip_output_label = tk.Label(unzip_tab, text="Choose destination directory:", font=("Arial", 12))
unzip_output_label.pack(pady=10)

unzip_output_text = tk.Text(unzip_tab, height=1, width=50)
unzip_output_text.pack()

browse_input_button = tk.Button(unzip_tab, text="Browse...", command=lambda: choose_directory(unzip_input_text))
browse_input_button.place(x = 30, y = 40)

browse_output_button = tk.Button(unzip_tab, text="Browse...", command=lambda: choose_directory(unzip_output_text))
browse_output_button.place(x = 30, y = 105)

unzip_button = tk.Button(unzip_tab, text="Unzip", command=unzip_files)
unzip_button.pack(pady=20)

window.mainloop()
