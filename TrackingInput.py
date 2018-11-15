import tkinter as tk

def submit():
	print("Submit pressed")
	list.append(ent.get())
	print(list)
	lab.config(text = "Changed")


#This function will parse a string and
#add a new element to the list for all
#values 



#creates an empty list
list = []

root = tk.Tk()

lab = tk.Label(root, text = "Input Food")
lab.pack()

ent = tk.Entry(root)
ent.pack()

btn = tk.Button(root, text = "Submit", command = submit)
btn.pack()

root.mainloop()