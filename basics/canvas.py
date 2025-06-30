import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Canvas")
window.geometry("600x400")

canvas = tk.Canvas(
    window,
    bg="white",
)
canvas.pack()

# canvas.create_rectangle((50, 20, 100, 100), fill="red", width=3, outline="green")
# canvas.create_line((10, 10, 150, 120), fill="blue", width=3)
# canvas.create_oval((150, 150, 250, 250), fill="green")
# canvas.create_arc((150, 150, 250, 250), fill="yellow", start=90, extent=90)
# canvas.create_polygon((120, 150, 150, 150, 200, 50, 120, 0))


# canvas.create_text((100, 100), text="This is some text")

# canvas.create_window(
#     (150, 100), window=ttk.Button(window, text="This is text in a canvas.")
# )


brush_size = 4


def draw_line(event):
    x0 = event.x - brush_size / 2
    y0 = event.y - brush_size / 2
    x1 = event.x + brush_size / 2
    y1 = event.y + brush_size / 2
    canvas.create_oval(x0, y0, x1, y1, width=brush_size, fill="black")


def width_adjust(event):
    global brush_size

    if event.num == 4:
        brush_size += 1
    else:
        brush_size -= 1

    brush_size = max(1, min(brush_size, 20))


canvas.bind("<Shift-Motion>", lambda event: draw_line(event))
canvas.bind("<Button-4>", width_adjust)
canvas.bind("<Button-5>", width_adjust)

window.mainloop()
