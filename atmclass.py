
class CheckingAccount(object):   #asks the user for their UserID and checks their PIN 
	dict={'jsmith' : '1994', 'rstein': '2010', 'rong' : '1945' , 'annah': '2020'}
	holder={'jsmith' : 'John Smith', 'rstein' : 'Rebecca Stein', 
			'rong': 'Ronald Gray', 'annah' : 'Anna Heller'}
	
	def __init__(self, userID, PIN):
		self.userID= userID
		self.pin= PIN 
		
		if userID not in self.dict.keys():
			raise NameError("The UserID you put in does not exist. Try again.")
		elif (userID in self.dict.keys()) and (PIN!=self.dict[userID]):
			raise ValueError("Your PIN is incorrect. Please try again.") 
			
	def __repr__(self):
		return self.holder[self.userID]
			
		
class Balance(CheckingAccount):
	initial_balance={'jsmith' : 1350, 'rstein' : 200, 'rong': 4000, 'annah':1000}
	updated_balance={'jsmith' : 1350, 'rstein' : 200, 'rong': 4000, 'annah':1000}
	def __init__(self, userID,pin):
		super(Balance,self).__init__(userID, pin)
		
	def initial_balance_(self,userID):
		return self.initial_balance[userID]
	
	def withdraw(self,amount,userID):
		new_balance=float(self.updated_balance[userID])-amount
		if amount>self.updated_balance[userID]:
			print("Insufficient Funds for this withdrawal.", 
				   "Please try again. Current Amount is $" + str(self.updated_balance[userID]))
		else:
			self.updated_balance[userID]=new_balance
			return str(new_balance)

	def current_balance(self,userID):
		return self.updated_balance[userID]
	
	def deposit(self,amount,userID):
		new_balance=(float(self.updated_balance[userID])+amount)
		self.updated_balance[userID]=new_balance
		return str(new_balance)

class Transfer(Balance):
	dict={'jsmith' : '2340', 'rstein': '1984', 'rong' : '1941' , 'annah': '1912'}
	savings_balance={'jsmith' : 30000, 'rstein' : 25000, 'rong': 8500, 'annah':6540}
	def __init__(self,userID, transferpin):
		self.userID=userID
		self.pin=transferpin
		
		if userID not in self.dict.keys():
			raise NameError("The UserID you put in does not exist. Try again.")
		elif (userID in self.dict.keys()) and (transferpin!=self.dict[userID]):
			raise ValueError("Your PIN is incorrect. Please try again.") 
			
	def transfer(self,amount,userID):
		new_balance=float(self.savings_balance[userID])-amount
		if amount>self.savings_balance[userID]:
			print("Insufficient Funds for this transfer.", 
				   "Please try again. Current Amount is $" + str(self.savings_balance[userID]))
		else:
			self.savings_balance[userID]=new_balance
			self.updated_balance[userID]+=amount
			return str(new_balance)

def main():
	print('Welcome to the Automated Transaction Machine')
	userID=str(input('Please input your UserID to access your bank information: '))
	pin=str(input('Please input the corresponding pin to your account: '))
	while True:
		try:
			holder=CheckingAccount(userID,pin)
			break
		except ValueError:
			pin=str(input('Your PIN is incorrect. Please input correct pin to your account: '))	
		except NameError:
			userID=str(input("Your userID is incorrect. Please input correct userID to your account: "))
	print("Welcome "+ str(holder) +"! It is a pleasure serving you today!")
	holder_balance=Balance(userID,pin)
	print("Your initial balance is: $" + str(holder_balance.initial_balance_(userID)))
	try:
		while True:
			response=input("Would you like to withdraw, deposit, check balance, or transfer from another account?: ")
			if "deposit" in response:
				how_much=float(input("How much would you like to deposit?: "))
				holder_balance.deposit(how_much,userID)
				print("Your new balance is now $" + str(holder_balance.updated_balance[userID]))
			elif "withdraw" in response:
				how_much=float(input("How much would you like to withdraw?: "))
				holder_balance.withdraw(how_much,userID)
				print("Your new balance is now $" + str(holder_balance.updated_balance[userID]))
			elif "check" in response:
				print("Your balance is: $"+ str(holder_balance.updated_balance[userID]))
			elif "transfer" in response:
				transfer_pin=str(input("What is your savings account pin: "))
				while True:
					try:
						savings=Transfer(userID,transfer_pin)
						break
					except ValueError:
						transfer_pin=str(input("Your Savings PIN is incorrect. What is your savings account pin: "))
					except NameError:
						userID=str(input("Your UserID is incorrect. Try Again: "))
				transfer_amount=float(input("How much would you like to transfer?: "))
				savings.transfer(transfer_amount,userID)
				print("Your new balance is now $" + str(holder_balance.updated_balance[userID]))
				print("Your savings balance is now $" + str(savings.savings_balance[userID]))
			elif "deposit" not in response or "withdraw" not in response \
			or "check" not in response or "transfer" not in response:
				print("Please try again, I am not understanding.")
			print("If you are done, please hit CTRL-C")		
	except KeyboardInterrupt:
		print("\nBye")


main()	

def graphics():
	dict={'jsmith' : '1994', 'rstein': '2010', 'rong' : '1945' , 'annah': '2020'}
	holder={'jsmith' : 'John Smith', 'rstein' : 'Rebecca Stein', 
			'rong': 'Ronald Gray', 'annah' : 'Anna Heller'}
	from graphics import GraphWin, Rectangle, Entry, Text, Point, Circle 

	win=GraphWin('Automated Transaction Machine', 500,500)
	win.setCoords(0,0,40,40)

	Welcome_message=Text(Point(20,35),'Welcome to the Automated Transaction Machine')

	Rect=Rectangle(Point(2,2), Point(37,37))
	Rect.draw(win)
	Welcome_message.draw(win)
	Pin_value=Text(Point(10,32), '\tPlease input your 1.UserID and 2. PIN below')
	Pin_value.setSize(10)
	Pin_value.draw(win)
	userID=Entry(Point(8,30),8)
	userID.draw(win)
	pin=Entry(Point(8,26),8)
	pin.draw(win)
	win.getMouse()
	x=pin.getText()
	y=userID.getText()
	Pin_value.undraw()
	userID.undraw()
	pin.undraw()
	
	while True:
		try:
			holder=CheckingAccount(y,x)
			break
		except ValueError:
			Incorrect_value=Text(Point(10,32), '\tYour PIN is incorrect. Try Again')
			Incorrect_value.draw(win)
			pin=Entry(Point(8,26),8)
			pin.draw(win)
			win.getMouse()
			x=pin.getText()
			Incorrect_value.undraw()
			pin.undraw()
		except NameError:
			Incorrect_value=Text(Point(10,32), '\tYour UserID is incorrect. Try Again')
			Incorrect_value.draw(win)
			userID=Entry(Point(8,30),8)
			userID.draw(win)
			win.getMouse()
			y=userID.getText()
			Incorrect_value.undraw()
			userID.undraw()
	
	userID.undraw()
	pin.undraw()	
	Welcome=Text(Point(20,25), "Welcome "+ str(holder) + "! It is a pleasure serving you today!")
	Welcome.draw(win)
	win.getMouse()
	Welcome.undraw()
	Option=Text(Point(20,25), 'Would you like to withdraw or deposit')
	Option.draw(win)
	win.getMouse()
		
			
#note : GUI Part is not complete for the ATM Simulation. 
# graphics() 

















