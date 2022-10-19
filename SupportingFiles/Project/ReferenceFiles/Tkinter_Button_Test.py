import tkinter as tk
from tkinter.filedialog import askopenfilenames

filename = None
def UploadAction(event=None):
    filename = askopenfilenames()
    print('Selected:', filename)
    # Change text of label
    label1['text'] = filename

root = tk.Tk()

button1 = tk.Button(text='Click Me', command=UploadAction, bg='brown', fg='white')
button1.pack(padx=2, pady=5)
label1 = tk.Label(text='Please choose a file')
label1.pack(padx=2, pady=2)

root.mainloop()