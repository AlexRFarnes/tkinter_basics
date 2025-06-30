import tkinter as tk
from tkinter import ttk

# https://www.pythontutorial.net/tkinter/tkinter-event-binding/


def get_post(event):
    print(f"x: {event.x} y: {event.y}")


window = tk.Tk()
window.title("Events")
window.geometry("600x600")


text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="A button")
button.pack()

# button.bind("<Alt-KeyPress-a>", lambda event: print(event))
# text.bind("<Motion>", get_post)

# window.bind("<KeyPress>", lambda event: print(event.char))

# entry.bind("<FocusIn>", lambda event: print("Entry field was selected"))

text.bind("<Shift-MouseWheel>", lambda event: print("MouseWheel"))


window.mainloop()
