import tkinter as tk
#Next step:

#Bind a function to the minus and plus button fro goals
#Whne the plus button is hit plrint out plus and when minus button is hit
#print out 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

'''
Theory: this is a 2D list if I want to access Player 4 yellow card count
players[3][4]
'''
players = [
	# [name, goals, assists,fouls,yellow cards, redcards]
	["Player 1",0,0,0,0,0],

	["Player 2",1,1,1,1,1],

	["Player 3",2,2,2,2,2],

	["Player 4",3,3,3,3,3],

	["Player 5",4,4,4,4,4]

]
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
sbtn.grid(row = 7, column = 0, columnspan = 4)


# link function to change dropdown
tkvar.trace('w', change_dropdown)

output = tk.Text(root,  height = 10, width = 50, background = "light grey")
output.grid(row = 0, column = 4, rowspan = 8) 

'''
Setting up output intial display
'''
#Step 1: Loop through rows

for r in range(0, 5, 1): #A
	temp = "" #creates an empty string
	for c in range (0, 6, 1): #B
		print(players[r][c])
		temp = temp + str(players[r][c])+"\t"
	temp = temp + "\n"
	output.insert(tk.END, temp)	
'''
Trace Code
#A r = 0  0 < 5 True
		temp = ""
#B     c = 0 0 < 6 True
		print (players[0][0])
		temp = "" + "Player 1"
#B     c = 1 1 < 6 True
		print (players[0][1])
		temp = "Player 1 "+"0"
#B     c = 2 2 < 6 True
		print (players[0][2])
		temp = "Player 1 0 "+"0"
#B     c = 3 3 < 6 True
		temp = "Player 1 0 0"+"0"
		print (players[0][3])
		temp = "Player 1 0 0 0"+"0"
#B     c = 4 4 < 6 True
		temp = "Player 1 0 0 0 0"+"0"
		print (players[0][4])
		temp = "Player 1 0 0 0 0 0"
#B     c = 5 5 < 6 True
		temp = "Player 1 0 0 0 0 0"
		print (players[0][5])
#B     c = 6 6 < 6 False
#A r = 1 1 < 5 True
#B     c = 0 0 < 6 True
		print (players[1][0])
#B     c = 1 1 < 6 True
		print (players[1][1])
#B     c = 2 2 < 6 True
		print (players[1][2])
#B     c = 3 3 < 6 True
		print (players[1][3])
#B     c = 4 4 < 6 True
		print (players[1][4])
#B     c = 5 5 < 6 True
		print (players[1][5])
#B     c = 6 6 < 6 False

'''

output.config(state = "disabled")





root.mainloop()