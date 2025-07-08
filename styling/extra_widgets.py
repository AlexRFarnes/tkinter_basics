# extra_widgets.py

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame

# Window
window = ttk.Window(themename="superhero")
window.title("Extra widgets")


# Scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack()

# Run
window.mainloop()
