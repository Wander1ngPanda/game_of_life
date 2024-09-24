import tkinter as tk

processing = False

def on_click(event):
    apply_function_to_cell(event.x, event.y)

def on_drag(event):
    global processing
    if not processing:
        processing = True
        apply_function_to_cell(event.x, event.y)
        # Schedule the reset of the processing flag after 100 milliseconds
        canvas.after(200, reset_processing)

def reset_processing():
    global processing
    processing = False

def apply_function_to_cell(x, y):
    print(x, y)

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

root.mainloop()