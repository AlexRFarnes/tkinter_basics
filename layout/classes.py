import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, title, size):
        # Main setup
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(600, 600)

        # Widgets
        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.menu_button1 = ttk.Button(self, text="Button 1")
        self.menu_button2 = ttk.Button(self, text="Button 2")
        self.menu_button3 = ttk.Button(self, text="Button 3")

        self.menu_slider1 = ttk.Scale(self, orient="vertical")
        self.menu_slider2 = ttk.Scale(self, orient="vertical")

        self.toggle_frame = ttk.Frame(self)
        self.menu_toggle1 = ttk.Checkbutton(self.toggle_frame, text="Check 1")
        self.menu_toggle2 = ttk.Checkbutton(self.toggle_frame, text="Check 2")

        self.entry = ttk.Entry(self)

    def create_layout(self):
        # Grid
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # Widgets layout
        self.menu_button1.grid(row=0, column=0, sticky="nswe", columnspan=2)
        self.menu_button2.grid(row=0, column=2, sticky="nswe")
        self.menu_button3.grid(row=1, column=0, columnspan=3, sticky="nswe")

        self.menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nswe", pady=20)
        self.menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nswe", pady=20)

        # Toggle layout
        self.toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nswe")
        self.menu_toggle1.pack(side="left", expand=True)
        self.menu_toggle2.pack(side="left", expand=True)

        # Entry layout
        self.entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # ttk.Label(self, text="Label", background="red").pack(expand=True, fill="both")
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.entry_frame1 = ttk.Frame(self)
        self.main_label1 = ttk.Label(
            self.entry_frame1, text="label 1", background="red"
        )
        self.main_button1 = ttk.Button(self.entry_frame1, text="Button 1")

        self.entry_frame2 = ttk.Frame(self)
        self.main_label2 = ttk.Label(
            self.entry_frame2, text="label 2", background="blue"
        )
        self.main_button2 = ttk.Button(self.entry_frame2, text="Button 2")

    def create_layout(self):
        self.entry_frame1.pack(expand=True, side="left", fill="both", padx=20, pady=20)
        self.entry_frame2.pack(expand=True, side="left", fill="both", padx=20, pady=20)

        self.main_label1.pack(expand=True, fill="both")
        self.main_button1.pack(expand=True, fill="both", pady=10)

        self.main_label2.pack(expand=True, fill="both")
        self.main_button2.pack(expand=True, fill="both", pady=10)


app = App("Class based app", (600, 600))
