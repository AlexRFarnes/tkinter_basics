# pack_parenting.py

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Pack Parenting")
window.geometry("400x600")

# Top frame
top_frame = ttk.Frame(window)
label_1 = ttk.Label(top_frame, text="Label 1", background="red")
label_2 = ttk.Label(top_frame, text="Label 2", background="blue")

# Middle widget
label_3 = ttk.Label(window, text="Label 3", background="green")

# Bottom frame
bottom_frame = ttk.Frame(window)
label_4 = ttk.Label(bottom_frame, text="Label 5", background="orange")
button_1 = ttk.Button(bottom_frame, text="Button 1")
button_2 = ttk.Button(bottom_frame, text="Button 2")
# Exercise
bottom_side_frame = ttk.Frame(bottom_frame)
button_3 = ttk.Button(bottom_side_frame, text="Button 3")
button_4 = ttk.Button(bottom_side_frame, text="Button 4")
button_5 = ttk.Button(bottom_side_frame, text="Button 5")


# Top layout
label_1.pack(side="left", fill="both", expand=True)
label_2.pack(side="left", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)

# Middle layout
label_3.pack(expand=True)

# Bottom layout
button_1.pack(side="left", expand=True, fill="both")
label_4.pack(side="left", expand=True, fill="both")
button_2.pack(side="left", expand=True, fill="both")

# Exercise
button_3.pack(expand=True, fill="both")
button_4.pack(expand=True, fill="both")
button_5.pack(expand=True, fill="both")
bottom_side_frame.pack(side="left", expand=True, fill="both")
bottom_frame.pack(expand=True, fill="both", padx=20, pady=20)

# run
window.mainloop()
