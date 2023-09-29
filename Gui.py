import tkinter
import customtkinter
from main import *
from tkinter import *


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

def create_new():
    print("Create Button Pressed!")
    check_var = customtkinter.StringVar(value="off")
    checkbox = customtkinter.CTkCheckBox(app, text="", command=checkbox_event,
                                         variable=check_var, onvalue="on", offvalue="off")
    numbers = show_item()
    var = tkinter.StringVar()
    textbox = customtkinter.CTkTextbox(app, width=300, height=30)

    checkbox.grid(row=numbers, column=0, padx=20, pady=10)
    textbox.grid(row=numbers, column=1, pady=10)
    return


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App Geometry
app = customtkinter.CTk()
app.geometry("480x200")
app.title("To-Do App")

#Grid

# configure grid layout (4x4)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure((2, 3), weight=0)
app.grid_rowconfigure((0, 1, 2), weight=1)

# Adding UI Elements, Title

title = customtkinter.CTkLabel(app, text="To-Do List:")
title.grid(row=0, column=0, padx=10, pady=30)

# Extract data from a To-Do text file
app.columnconfigure(0, weight=1)
with open("To-Do File.txt", "r") as f:
    todo = f.readline(10)

#Textbox and Checkbox in oneline.

check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(app, text="", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")

var =tkinter.StringVar()
textbox = customtkinter.CTkTextbox(app, width=300, height=30,xscrollcommand=None, yscrollcommand=None)
textbox.insert("0.0", todo)

checkbox.grid(row=1, column=0, padx=20, pady=10)
textbox.grid(row=1, column=1, pady=10)
#checkbox.pack(side="left", padx=60, pady=10)
#textbox.pack(side="left", pady=10)

#Create Button

button = customtkinter.CTkButton(app, text="Create New Todo", command=create_new)
button.grid(row=10,column=0,padx=10,pady=10)


textbox = customtkinter.CTkTextbox(app)

app.mainloop()