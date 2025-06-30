import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("600x400")
window.title("Frames and Parenting")

# frame
frame = ttk.Frame(window, width=200, height=200, borderwidth=1, relief=tk.GROOVE)
frame.pack_propagate(False)
frame.pack(side="left")

# master setting
label = ttk.Label(frame, text="Label in frame")
label.pack()

button = ttk.Button(frame, text="Button in frame")
button.pack()

label_2 = ttk.Label(window, text="Label in window")
label_2.pack(side="right")

# run
window.mainloop()
