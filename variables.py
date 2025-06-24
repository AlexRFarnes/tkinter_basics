import tkinter as tk
from tkinter import ttk


def button_func():
    print(string.get())
    string.set("button pressed")


window = tk.Tk()
window.title("Tkinter Variables")
window.geometry("400x200")

# tkinter variable
string = tk.StringVar()

# label
label = ttk.Label(master=window, text="Text", textvariable=string)
label.pack()

# entry
entry = ttk.Entry(master=window, textvariable=string)
entry.pack()

button = ttk.Button(master=window, text="button", command=button_func)
button.pack()


string_var_2 = tk.StringVar(value="test")

entry_2 = ttk.Entry(master=window, textvariable=string_var_2)
entry_2.pack()

entry_3 = ttk.Entry(master=window, textvariable=string_var_2)
entry_3.pack()

label_2 = ttk.Label(master=window, text="", textvariable=string_var_2)
label_2.pack()

window.mainloop()
