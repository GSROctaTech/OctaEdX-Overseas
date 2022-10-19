import tkinter as tk
from tkinter import filedialog
my_w = tk.Tk()
my_w.geometry("400x200")  # Size of the window
my_w.title("Data Processing")  #  title
my_dir='' # string to hold directory path
def my_fun():
    my_dir = filedialog.askdirectory() # select directory
    l1.config(text=my_dir) # update the text of Label with directory path

b1=tk.Button(my_w,text='Select directory',font=22, command=lambda:my_fun(),bg='lightgreen')
b1.grid(row=0,column=0,padx=10,pady=20)
l1=tk.Label(my_w,text=my_dir,bg='yellow',font=18)
l1.grid(row=0,column=1,padx=2)
my_w.mainloop()  # Keep the window open