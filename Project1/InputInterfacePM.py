import tkinter as tk
#Next step:

#Bind a function to the minus and plus button fro goals
#Whne the plus button is hit plrint out plus and when minus button is hit
#print out 
# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

#Adding functions to plus and minus buttons

def goalsAdd():
	print("Running Goals Add")
	newVal = int(entGoals.get())+1
	entGoals.delete(0, tk.END)
	entGoals.insert(0, newVal)

def goalsSub():
	print("Running Goals Sub")
	newVal = int(entGoals.get())-1
	entGoals.delete(0, tk.END)
	entGoals.insert(0, newVal)


def assistsAdd():
	print("Running Assists Add")
	newVal = int(entAssists.get())+1
	entAssists.delete(0, tk.END)
	entAssists.insert(0, newVal)

def assistsSub():
	print("Running Assists Sub")
	newVal = int(entAssists.get())-1
	entAssists.delete(0, tk.END)
	entAssists.insert(0, newVal)


def foulsAdd():
	print("Running Fouls Add")
	newVal = int(entFouls.get())+1
	entFouls.delete(0, tk.END)
	entFouls.insert(0, newVal)

def foulsSub():
	print("Running Fouls Sub")
	newVal = int(entFouls.get())-1
	entFouls.delete(0, tk.END)
	entFouls.insert(0, newVal)

def YCAdd():
	print("Running YC Add")
	newVal = int(entYC.get())+1
	entYC.delete(0, tk.END)
	entYC.insert(0, newVal)

def YCSub():
	print("Running YC Sub")
	newVal = int(entYC.get())-1
	entYC.delete(0, tk.END)
	entYC.insert(0, newVal)

def RCAdd():
	print("Running RC Add")
	newVal = int(entRC.get())+1
	entRC.delete(0, tk.END)
	entRC.insert(0, newVal)

def RCSub():
	print("Running YC Sub")
	newVal = int(entYC.get())-1
	entYC.delete(0, tk.END)
	entYC.insert(0, newVal)


'''
Theory: this is a 2D list if I want to access Player 4 yellow card count
players[3][4]
'''
players = [
	# [name, goals, assists,fouls,yellow cards, redcards]
	["Player 1",0,0,0,0,0],

	["Player 2",0,0,0,0,0],

	["Player 3",0,0,0,0,0],

	["Player 4",0,0,0,0,0],

	["Player 5",0,0,0,0,0]
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



pbtnGoals = tk.Button(root, text = "+", command=goalsAdd)
pbtnGoals.grid( row = 2, column = 3)




entGoals = tk.Entry(root, width = 2)
entGoals.insert(0,players[0][1])
entGoals.grid(row = 2, column = 2)



nbtnGoals = tk.Button(root, text = "-", command = goalsSub)
nbtnGoals.grid( row = 2, column = 1, sticky = "E")


#Input for assists
labAssists = tk.Label(root, text = "Assist(s)")
labAssists.grid( row = 3, column = 0)


pbtnAssists = tk.Button(root, text = "+", command = assistsAdd)
pbtnAssists.grid( row = 3, column = 3,)

entAssists = tk.Entry(root, width = 2)
entAssists.insert(0,"0")
entAssists.grid(row = 3, column = 2,sticky = "E")

nbtnAssists = tk.Button(root, text = "-", command = assistsSub)
nbtnAssists.grid(row = 3, column = 1, sticky = "E")

#Input for Fouls
labFouls = tk.Label(root, text = "Foul(s)")
labFouls.grid( row = 4, column = 0)


pbtnFouls = tk.Button(root, text = "+", command = foulsAdd)
pbtnFouls.grid( row = 4, column = 3)

entFouls = tk.Entry(root, width = 2)
entFouls.insert(0,"0")
entFouls.grid(row = 4, column = 2)


nbtnFouls = tk.Button(root, text = "-", command = foulsSub)
nbtnFouls.grid(row = 4, column = 1, sticky = "E")

#Input for Yellow Cards
labYC = tk.Label(root, text = "Yellow Card(s)")
labYC.grid( row = 5, column = 0)


pbtnYC = tk.Button(root, text = "+", command = YCAdd)
pbtnYC.grid( row = 5, column = 3)

entYC = tk.Entry(root, width = 2)
entYC.insert(0,"0")
entYC.grid(row = 5, column = 2)


nbtnYC = tk.Button(root, text = "-", command = YCSub)
nbtnYC.grid( row = 5, column =1, sticky = "E")

#Input for Red Cards
labRC = tk.Label(root, text = "Red Card(s)")
labRC.grid( row = 6, column = 0)

pbtnRC = tk.Button(root, text = "+", command = RCAdd)
pbtnRC.grid( row = 6, column = 3)

entRC = tk.Entry(root, width = 2)
entRC.insert(0,"0")
entRC.grid(row = 6, column = 2)

nbtnRC = tk.Button(root, text = "-", command = RCSub)
nbtnRC.grid( row = 6, column = 1, sticky = "E")

output = tk.Text(root,  height = 10, width = 50, background = "light blue")
output.grid(row = 0, column = 4, rowspan = 8) 

'''
Setting up output intial display
'''
#Step 1: Loop through rows

for r in range(0, 5, 1): #A
	#output.delete("1.0", tk.END)
	temp = "" #creates an empty string
	for c in range (0, 6, 1): #B
		print(players[r][c])
		temp = temp + str(players[r][c])+"\t"
	temp = temp + "\n"
	output.insert(tk.END, temp)	


#Save Button


def submit(*args): 
	
	goals = entGoals.get()
	assists = entAssists.get()
	fouls = entFouls.get()
	YC = entYC.get()
	RC = entRC.get() 

	player = tkvar.get()
	if player == 'Player 1':
		output.delete("1.0", "2.0")
		players[0][1] = goals
		players[0][2] = assists
		players[0][3] = fouls
		players[0][4] = YC
		players[0][5] = RC
		#print(players[0][1])
		temp = "" #creates an empty string
		for c in range (0, 6, 1): #B
			print(players[0][c])
			temp = temp + str(players[0][c])+"\t"
		temp = temp + "\n"
		print(temp)
		output.insert('1.0', temp)
	elif player == 'Player 2':
		output.delete("2.0", "3.0")
		players[1][1] = goals
		players[1][2] = assists
		players[1][3] = fouls
		players[1][4] = YC
		players[1][5] = RC
		#print(players[0][1])
		temp = "" #creates an empty string
		for c in range (0, 6, 1): #B
			print(players[0][c])
			temp = temp + str(players[1][c])+"\t"
		temp = temp + "\n"
		print(temp)
		output.insert('2.0', temp)
	elif player == 'Player 3':
		output.delete("3.0", "4.0")
		players[2][1] = goals
		players[2][2] = assists
		players[2][3] = fouls
		players[2][4] = YC
		players[2][5] = RC
		#print(players[0][1])
		temp = "" #creates an empty string
		for c in range (0, 6, 1): #B
			print(players[0][c])
			temp = temp + str(players[2][c])+"\t"
		temp = temp + "\n"
		print(temp)
		output.insert('3.0', temp)
	elif player == 'Player 4':
		output.delete("4.0", "5.0")
		players[3][1] = goals
		players[3][2] = assists
		players[3][3] = fouls
		players[3][4] = YC
		players[3][5] = RC
		#print(players[0][1])
		temp = "" #creates an empty string
		for c in range (0, 6, 1): #B
			print(players[0][c])
			temp = temp + str(players[3][c])+"\t"
		temp = temp + "\n"
		print(temp)
		output.insert('4.0', temp)
	elif player == 'Player 5':
		output.delete("5.0", "6.0")
		players[4][1] = goals
		players[4][2] = assists
		players[4][3] = fouls
		players[4][4] = YC
		players[4][5] = RC
		#print(players[0][1])
		temp = "" #creates an empty string
		for c in range (0, 6, 1): #B
			print(players[0][c])
			temp = temp + str(players[4][c])+"\t"
		temp = temp + "\n"
		print(temp)
		output.insert('5.0', temp)




	#output.insert(tk.INSERT, goals)
	#output.insert(tk.INSERT, assists)
	#output.insert(tk.INSERT, fouls)
	#output.insert(tk.INSERT, YC)
	#output.insert(tk.INSERT, RC)
	"""if sbtn(["text"]) == "Save":
		try:
			var1 = int(entGoals.get())
			print("*")
			var2 = int(entAssist.get())
			print("**")
			var3 = int(entFoul.get())
			print("***")
			var4 = int(entYC.get())
			print("****")
			var5 = int(entRC.get())
			print("*****`")
		

			pList.append(var1)
			pList.append(var2)
			pList.append(var3)
			pList.append(var4)
			pList.append(var5)

		except:
			print("ERROR")

		print(plist)"""

pList=[]

sbtn = tk.Button(root, text = "Save", command = submit)
sbtn.grid(row = 7, column = 0, columnspan = 4)


# link function to change dropdown
tkvar.trace('w', change_dropdown)


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


#output.config(state = "disabled")


root.mainloop()