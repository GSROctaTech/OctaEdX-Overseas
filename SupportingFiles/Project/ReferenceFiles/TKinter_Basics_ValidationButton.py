import tkinter as tk
my_w=tk.Tk()
my_w.geometry('200x100')
my_str=tk.StringVar(my_w)
e1=tk.Entry(my_w,textvariable=my_str)
e1.grid(row=0,column=0)
b1=tk.Button(my_w,text='Button',state='disabled')
b1.grid(row=0,column=1)
def my_upd(*args):
    if(len(my_str.get())>4): # Minimum 5 char length
        b1.config(state='normal') # Enable the button
    else:
        b1.config(state='disabled') # disable the button
my_str.trace('w',my_upd) # event listener
my_w.mainloop()