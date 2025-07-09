# animation.py

import customtkinter as ctk

# Dark mode
ctk.set_appearance_mode("dark")

# Window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")


# Button
button_x = 0.5
button = ctk.CTkButton(window, text="Toggle sidebar")
button.place(relx=button_x, rely=0.5, anchor="center")

# Run
window.mainloop()
