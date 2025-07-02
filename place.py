# grid.py

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Place")
window.geometry("600x400")

# Place
label_1 = ttk.Label(window, text="Label 1", background="red")
label_2 = ttk.Label(window, text="Label 2", background="blue")
label_3 = ttk.Label(window, text="Label 3", background="green")
button_1 = ttk.Button(window, text="Button 1")

# Layout
label_1.place(x=100, y=200, width=300, height=50)
label_2.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.25, relheight=0.5)

# run
window.mainloop()
