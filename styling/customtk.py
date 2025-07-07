# customtk.py

import customtkinter as ctk

window = ctk.CTk()
window.geometry("400x200")


def update_theme():
    ctk.set_appearance_mode("dark")
    string_var.set(ctk.get_appearance_mode())


button = ctk.CTkButton(
    window,
    text="my button",
    fg_color=("#8800ff", "#b06dea"),
    hover_color=("#5e00af", "#bb95dc"),
    width=100,
    command=update_theme,
)
button.pack(padx=20, pady=20)

string_var = ctk.StringVar(value=ctk.get_appearance_mode())
label = ctk.CTkLabel(
    window,
    text="label",
    fg_color="#0088ff",
    corner_radius=5,
    width=100,
    text_color="#fcfcfc",
    textvariable=string_var,
)
label.pack(padx=20, pady=20)

switch = ctk.CTkSwitch(
    window,
    text="Switch",
    button_color="green",
    fg_color="red",
    progress_color="pink",
    button_hover_color="yellow",
    switch_width=60,
    switch_height=30,
    corner_radius=2,
)
switch.pack()

window.mainloop()
