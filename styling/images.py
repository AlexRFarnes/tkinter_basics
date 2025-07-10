# images.py

import tkinter as tk
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageTk

# Window
window = tk.Tk()
window.geometry("600x400")
window.title("Images")

# Grid layout
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
window.rowconfigure(0, weight=1)

# Image
image = Image.open("./raccoon.jpg").resize((600, 400))
image_tk = ImageTk.PhotoImage(image)  # Required to work with Tkinter

python_dark = Image.open("python_dark.png").resize((30, 30))
python_dark_tk = ImageTk.PhotoImage(python_dark)

img_ctk = ctk.CTkImage(
    light_image=Image.open("python_light.png"),
    dark_image=Image.open("python_dark.png"),
)

# Widgets
# label = ttk.Label(window, text="Racoon", image=image_tk)
# label.pack()

button_frame = ttk.Frame(window)
button = ttk.Button(
    button_frame, text="   A button", image=python_dark_tk, compound="left"
)
button.pack(pady=10)

button_ctk = ctk.CTkButton(
    button_frame, text="A button", image=img_ctk, compound="left"
)
button_ctk.pack(pady=10)

button_frame.grid(column=0, row=0, sticky="nsew")

# Canvas -> image
canvas = tk.Canvas(
    window, background="black", bd=0, highlightthickness=0, relief="ridge"
)
canvas.grid(column=1, columnspan=3, row=0, sticky="nsew")

canvas.bind("<Configure>", show_full_image)

# Run
window.mainloop()
