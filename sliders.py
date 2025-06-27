import tkinter as tk
from tkinter import scrolledtext, ttk

window = tk.Tk()
window.title("Sliders")
window.geometry("400x200")

# slider
scale_int = tk.IntVar(value=5)
scale = ttk.Scale(
    window,
    command=lambda _: print(scale_int.get()),
    from_=0,
    to=10,
    length=200,
    orient="horizontal",  # "vertical"
    variable=scale_int,
)
scale.pack()

# progress bar
progress = ttk.Progressbar(
    window,
    variable=scale_int,
    maximum=10,
    mode="determinate",  # indeterminate,
    length=100,
)
progress.pack()

# progress.start(1000) # miliseconds
# progress.stop()

scroll_text = scrolledtext.ScrolledText(window, width=25, height=5)
scroll_text.pack()

window.mainloop()
