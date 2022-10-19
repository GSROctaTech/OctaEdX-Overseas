# https://www.plus2net.com/python/tkinter.php
import tkinter as tk
import os
from tkinter import messagebox

# Application Window
root = tk.Tk()
root.geometry("500x500+10+10")  # Size of the window & Window Position (10+10)
root.title("Resource Management System ")  # Adding a title
root.resizable(width=0,height=0) # resizing of window is not allowed
root.state('normal') # while opening we can set to full screen, options : zoomed default is 'normal'

# Change the background colour
# root.configure(background='gray')
# root .configure(background='#FFFF00')

# For Transparent Window
# root.attributes('-alpha',0.5)

# Ref : https://stackoverflow.com/questions/33137829/how-to-replace-the-icon-in-a-tkinter-app
root.iconbitmap("images/rms.ico")

# Buttons
# Function to Close the window --> root.destroy()
my_font = ('times', 8, 'underline')

testButton = tk.Button(root,
                       text='Test',
                       width=40,
                       #height=2,
                       default='active', # set focus to this button on form loading
                       state='normal', # Other Options 'disabled', default 'normal'
                       disabledforeground='red', # disbled color
                       font=my_font,
                       fg='red', # foreground Color
                       highlightbackground='red',
                       bg='yellow', # Background Color, Same As Var :background
                       bd=5, # Border,  Same As Var :borderwidth
                       activebackground='red',
                       activeforeground='green',
                       cursor='boat',
                       highlightcolor='blue',
                       highlightthickness=5
                       )
testButton.grid(row=1,column=1)

closeButton = tk.Button(root, text='Close Window', width=20,bg='blue', command=root.destroy)
closeButton.grid(row=10,column=2)

exitButton = tk.Button(root, text='Exit Application', width=20,command=lambda: ExitApp(),bg='brown',fg='white')
exitButton.grid(row=12,column=2)

functionButton = tk.Button(root, text='Change Color', width=20,bg='blue',command=lambda: my_upd())
functionButton.grid(row=11,column=2)

colorButton = tk.Button(root,text='B1',width=10,activeforeground='green')
colorButton.grid(row=11,column=3)

buttonBorder=tk.Button(root,text='Border Button', width=10, command=lambda:buttonBorder.config(bd=0))
buttonBorder.grid(row=12,column=3)

# Window Closing Options
root.bind('<Escape>', lambda e:root.quit()) # to close window by pressing "ESC" key








#######################################################################################################################
# Functions definations used in this file
#######################################################################################################################
def my_upd():
    functionButton.config(bg='red')

def function_test():
    print('hi')

def ExitApp():
    MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',icon='warning')
    if MsgBox == 'yes':
        root.destroy()
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')

def button_toggle():
        st = b2["state"]
        if (st == "normal"):
            b2["state"] = "disabled"
            b2["text"] = "I am Disabled"
            b1["text"] = "Enable"
        else:
            b2["state"] = "normal"
            b2["text"] = "I am Enabled"
            b1["text"] = "Disable"

            #usage mybutton = tk.Button(root, text='Disable',command=lambda: button_toggle())


def changeProperty(*args):
    buttonConfig.config(bg='red')
    # Usage  buttonConfig = tk.Button(root, text='Change Color', width=50, bg='yellow',command=lambda: changeProperty())
    #        buttonConfig.grid(row=2, column=2)

def increase_button_size():
    w = testButton.cget('width') # read the width of the button
    w = w+5              # increase width by 5
    testButton.config(width=w)
    # Usage : testButton = tk.Button(root, text='+', width=10,bg='yellow', command=lambda: increase_button_size())


def buttonClickCount():
    global count
    count = count + 1  # increase by 1
    my_button.config(text='Count: ' + str(count))  # update text

    # Usage :
    #     count=0 # initial value of counter
    #     my_button = tk.Button(root, text='Count: 0 ', width=12, command=lambda: buttonClickCount(), bg='orange', font=12)
    #     my_button.grid(row=0, column=0, padx=100, pady=50)


def CheckValidTextSize(*args):
    if(len(my_str.get())>4): # Minimum 5 char length
        validValButton.config(state='normal') # Enable the button
    else:
        validValButton.config(state='disabled') # disable the button


    # Usage :

    # my_str = tk.StringVar(root)
    # e1 = tk.Entry(root, textvariable=my_str)
    # e1.grid(row=0, column=0)
    # validValButton = tk.Button(root, text='Button', state='disabled')
    # validValButton.grid(row=0, column=1)
    # my_str.trace('w',CheckValidTextSize) # event listener
#######################################################################################################################

# Keep Window Running/Open
root.mainloop()  # Keep the window open
