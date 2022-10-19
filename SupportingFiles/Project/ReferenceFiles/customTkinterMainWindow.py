# https://github.com/TomSchimansky/CustomTkinter/wiki/CTkOptionMenu

import tkinter
import customtkinter


class App(customtkinter.CTk)
    def __init__(self):
        super().__init__()

        self.geometry(f"{600}x{500}")
        self.title("CTk example")


# Without Variable
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


combobox = customtkinter.CTkOptionMenu(master=app,
                                       values=["option 1", "option 2"],
                                       command=optionmenu_callback)
combobox.pack(padx=20, pady=10)
combobox.set("option 2")  # set initial value

# With Variable
optionmenu_var = customtkinter.StringVar(value="option 2")  # set initial value


def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)


combobox = customtkinter.CTkComboBox(master=app,
                                     values=["option 1", "option 2"],
                                     command=optionmenu_callback,
                                     variable=optionmenu_var)
combobox.pack(padx=20, pady=10)

app = App()
app.mainloop()
