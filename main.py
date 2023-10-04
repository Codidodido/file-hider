import tkinter as tk
from tkinter import filedialog
import os
from tkinter import ttk
import datetime
import os.path
from module import humanize


def save_files_to_file():
    with open('hide_list.txt', 'w') as file:
        for item in file_tree.get_children():
            file_path = file_tree.item(item)['values'][1]
            file.write(f"{file_path}\n")


def load_files_from_file():
    if os.path.isfile('hide_list.txt'):
        with open('hide_list.txt', 'r') as file:
            for line in file:
                file_path = line.strip()
                if file_path and os.path.exists(file_path):
                    file_name = os.path.basename(file_path)
                    file_size = humanize.make_readable(os.path.getsize(file_path))
                    creation_time = os.path.getctime(file_path)
                    formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                    file_tree.insert("", "end", values=(file_name, file_path, file_size, formatted_time))

def browse_file():
    file_path = filedialog.askopenfilenames()
    for file in file_path:
        os.system(f'attrib +h "{file}"')
        file_name = os.path.basename(file)
        file_size = humanize.make_readable(os.path.getsize(file))
        creation_time = os.path.getctime(file)
        formatted_time = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        file_tree.insert("", "end", values=(file_name, file, file_size, formatted_time))
        save_files_to_file()

def remove_file():
    selected_items = file_tree.selection()
    for item in selected_items:
        selected_file = file_tree.item(item)['values'][1]
        os.system(f'attrib -h "{selected_file}"')
        file_tree.delete(item)
    save_files_to_file()

root = tk.Tk()
root.title("File Hider")

file_tree = ttk.Treeview(root, columns=("File Name", "File Path", "Size", "Creation Date"))
file_tree.heading("File Name", text="File Name")
file_tree.heading("File Path", text="File Path")
file_tree.heading("Size", text="Size")
file_tree.heading("Creation Date", text="Creation Date")
file_tree.pack(padx=10, pady=10)

browse_button = tk.Button(root, text="Browse", command=browse_file)
remove_button = tk.Button(root, text="Remove", command=remove_file)

browse_button.pack(padx=10, pady=5)
remove_button.pack(padx=10, pady=5)

load_files_from_file()

root.mainloop()
