import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
my_w = tk.Tk()
my_w.geometry("1170x640+10+10")  # Size of the window
my_w.title('Read CSV Files')
my_w.resizable(False, False)

my_font1=('times', 12, 'bold')
l1 = tk.Label(my_w,text='Read File & create DataFrame', width=80,font=my_font1)
l1.grid(row=1,column=1)

b1 = tk.Button(my_w, text='Browse for a Excel File', width=20,command = lambda:upload_file())
b1.grid(row=2,column=1)

t1=tk.Text(my_w,width=142,height=35)
t1.grid(row=3,column=1,padx=15)

def upload_file():
    t1.insert(tk.END, '')

    f_types = [('CSV files',"*.csv"),
               ('Excel files', "*.xls"),
               ('Excel files', "*.xlsx"),
               ('JSON files', "*.json"),
               ('XML files', "*.xml"),
               ('All',"*.*")]
    file = filedialog.askopenfilename(filetypes=f_types)
    l1.config(text=file) # display the path
    if file:
        #df=pd.read_csv(file) # create DataFrame
        df=pd.read_excel(file)
        str1=file + " - Rows:" + str(df.shape[0])+ " - Columns:"+str(df.shape[1])+ "\n"*2

        print(df.info())
        t1.insert(tk.END, str1) # add to Text widget
    else:
        str1 = ''
        t1.insert(tk.END, str1)
my_w.mainloop()  # Keep the window open