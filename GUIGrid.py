import tkinter as tk

root = tk.Tk()

ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid( row = 2, column = 0)

label = tk.Label(root, text = "...")
label.grid(row = 1, column = 0, columnspan = 2)

root. mainloop() 