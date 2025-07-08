# ttkbs.py

# https://ttkbootstrap.readthedocs.io/en/latest/


# from tkinter import ttk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename="superhero")
window.title("ttk bootstrap intro")
window.geometry("400x300")

label = ttk.Label(window, text="Label")
label.pack(pady=10)

button1 = ttk.Button(window, text="Red", bootstyle="danger-outline")  # type: ignore
button1.pack(pady=10)

button2 = ttk.Button(window, text="Warning", bootstyle="warning")  # type: ignore
button2.pack(pady=10)

button3 = ttk.Button(window, text="Green", bootstyle="success")  # type: ignore
button3.pack(pady=10)

# run
window.mainloop()
