from tkinter import *
from tkinter import ttk
import tkinter.messagebox as box
import os
from tkinter.filedialog import askopenfilenames
myList={}
global timesButtonClicked

timesButtonClicked = 0

window = Tk()
window.title('RMS Files')

window.geometry("850x400+70+150")

frame = ttk.Frame(window, width = 400, height = 400)# padding=(3, 3, 12, 12))
frame.grid(column=1, row=5, sticky=(N, S, E, W))

#frame = Frame(window)
listbox = Listbox(frame, width = 100, height = 50, selectmode='multiple')


filetypes = (
        ('Text files' , '*.txt'),
        ('CSV Files'  , '*.csv'),
        ('Excel Files', '*.xls'),
        ('Excel Files', '*.xlsx'),
        ('JSON Files' , '*.json'),
        ('XML Files'  , '*.xml'),
        ('All files'  , '*.*')
    )

def selectFiles():
    global timesButtonClicked
    myList = askopenfilenames(title='Open files',
                              initialdir='/',
                              filetypes=filetypes)  # os.listdir('E:\Parnika\Art')

    print('Files List : from selectFiles'+'\n' + str(myList))
    timesButtonClicked = timesButtonClicked + 1
    for name in myList:
        listbox.insert('end', name)

def listbox_used(event):
    curselection = listbox.curselection()
    mesg=''
    print('from listbox_used() event')
    for index in curselection:
            mesg = mesg + '\n' + str(listbox.get(index))
            print('From listbox_used() for stmt '+ listbox.get(index))  # Gets current selection from listbox
            # Only challenge with this implementation is the incremental growth of the list.
            # However, this could be resolved with a Submit button that gets the final selections.
    box.showinfo('Selected Files..', 'Your Choice of files from listbox_used() ' + mesg)

def dialog():
    filenames =''
    dialogMesg = 'No of Files Selected, from dialog(): ' + str(len(listbox.curselection())) + '\n'
    if len(listbox.curselection()) > 0:
        print("No of Files Selected, from dialog(): " + str(len(listbox.curselection())))

        for index in listbox.curselection():
            filenames = filenames + str(listbox.get(index)) + '\n'

    else:
        print("Length of File Name from dialog() Else Block")
        filenames ='Error!','Please Select Files'

    box.showinfo('Your file(s) Selection',dialogMesg + str(filenames))


btn = Button(frame, text='View Selected File Info', command=dialog)
fileSelectButton = Button(frame, text='Select Files', command=selectFiles)

btn.pack(side=RIGHT, padx=5)
fileSelectButton.pack(side=RIGHT, padx=5)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack(side=LEFT)
frame.pack(padx=10, pady=30)

# MyListBox = Listbox(frame)
# for file in myList:
#     MyListBox.insert(END, file)


window.mainloop()
