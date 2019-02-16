import random

player = int(raw_input("Lets play! Please enter a numerical value. Rock(1), paper(2), or scissors(3)?"))


computer = random.randint(1,3)

if (computer ==1 and player ==3):
	print("Computer chose rock, Computer wins")
	
elif (computer ==1 and player ==2):
	print("Computer chose rock, player wins")

elif (computer ==1 and player ==1):
	print("Computer chose rock, player and computer tie")
	
elif (computer ==2 and player ==1):
     print("Computer chose paper, computer wins")
	
elif (computer ==2 and player ==3):
	print("Computer chose paper, player wins")
	
elif (computer ==2 and player ==2):
	print("Computer chose paper, player and computer tie")
	
elif (computer ==3 and player ==2):
	print("Computer chose scissors, computer wins")
	
elif (computer ==3 and player ==3):
	print("Computer chose scissors, player and computer tie")
	
elif (computer ==3 and player ==1):
	print("Computer chose scissors, player wins")
	
else:
	print("Please choose a number from 1 to 3")
	