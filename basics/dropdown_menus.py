import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Combo and Spin")
window.geometry("600x600")

# Comboxbox
items = ["Do Laundry", "Read", "Gym"]
task_string = tk.StringVar(value="Select a task")

combo = ttk.Combobox(window, values=items, textvariable=task_string)
# combo["values"] = items
# combo.configure(values=items)
# combo.config(values=items)
combo.pack()

combo.bind(
    "<<ComboboxSelected>>",
    lambda event: combo_label.config(text=f"Selected task: {task_string.get()}"),
)

combo_label = ttk.Label(window, text="Tasks")
combo_label.pack()

# Spinbox
spin_int = tk.IntVar(value=5)
spin = ttk.Spinbox(
    window,
    from_=1,
    to=10,
    command=lambda: print(spin_int.get()),
    textvariable=spin_int,
)
spin.bind("<<Increment>>", lambda event: print("Up"))
spin.bind("<<Decrement>>", lambda event: print("Down"))
# spin["values"] = (1, 2, 3, 4, 5)
spin.pack()

window.mainloop()
