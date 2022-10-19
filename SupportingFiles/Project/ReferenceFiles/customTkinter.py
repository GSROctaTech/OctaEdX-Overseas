#https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22

from tkinter import *
import customtkinter

# Creating root window
# root = Tk()
root = customtkinter.CTk()

#customtkinter.set_appearance_mode("light")

# Setting window width & Height
root.geometry('300x400')

# Creating a button CTkButton instead of tkinter Button
mybutton = customtkinter.CTkButton(master=root, text='Hellow World!')

# showing at the center of the screen
mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)

# running the App
root.mainloop()