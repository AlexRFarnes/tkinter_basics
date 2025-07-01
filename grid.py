# grid.py

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Pack Parenting")
window.geometry("600x400")

# Top frame

label_1 = ttk.Label(window, text="Label 1", background="red")
label_2 = ttk.Label(window, text="Label 2", background="blue")
label_3 = ttk.Label(window, text="Label 3", background="green")
label_4 = ttk.Label(window, text="Label 5", background="orange")
button_1 = ttk.Button(window, text="Button 1")
button_2 = ttk.Button(window, text="Button 2")
entry = ttk.Entry(window)


# define grid
window.columnconfigure((0, 1, 2), weight=1, uniform="a")
# window.columnconfigure(1, weight=1)
# window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=2)
window.rowconfigure((0, 1, 2, 3), weight=1, uniform="a")

# Place grid
label_1.grid(row=0, column=0, sticky="nsew")
label_2.grid(row=1, column=1, rowspan=2, sticky="nsew")
label_3.grid(row=0, column=3, sticky="nsew")
label_4.grid(row=3, column=3, sticky="se")

# run
window.mainloop()
