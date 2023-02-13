import tkinter as tk
from tkinter import filedialog
import os

def rename_files():
    path = filedialog.askdirectory()
    addition = entry.get()
    for filename in os.listdir(path):
        new_name = filename.split(".")[0] + "-" + addition + "." + filename.split(".")[1]
        os.rename(os.path.join(path, filename), os.path.join(path, new_name))

root = tk.Tk()
root.title("Rename Files")
root.geometry("400x200")


label = tk.Label(root, text="Enter the addition:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

rename_button = tk.Button(root, text="Rename Files", command=rename_files)
rename_button.pack(pady=10)

root.mainloop()