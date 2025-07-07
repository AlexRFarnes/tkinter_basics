# styling.py

import tkinter as tk
from tkinter import font, ttk

# Window
window = tk.Tk()
window.title("Styling")
window.geometry("400x300")


# Style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use("clam")

style.configure("new.TButton", foreground="green", font=("Garamond", 16))
style.map(
    "new.TButton",
    foreground=[("pressed", "red"), ("disabled", "yellow")],
    background=[("pressed", "green"), ("active", "blue")],
)

# Widgets
label = ttk.Label(
    window,
    text="Label",
    background="black",
    foreground="white",
    font=("Garamond", 16),
)
label.pack()

button = ttk.Button(window, text="Button", style="new.TButton")
button.pack()


style.configure("new.TFrame", background="pink")


frame = ttk.Frame(window, height=200, width=200, style="new.TFrame")
frame.pack()

# Run
window.mainloop()
