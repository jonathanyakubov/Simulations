def craps():
	print("Welcome, you are going to play a games of craps.")
	number_of_games=int(input("How many games do you want to play? "))
	
	return number_of_games
	
def roll():
	import random
	number_of_games=craps()
	game=0
	win=0
	while game<number_of_games:
		die1=random.randint(1,6)
		die2=random.randint(1,6)
		roll=die1 + die2
		if roll in [2,3,12]:  #loss
			game+=1
		elif roll in [7,11]:   #win 
			game+=1
			win+=1
		else: 
			roll_again=0 #initialize 
			while True:
				die_1=random.randint(1,6)
				die_2=random.randint(1,6)
				roll_again=die_1+die_2
				if roll_again==roll:
					game+=1
					win+=1 
					break
				elif roll_again==7:
					game+=1
					break
					
	
	print(game,win)
	return game,win
			
def calculations():
	wins=[]
	games=[]
	game,win=roll()
	wins.append(win)
	games.append(game)
	total_wins=sum(wins)
	total_games=sum(games)
	print(total_wins)
	print(total_games)
	probability=(total_wins/total_games)					
	print("The estimated probability of winning is ", probability)
		

calculations()
			
			
	
			
		