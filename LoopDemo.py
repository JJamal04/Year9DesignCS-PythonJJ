#A loop structure is a structure that allows us ti run 
#a  setion of code a number of times. It is great for
#when we need to repeat a proccess It is also great 
#when we need to run a pattern.

#There are two broad catagories of loops
# Contitionall loop: This loops as long as something is true
# Counted loop: THis loops a certain number of times.

print("0") 
print("1") 
print("2") 
print("3") 
print("4") 
print("5") 
print("6") 
print("7") 
print("8") 
print("9") 
print("10") 

print("******************************************************")

#The general structire if a counted loops is 
#Count: This is rte variable we use to track the number of 
# 	times a loop runs
#Check: This the boolean (true or false) statement we evaluate 
#	to decide if we keep going
#ChangeL tTHis is the change in the count that happens after each 
#	loop.each

#We use a for i in the range loop
for i in range(0, 6, 1):
	print (i) 
#Hoe would the above loop tin 
#We would reach line 27
#i = 1, 1 < 6, True RUN LOOP
#i = 2, 2 < 6, True RUN LOOP
#i = 3, 3 < 6, True RUN LOOP
#i = 4, 4 < 6, True RUN LOOP
#i = 5, 5 < 6, True RUN LOOP
#i = 6, 6 < 6, False EXIT LOOP AND MOVE ON

print("********************************************************")
print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7, 105, 1):
	print(i)

print("*********************************************************")
print("Write a loop that will print out even numbers from -22 to 134")
for i in range(-22, 134, 2):
	print(i)

print("We can count backwards as wel. Pyhthon 3 will assime the check based on")
print("Print out all bumbers from 101 ro 0 inclusice")
for i in range(3, 0, 1):
	print(i)

print("*********************************************************")
print("Print out all numbers from 101 to 0 inclusive")
for i in range(101, -1, -1):
	print(i)

print("********************PRINTING OOUT STRINGS*************************************")
s="Fish_food"

for i in ragne(0,lens(s),1):
	print(s[i])
print("**************************************************************")
for i in range(len(s) -1,-1,-1);
	print(s[i])

print("**************************************************************")
for i in range(0,lens(s),2)
	print(s[i])
	







