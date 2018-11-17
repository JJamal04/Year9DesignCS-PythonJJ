import tkinter as tk

root = tk.Tk()
root.title("GUI Text")
text1 = tk.Text(root, height=10, width=10)

text1.config(state="normal")
text1.insert(tk.INSERT,"Line 1\n")
text1.insert(tk.INSERT,"Line 2")
text1.config(state="disabled")

text1.pack()

root.mainloop() 