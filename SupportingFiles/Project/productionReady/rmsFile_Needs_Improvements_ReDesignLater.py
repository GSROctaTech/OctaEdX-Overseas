import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
from tkinter import *

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('500x450')

curWrkDir = os.getcwd()
filenames = os.listdir(curWrkDir)
print("The current working directory is", curWrkDir)
print("Files in current working directory are : ", filenames)
pathname = os.path.join(filenames[1])
print("File : ", filenames[1])
for index in range(len(filenames)):
    value = filenames[index]
    print("Path : " + str(index) + "- " + curWrkDir + "\\" + value)

def select_files():
    filetypes = (('Text files', '*.txt'),('All files', '*.*'))

    selectedfilenames = fd.askopenfilenames(title='Open files',
                                            initialdir='/',
                                            filetypes=filetypes)

    #showinfo(title='Selected Files', message=selectedfilenames)

    selectedfilenames = select_files()
    Lb = Listbox(root)

    for index in range(len(selectedfilenames)):
        value = selectedfilenames[index]
        print(str(index) + " " + str(selectedfilenames[index]))
        Lb.insert(index, value)
        Lb.pack()

def open_file():
    file = fd.askopenfilenames(parent=root, title='Choose a File')
    fv_fileslist = root.splitlist(file)
    return fv_fileslist

# open button
open_button = ttk.Button(root, text='Open Files', command=open_file)
open_button.pack(expand=True)

# top = Tk() -- Create New Form Instance

fileslist = open_file()

Lb = Listbox(root,width=150,height=80)

for index in range(len(fileslist)):
    value = fileslist[index]
    print(str(index) + " " + str(fileslist[index]))
    Lb.insert(index, value)
    Lb.pack()

root.mainloop()
