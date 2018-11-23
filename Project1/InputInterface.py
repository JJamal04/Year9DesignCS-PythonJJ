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
choices = { 'Player 1','Player 2','Player 3','Player4','Player 5'}
tkvar.set('Player 1') # set the default option
 
popupMenu = tk.OptionMenu(root, tkvar, *choices)
popupMenu.grid(row = 1, column =0, columnspan = 4)

labGoals = tk.Label(root, text = "Goal(s)")
labGoals.grid( row = 2, column = 0)


pbtnGoals = tk.Button(root, text = "+")
pbtnGoals.grid( row = 2, column = 1)

entGoals = tk.Entry(root, width = 2)
entGoals.grid(row = 2, column = 2)


nbtnGoals = tk.Button(root, text = "-")
nbtnGoals.grid( row = 2, column = 3)



# link function to change dropdown
tkvar.trace('w', change_dropdown)
 
 

root.mainloop()