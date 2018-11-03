def random_walk_2d(n):
	import random
	import math
	import graphics
	win=graphics.GraphWin("Random Walk Sketch", 200,200)
	win.setCoords(-10,-10,10,10)
	x,y=0,0
	x_values=[]
	y_values=[]
	for i in range(n):  #number of steps stated by user 
		movement=random.randint(1,4)
		if movement==1:
			x+=1
		elif movement==2:
			y+=1
		elif movement==3:
			x-=1
		else:
			y-=1
		x_values.append(x)
		y_values.append(y)
		Point=graphics.Point(x,y)
		Circle=graphics.Circle(Point,.50)
		Circle.draw(win)
		Circle.setFill("red1")
		Circle.setOutline("red1")
		walk=graphics.Text(graphics.Point(x,y),"")
		walk.draw(win)
		walk.setText("Walk {0}".format(i+1))
		walk.setSize(10)
	x_last_value=x_values[len(x_values)-1]
	y_last_value=y_values[len(y_values)-1]
	distance_difference=math.sqrt(((x_last_value-0)**2)+((y_last_value-0)**2))
	win.getMouse()
	return distance_difference 

def main():
	print("Simulation of two dimensional walk")
	number_of_walks=int(input("How many walks should I do? "))
	steps_to_take=int(input("How many steps should I take on each? "))
	average=[]
	for i in range(number_of_walks):
		distance_difference=random_walk_2d(steps_to_take)
		average.append(distance_difference)
	
	print("Average distance from start: ",(sum(average)/len(average)))
	
main()
		
		

		
		