# functional_widgets.py

import tkinter as tk
from tkinter import ttk


def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master=parent)

    # grid layout
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), weight=1, uniform="a")

    # widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew")
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky="nsew")

    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master=parent)

        # Grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nswe")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nswe")

        self.pack(expand=True, fill="both", padx=10, pady=10)


# Window
window = tk.Tk()
window.title("Widgets and Return")
window.geometry("400x600")

# Widgets
# Segment(window, "Label 1", "Button 1")
# Segment(window, "Label 2", "Button 2")
# Segment(window, "Label 3", "Button 3")
# Segment(window, "Label 4", "Button 4")
# Segment(window, "Label 5", "Button 5")

create_segment(window, "Label 1", "Button 1").pack(
    expand=True, fill="both", padx=10, pady=10
)
create_segment(window, "Label 2", "Button 2").pack(
    expand=True, fill="both", padx=10, pady=10
)
create_segment(window, "Label 3", "Button 3").pack(
    expand=True, fill="both", padx=10, pady=10
)
create_segment(window, "Label 4", "Button 4").pack(
    expand=True, fill="both", padx=10, pady=10
)
create_segment(window, "Label 5", "Button 5").pack(
    expand=True, fill="both", padx=10, pady=10
)

# Run
window.mainloop()
