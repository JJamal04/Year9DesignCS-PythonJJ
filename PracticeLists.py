List1 = [1, 2, 2, 3, 5, 5, 9]

def avg(somn): 
	tot=0
	for q in somn:
		tot = tot+q
	zavg= tot/len(somn)
	print(zavg)
	return zavg

avg(List1)