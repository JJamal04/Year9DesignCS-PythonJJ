#This approach is called parallel arrays
#One of the challenges is storing the information about the players

players = ["p1","p2","p3","p4"]
goals = [1,3,2,1]

#This code pairs the player with the amount of goals by using the index

for i in range(0, len(players),1):
	print(str(i)+": "+players[i])


#This code give the user a choice to view any of the four players amount of goals 
choice = input("What player do you want to see total goals: ")
choice = int(choice)
print(players[choice] +" has "+str(goals[choice])+" goals this year")