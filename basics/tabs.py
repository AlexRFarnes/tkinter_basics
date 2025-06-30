import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Tab Widget")

# Notebook
notebook = ttk.Notebook(window)

# Tabs
# Tab 1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text="Text in tab 1")
label1.pack()
button1 = ttk.Button(tab1, text="Button in tab 1")
button1.pack()

tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text="Text in tab 2")
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()


# Add tabs to notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

notebook.pack()


# run
window.mainloop()
