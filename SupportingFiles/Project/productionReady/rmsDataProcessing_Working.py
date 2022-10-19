# Youtube Link: https://www.youtube.com/watch?v=PgLjwl6Br0k
# https://gist.github.com/RamonWill/0686bd8c793e2e755761a8f20a42c762

import tkinter as tk
from tkinter import filedialog, messagebox, ttk, IntVar
import codecs
import pandas as pd

# initalise the tkinter GUI
root = tk.Tk()
#global noOfRowsToFetch
noOfRowsToFetch = IntVar()

root.geometry("1080x600+10+10")  # set the root dimensions of MainForm/Window
root.pack_propagate(False)  # tells the root to not let the widgets inside it determine its size.
# root.resizable(0, 0) # makes the root window fixed in size.

# Frame for TreeView/Table View
frame1 = tk.LabelFrame(root, text="Excel Data", )
frame1.place(height=380, width=1000)

# Treeview/Table/Grid Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical",
                           command=tv1.yview)  # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal",
                           command=tv1.xview)  # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set,
              yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=1000, rely=0.65, relx=0)

# The file/file path Text or Error Message
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)

# Buttons
btnSelectFile = tk.Button(file_frame, text="  Select File  ", command=lambda: File_dialog())
btnSelectFile.place(rely=0.5, relx=0.01)

btnLoadFile = tk.Button(file_frame, text=" Load File ", command=lambda: Load_excel_data())
btnLoadFile.place(rely=0.5, relx=0.35)

btnCbxVal = tk.Button(file_frame, text=" Show Rows Value ", command=lambda: fetchCmbox())
btnCbxVal.place(rely=0.5, relx=0.24)

# Combobox creation
# ComboBox Lable
Cboxlabel = ttk.Label(file_frame, text="Rows to Fetch :")
Cboxlabel.place(rely=0.55, relx=0.10)

n = tk.IntVar()
cbxRowsToFetch = ttk.Combobox(file_frame, width=4, textvariable=n, state='readonly',
                              values=(5, 10, 20, 30, 40, 50, 100))
cbxRowsToFetch.place(rely=0.55, relx=0.18)
cbxRowsToFetch.current(0)

def fetchCmbox():
    global noOfRowsToFetch
    messagebox.showinfo("Information - From fetchCmBox() - Before Assigning Var noOfRowToFetch : ", cbxRowsToFetch.get())
    noOfRowsToFetch = n.get()
    print("from fetchCmbox() - noOfRowsToFetch : " + str(noOfRowsToFetch) + ' - cbxRowsToFetch.get()' + cbxRowsToFetch.get())
# --------------------------------------------- Test ComboBox Start -----------------------------------------------------
# Define Days Tuple
days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')

# Function to print the index of selected option in Combobox
def callback(*arg):
    label_comboSelection = ttk.Label(file_frame,
                                     text="The value at index " + str(cb.current()) + " is" + " " + str(var.get()),
                                     font=('Helvetica 12'))
    label_comboSelection.place(rely=0.6, relx=0)

# Create a combobox widget
var = tk.StringVar()
cb = ttk.Combobox(file_frame, textvariable=var)
cb['values'] = days
cb['state'] = 'readonly'
cb.pack(fill='x', padx=5, pady=5)
cb.place(rely=0.55, relx=0.48)

# Set the tracing for the given variable
var.trace('w', callback)
# --------------------------------------------- Test ComboBox End ------------------------------------------------------


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filetypes = (('Text files', '*.txt'), ('CSV Files', '*.csv'), ('Excel Files', '*.xls'), ('Excel Files', '*.xlsx'),
                 ('JSON Files', '*.json'), ('XML Files', '*.xml'), ('All files', '*.*'))

    initDir = 'E:\GSReddy\PythonProjects\SampleData' # "/"
    filename = filedialog.askopenfilename(initialdir=initDir, title="Select A File", filetype=filetypes)
    label_file["text"] = filename
    return None

def Load_excel_data():
    global noOfRowsToFetch
    messagebox.showinfo("Information - From Load_excel_data() - Before Assigning Var cbxRowsToFetch : ", cbxRowsToFetch.get())
    noOfRowsToFetch = n.get()
    messagebox.showinfo("Information - From Load_excel_data() - After Assigning Var cbxRowsToFetch : ", cbxRowsToFetch.get())

    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            print('File Name : ' + excel_filename + ' Extension : ' + excel_filename[-4:])
            df = pd.read_csv(excel_filename)
        elif excel_filename[-4:] == ".txt":
            print('File Name : ' + excel_filename + ' Extension : ' + excel_filename[-4:] + ' noOfRowsToFetch : ' + str(noOfRowsToFetch))
            df = pd.read_csv(excel_filename, sep=',', nrows=noOfRowsToFetch)  # , lineterminator='\r')
            # df = pd.read_csv(excel_filename, sep='\t', lineterminator='\r')
            # excel_filename = codecs.open('document', 'en', 'UTF-16')  # open for reading with "universal" type set
            # df = pd.read_csv(excel_filename, sep='\t', skiprows=range(1,4), nrows=2)
        else:
            print('File Name : ' + excel_filename + ' Extension : ' + excel_filename[-4:])
            df = pd.read_excel(excel_filename)
    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)  # let the column heading = column name

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end",
                   values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None

def clear_data():
    tv1.delete(*tv1.get_children())
    return None

root.mainloop()
