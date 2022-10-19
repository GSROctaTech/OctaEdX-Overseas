from glob import glob
import tkinter as tk
import sys

class FileList:
    def __init__(self, ft):
        root = tk.Tk()
        root.geometry("400x800")
        lb = tk.Listbox(root)
        lb.configure(bg="gold")
        lb.pack(fill="both", expand=True)
        fl = glob("*." + ft)
        for f in fl:
            lb.insert(0, f)
        root.mainloop()


if __name__ == '__main__':
    FileList("py")