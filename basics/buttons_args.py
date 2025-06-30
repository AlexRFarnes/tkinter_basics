import tkinter as tk
from tkinter import ttk


def button_func(entry_string):
    print("Button pressed")
    print(entry_string.get())


def outer_func(parameter):
    def inner_func():
        print("Button pressed")
        print(parameter.get())

    return inner_func


window = tk.Tk()
window.title("Buttons with Arguments")
window.geometry("300x200")

entry_string = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(
    window, text="button", command=lambda: button_func(entry_string)
)  # command=outer_func(entry_string)
button.pack()

window.mainloop()
