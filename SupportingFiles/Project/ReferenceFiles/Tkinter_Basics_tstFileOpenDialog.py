# Import the required libraries
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd

# Create an instance of tkinter frame or window
from click import open_file

win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")


def open_file():
    file = fd.askopenfilenames(parent=win, title='Choose a File')
    fv_fileslist = win.splitlist(file)
    return fv_fileslist

fileslist = open_file()

Lb = Listbox(win, width=100, height=30)

for index in range(len(fileslist)):
    value = fileslist[index]
    print(str(index) + " " + str(fileslist[index]))

    # Lb.insert(listfiles)
    Lb.insert(index, value)
    Lb.pack()

    # Add a Label widget
label = Label(win, text="Select the Button to Open the File", font=('Aerial 11'))
label.pack(pady=30)

# Add a Button Widget
ttk.Button(win, text="Select a File", command=open_file).pack()

win.mainloop()
