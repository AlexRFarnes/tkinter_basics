import tkinter as tk
from tkinter import ttk


def button_func():
    print("A button was pressed")


def greet():
    print("Hello")


# create a window
window = tk.Tk()
window.title("Windows and Widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# ttk label
my_label = ttk.Label(master=window, text="My label")
my_label.pack()

# ttk button
button = ttk.Button(master=window, text="Button", command=button_func)
button.pack()

# ttk button
my_button = ttk.Button(master=window, text="My Button", command=greet)
my_button.pack()

# run
window.mainloop()
