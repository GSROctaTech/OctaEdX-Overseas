from tkinter import *
import tkinter.messagebox as box
import os
from tkinter.filedialog import askopenfilenames
myList={}

window = Tk()
window.title('RMS Files')

frame = Frame(window)
listbox = Listbox(frame,width=150,height=30)

def selectFiles():
    myList = askopenfilenames()  # os.listdir('E:\Parnika\Art')
    print(myList)
    for name in myList:
        listbox.insert('end', name)

def dialog():
    if len(listbox.curselection()) > 0:
        box.showinfo('Selection', 'Your Choice: ' + listbox.get(listbox.curselection()))
    else:
        box.showinfo('Error!','Please Select Files')

btn = Button(frame, text='View Selected File Info', command=dialog)
fileSelectButton = Button(frame, text='Select Files', command=selectFiles)

btn.pack(side=BOTTOM, padx=5)
fileSelectButton.pack(side=BOTTOM, padx=5)

listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30) # List/Other Objects Place after 30 space padding on the form

# MyListBox = Listbox(frame)
# for file in myList:
#     MyListBox.insert(END, file)


window.mainloop()
