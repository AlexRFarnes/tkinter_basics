import tkinter as tk
from random import choice
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Treeview")

# data
first_names = [
    "Bob",
    "Maria",
    "Alex",
    "James",
    "Susan",
    "Henry",
    "Lisa",
    "Anna",
    "Lisa",
]
last_names = [
    "Smith",
    "Brown",
    "Wilson",
    "Thomson",
    "Taylor",
    "Walker",
    "Clark",
]


# treeview
table = ttk.Treeview(window, columns=("first", "last", "email"), show="headings")
table.heading("first", text="First Name")
table.heading("last", text="Last Name")
table.heading("email", text="Email")
table.pack()

for i in range(100):
    first_name = choice(first_names)
    last_name = choice(last_names)
    email = first_name + last_name + "@gmail.com"
    table.insert(parent="", index=i, values=(first_name, last_name, email))

window.mainloop()
