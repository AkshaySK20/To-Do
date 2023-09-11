import customtkinter
import customtkinter as tk

def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App Geometry
app = customtkinter.CTk()
app.geometry("480x200")
app.title("To-Do App")

# Adding UI Elements, Title

title = customtkinter.CTkLabel(app, text="To-Do List:")
title.pack(padx=10, pady = 30)

check_var = customtkinter.StringVar(value="off")
checkbox = customtkinter.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(pady = 10)
textbox = customtkinter.CTkTextbox(app)

with open("To-Do File.txt", "r") as file:
    file.readlines()
    text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end

app.mainloop()