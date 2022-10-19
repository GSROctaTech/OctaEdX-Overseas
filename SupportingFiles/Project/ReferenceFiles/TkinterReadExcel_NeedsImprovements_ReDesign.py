import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pandas as pd

my_w = tk.Tk()
my_w.geometry("500x300")  # Size of the window
my_w.title('www.plus2net.com')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='Create DataFrame', width=30, font=my_font1)
l1.grid(row=0, column=1)
b1 = tk.Button(my_w, text='Upload Excel File', width=20, command=lambda: upload_file())
b1.grid(row=1, column=1)
t1 = tk.Text(my_w, height=30, width=150, bg='yellow')  # added one text box
t1.grid(row=2, column=1, padx=30, pady=10)  #


def upload_file():
    file = filedialog.askopenfilename(
        filetypes=[("Excel file", ".xlsx")])
    df = pd.read_excel(file, index_col=1)  # creating DataFrame
    t1.delete('1.0', END)  # Delete previous data from position 0 till end
    t1.insert(tk.END, df.head())  # adding data to text widget


my_w.mainloop()  # Keep the window open
