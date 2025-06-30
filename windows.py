import tkinter as tk
from tkinter import ttk

# Window
window = tk.Tk()
window.title("Windows")
# window.geometry("600x400")
# # window.iconbitmap("ibm.ico")

# # window sizes
# window.minsize(200, 100)
# # Window.maxsize(900, 600)
# # window.resizable(True, False)

# # Screen attributes
# print(window.winfo_screenwidth())
# print(window.winfo_screenheight())

# # Window attributes
# window.attributes("-alpha", 0.5)
# # window.attributes("-topmost", True)

# # Security event
# window.bind("<Escape>", lambda event: window.quit())
# # window.attributes("-fullscreen", True)

# # Title bar
# window.overrideredirect(True)
# grip = ttk.Sizegrip(window)
# grip.place(relx=1.0, rely=1.0, anchor="se")

# Exercise
window_width = 900
window_height = 600
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
left = int(screen_width / 2 - window_width / 2)
top = int(screen_height / 2 - window_height / 2)

window.geometry(f"{window_width}x{window_height}+{left}+{top}")

# run
window.mainloop()
