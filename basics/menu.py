import tkinter as tk
from tkinter import ttk

# docs: https://www.tutorialspoint.com/python/tk_menu.htm

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Menus")

# menu
menu = tk.Menu(window)

# sub menu
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="New", command=lambda: print("New file"))
file_menu.add_command(label="Open", command=lambda: print("Open file"))
file_menu.add_separator()
file_menu.add_command(label="Save", command=lambda: print("Save file"))
menu.add_cascade(label="File", menu=file_menu)

# sub menu
help_menu = tk.Menu(menu, tearoff=False)
help_menu.add_command(label="Help", command=lambda: print(help_check_string.get()))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(
    label="Check", onvalue="on", offvalue="off", variable=help_check_string
)
menu.add_cascade(label="Help", menu=help_menu)

# exercise
exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label="exercise test 1")
menu.add_cascade(label="Exercise", menu=exercise_menu)

exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_sub_menu.add_command(label="some more stuff")
exercise_menu.add_cascade(label="more stuff", menu=exercise_sub_menu)

# Add menu to window
window.configure(menu=menu)

# menu button
menu_button = ttk.Menubutton(window, text="Menu button")
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
button_sub_menu.add_command(label="Entry 1", command=lambda: print("Entry 1"))
menu_button.configure(menu=button_sub_menu)


window.mainloop()
