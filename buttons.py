import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")


# buttons
def button_func():
    print("A basic button")
    print(radio_var.get())


button_string = tk.StringVar(value="A button with string var")
button = ttk.Button(
    window, text="A button", command=button_func, textvariable=button_string
)
button.pack()


# check button
def button_check():
    print(check_var.get())


check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(
    window,
    text="Checkbox",
    command=button_check,
    variable=check_var,
    onvalue=10,
    offvalue=5,
)
check.pack()

# radio buttons
radio_var = tk.StringVar()
radio_1 = ttk.Radiobutton(
    window,
    text="Radio 1",
    variable=radio_var,
    value=1,
    command=lambda: print(radio_var.get()),
)
radio_1.pack()

radio_2 = ttk.Radiobutton(window, text="Radio 2", variable=radio_var, value=2)
radio_2.pack()


# Exercise
def radio_func():
    print(check_bool.get())
    check_bool.set(False)


# data
check_bool = tk.BooleanVar()
radio_str = tk.StringVar()

# widgets
radio_ex_1 = ttk.Radiobutton(
    window, text="Radio A", value="A", variable=radio_str, command=radio_func
)
radio_ex_1.pack()

radio_ex_2 = ttk.Radiobutton(
    window, text="Radio B", value="B", variable=radio_str, command=radio_func
)
radio_ex_2.pack()

check_ex = ttk.Checkbutton(
    window, text="Check", variable=check_bool, command=lambda: print(radio_str.get())
)
check_ex.pack()

window.mainloop()
