import tkinter as tk

root = tk.Tk()


titleLabel = tk.Label(root, text = "PASSWORD GENERATOR", font =("Helvetica",16))
titleLabel.pack()

titleLabel.grid(row = 0, column = 0, columnspan = 1)

output = tk.Text(root, height = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)


word1Label = tk.Label(root, text = "Word1", background = "red", foreground = "blue")
word1Label.grid(row = 2, column = 0)

word2Label = tk.Label(root, text = "word2", background = "red", foreground = "blue")
word2Label.grid(row = 3, column = 0)

word3Label = tk.Label(root, text = "word3")
word3Label.grid(row = 4, column = 0)

ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

btnGo = tk.Button(root, text = "GENERATE")
btnGo.grid(row = 5, column = 1,)


root.mainloop()