# pack.py

import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Pack")
window.geometry("400x600")

# widgets
label1 = ttk.Label(window, text="Label 1", background="red")
label2 = ttk.Label(window, text="Label 2", background="blue")
label3 = ttk.Label(window, text="Label 3", background="green")
button = ttk.Button(window, text="Button")

# layout
# label1.pack(
#     side="top", fill="both", pady=50, padx=50, ipady=50
# )  # side="left|right|top|bottom"
label1.pack(side="top", expand=True, fill="both", padx=10, pady=10)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")


# run
window.mainloop()
