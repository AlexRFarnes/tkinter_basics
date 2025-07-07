# colors.py
import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Colors")
window.geometry("400x300")


# widgets
ttk.Label(window, background="#ff3333").pack(expand=True, fill="both")
ttk.Label(window, background="#0088ff").pack(expand=True, fill="both")
ttk.Label(window, background="#4fc296").pack(expand=True, fill="both")
ttk.Label(window, background="#880f00").pack(expand=True, fill="both")
ttk.Label(window, background="#000").pack(expand=True, fill="both")
ttk.Label(window, background="#fff").pack(expand=True, fill="both")

# run
window.mainloop()
