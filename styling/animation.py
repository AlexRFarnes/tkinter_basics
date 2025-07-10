# animation.py

from random import choice

import customtkinter as ctk


class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # Attributes
        self.start_pos = start_pos + 0.05
        self.end_pos = end_pos - 0.01
        self.width = abs(start_pos - end_pos)

        # Animate logic
        self.pos = self.start_pos
        self.toggle = True

        # Layout
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.toggle:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.toggle = False

    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.01
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backward)
        else:
            self.toggle = True


def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, anchor="center")
    window.after(1000, move_btn)

    # comfigure
    # colors = ["red", "orange", "pink", "yellow"]
    # color = choice(colors)
    # button.configure(fg_color=color)


# Dark mode
ctk.set_appearance_mode("dark")

# Window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")

# Animated widget
animated_panel = SlidePanel(window, 1, 0.7)
ctk.CTkLabel(animated_panel, text="Label 1").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkLabel(animated_panel, text="Label 2").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkButton(animated_panel, text="Button", corner_radius=0).pack(
    expand=True, fill="both", pady=10
)
ctk.CTkTextbox(animated_panel, fg_color=("#dbdbdb", "#2b2b2b")).pack(
    expand=True, fill="both", pady=10
)

# Button
button_x = 0.5
button = ctk.CTkButton(window, text="Toggle sidebar", command=animated_panel.animate)
button.place(relx=button_x, rely=0.5, anchor="center")

# Run
window.mainloop()
