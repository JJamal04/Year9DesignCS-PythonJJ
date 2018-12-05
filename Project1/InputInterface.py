import tkinter as tk

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )


root = tk.Tk()
root.title("Player")


titleLabel = tk.Label(root, text = "Input Statistics", font =("Helvetica",16))
titleLabel.grid(row = 0, column = 0, columnspan = 4)

  
# Create a Tkinter variable
tkvar = tk.StringVar(root)
 
# Dictionary with options
choices = { 'Player 1','Player 2','Player 3','Player 4','Player 5'}
tkvar.set('Player 1') # set the default option
 
popupMenu = tk.OptionMenu(root, tkvar, *choices)
popupMenu.grid(row = 1, column =0, columnspan = 4)


#Input for goals
labGoals = tk.Label(root, text = "Goal(s)")
labGoals.grid( row = 2, column = 0)


pbtnGoals = tk.Button(root, text = "+")
pbtnGoals.grid( row = 2, column = 3)

entGoals = tk.Entry(root, width = 2)
entGoals.grid(row = 2, column = 2)


nbtnGoals = tk.Button(root, text = "-")

nbtnGoals.grid( row = 2, column = 1, sticky = "E")


#Input for assists
labGoals = tk.Label(root, text = "Assist(s)")
labGoals.grid( row = 3, column = 0)


pbtnGoals = tk.Button(root, text = "+")
pbtnGoals.grid( row = 3, column = 3)

entGoals = tk.Entry(root, width = 2)
entGoals.grid(row = 3, column = 2,sticky = "E")


nbtnGoals = tk.Button(root, text = "-")
nbtnGoals.grid( row = 3, column = 1, sticky = "E")

#Input for Fouls
labGoals = tk.Label(root, text = "Foul(s)")
labGoals.grid( row = 4, column = 0)


pbtnGoals = tk.Button(root, text = "+")
pbtnGoals.grid( row = 4, column = 3)

entGoals = tk.Entry(root, width = 2)
entGoals.grid(row = 4, column = 2)


nbtnGoals = tk.Button(root, text = "-")
nbtnGoals.grid( row = 4, column = 1, sticky = "E")

#Input for Yellow Cards
labGoals = tk.Label(root, text = "Yellow Card(s)")
labGoals.grid( row = 5, column = 0)


pbtnGoals = tk.Button(root, text = "+")
pbtnGoals.grid( row = 5, column = 3)

entGoals = tk.Entry(root, width = 2)
entGoals.grid(row = 5, column = 2)


nbtnGoals = tk.Button(root, text = "-")
nbtnGoals.grid( row = 5, column =1, sticky = "E")

#Input for Red Cards
labGoals = tk.Label(root, text = "Red Card(s)")
labGoals.grid( row = 6, column = 0)


pbtnGoals = tk.Button(root, text = "+")
pbtnGoals.grid( row = 6, column = 3)

entGoals = tk.Entry(root, width = 2)
entGoals.grid(row = 6, column = 2)

nbtnGoals = tk.Button(root, text = "-")
nbtnGoals.grid( row = 6, column = 1, sticky = "E")


#Save Button
sbtn = tk.Button(root, text = "Save")
sbtn.grid(row = , column = 0, columnspan = 4)

# link function to change dropdown
tkvar.trace('w', change_dropdown)
 

 

root.mainloop()