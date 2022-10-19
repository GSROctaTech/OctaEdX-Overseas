
# https://medium.com/@fareedkhandev/themes-for-tkinter-232c17813e3a

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

# Creating root window
# root = Tk()
root = ThemedTk(theme="winxpblue")

# Setting window width & Height
root.geometry('300x400')

# Creating a button widget
mybutton = ttk.Button(root, text='Hellow World!')

# showing at the center of the screen
mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)

# running the App
root.mainloop()
