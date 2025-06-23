import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content from the entry
    text = entry.get()
    if text:
        label["text"] = text  # label.configure(text="new text")
        entry["state"] = "disabled"


def reset():
    label["text"] = "Some text"
    entry["state"] = "enabled"
    entry.delete(0, "end")  # clear entry


# window
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry("800x600")

label = ttk.Label(master=window, text="My Label")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="My Button", command=button_func)
button.pack()

reset_button = ttk.Button(master=window, text="Reset", command=reset)
reset_button.pack()


# run
window.mainloop()
