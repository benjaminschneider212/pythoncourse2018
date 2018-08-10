import datetime #this is for the date and time of log entries
import random #this is for the uniform distributions
class Portfolio(object):
	def __init__(self,client): #only one necessary argument here and that is the clients name
		self.client=client #this argument is carried over
		self.contents = {"cash" : int(0), "mutual funds" : {}, "stocks" : {}} #this dictionary created by default
		self.log =[] #this list created by default

	def __str__(self): #just an easy print function that is a copy paste sort of string statement
		return "The portfolio of %s contains: \n %s" %(self.client,self.contents)

	def helper(self): #this helper function captures the time and date of the function running for the log.
		now = datetime.datetime.now()
		return now.strftime("%B-%d-%Y %H:%M:%S") #I used this date time format for readability

	def addCash(self,cash): #this is a simple function to add cash to the account and only needs the number f dollars to be added
		self.contents["cash"]+=cash #this updates the cash from the baseline
		self.log.append("On %s %s added $%i in cash to their portfolio. Balance at time of transaction: $%i" % (self.helper(),self.client,cash,self.contents["cash"])) #this is added to the log to track the transaction

	def withdrawCash(self,cash): #exact opposite of above
		if self.contents["cash"]-cash<0: #this statement is so there are no withdraws over the actual amount in the account
			self.log.append("On %s %s attempted to withdraw $%i in cash from their portfolio, but were denied due to insufficient funds. Balance at time of transaction: $%i" % (self.helper(),self.client,cash,self.contents["cash"])) #this is added to the log to track the transaction
			return "Insufficient funds. Must move around assets to remove $%i in cash from account. Current balance: $%i" % (cash,self.contents["cash"]) #helpful statement returned
		else:
			self.contents["cash"]-=cash #now this looks exactly like the above but with a -
			self.log.append("On %s %s withdrew $%i in cash from their portfolio. Balance at time of transaction: $%i" % (self.helper(),self.client,cash,self.contents["cash"])) #this is added to the log to track the transaction

	def history(self): #basic history function, nothing to write home about here
		return self.log #just returns the log and all of the statements appended to it

	def buyStock(self,name,quantity): #this function takes an object of the stock class and the amount of shares wanted
		if name.price*quantity>self.contents["cash"]: #this makes sure they have enough money to purchase the stock
			self.log.append("On %s, %s attempted to purchase %i unit(s) of the stock %s. $%i was needed for this transation. Balance at time of transaction: $%i" %(self.helper(),self.client,quantity,name.stock_name,name.price*quantity,self.contents["cash"])) #this is added to the log to track the transaction
			return "Insufficent funds to purchase %i of stock %s. $%i needed for this transaction. Current balance: $%i"%(quantity,name.stock_name,name.price*quantity,self.contents["cash"]) #helpful statement returned
		elif "%s"%name.stock_name in self.contents["stocks"]: #this checks if they already own some of the stock
			self.contents["cash"]-=name.price*quantity #updates the cash
			self.contents["stocks"].update({"%s"%name.stock_name:[name.price,quantity+self.contents["stocks"]["%s"%name.stock_name][1]]}) #adds the new stocks to the old ones
			self.log.append("On %s, %s purchased %i unit(s) of the stock %s for $%i. Cash balance after transaction: $%i"%(self.helper(),self.client,quantity,name.stock_name,name.price*quantity,self.contents["cash"])) #this is added to the log to track the transaction
		else:
			self.contents["cash"]-=name.price*quantity #updates the cash
			self.contents["stocks"].update({"%s"%name.stock_name:[name.price,quantity]}) #creates a new dictionary entry for the stock
			self.log.append("On %s, %s purchased %i unit(s) of the stock %s for $%i. Cash balance after transaction: $%i"%(self.helper(),self.client,quantity,name.stock_name,name.price*quantity,self.contents["cash"])) #this is added to the log to track the transaction

	def sellStock(self,name,quantity): #to sell you dont need the object of stock class, can just give the name of the stock
		if self.contents["stocks"]["%s"%name][1]<=quantity: #checks if there is enough of that stock to sell
			self.log.append("On %s, %s attempted to sell %i unit(s) of the stock %s. They only had %i unit(s) of the stock." %(self.helper(),self.client,quantity,name,self.contents["stocks"]["%s"%name][1])) #this is added to the log to track the transaction
			return "You are attempting to sell more stocks than you have" #helpful return statement
		else:
			newprice=random.uniform(self.contents["stocks"]["%s"%name][0]*.5,self.contents["stocks"]["%s"%name][0]*1.5) #selects a new price for the stock over the uniform dist
			newstock={"%s"%name:[self.contents["stocks"]["%s"%name][0],self.contents["stocks"]["%s"%name][1]-quantity]} #creates the new entry for the stock with the units taken away fo what was sold
			self.contents["stocks"].update(newstock) #adds it
			self.contents["cash"]+=newprice*quantity #updates the cash
			self.log.append("On %s, %s sold %i unit(s) of the stock %s. The original price was $%i and the new price was $%r. Cash Balance at time of transation: $%r" %(self.helper(),self.client,quantity,name,self.contents["stocks"]["%s"%name][0],newprice,self.contents["cash"])) #this is added to the log to track the transaction

	def buyMutualFund(self,fund,quantity): #this function takes an object of the mutual fund class and the amount of shares wanted
		if quantity>=self.contents["cash"]: #this makes sure they have enough money to purchase the mutual fund
			self.log.append("On %s, %s attempted to purchase %i unit(s) of the mutual fund %s. $%i was needed for this transation. Balance at time of transaction: $%i" %(self.helper(),self.client,quantity,fund.name,quantity,self.contents["cash"])) #this makes sure they have enough money to purchase the stock
			return "Insufficent funds to purchase %i of mutual fund %s. $%i needed for this transaction. Current balance: $%i"%(quantity,fund.name,quantity,self.contents["cash"]) #helpful return statement
		elif "%s"%fund.name in self.contents["mutual funds"]: #this checks if they already own some of the mutual fund
			self.contents["cash"]-=quantity #updates the cash
			self.contents["mutual funds"].update({"%s"%fund.name:[quantity+self.contents["mutual funds"]["%s"%fund.name][0]]}) #Updates the mutual fund entry with the new funds
			self.log.append("On %s, %s purchased %i unit(s) of the mutual fund %s. Cash balance after transaction: $%r"%(self.helper(),self.client,quantity,fund.name,self.contents["cash"])) #this makes sure they have enough money to purchase the stock
		else:
			self.contents["cash"]-=quantity #updates the cash
			self.contents["mutual funds"].update({"%s"%fund.name:[quantity]}) #creates a new dictionary entry for the mutual fund
			self.log.append("On %s, %s purchased %i unit(s) of the mutual fund %s. Cash balance after transaction: $%r"%(self.helper(),self.client,quantity,fund.name,self.contents["cash"]))#this makes sure they have enough money to purchase the stock

	def sellMutualFund(self,name,quantity): #to sell you dont need the object of mutual fund class, can just give the name of the mutual fund
		if self.contents["mutual funds"]["%s"%name][0]<=quantity: #checks if there is enough of that mutual fund to sell
			self.log.append("On %s, %s attempted to sell %i unit(s) of the mutual fund %s. They only had %i unit(s) of the stock." %(self.helper(),self.client,quantity,name,self.contents["mutual funds"]["%s"%name][0]))#this makes sure they have enough money to purchase the stock
			return "You are attempting to sell more mutual funds than you have" #helpful return statement
		else:
			newprice=random.uniform(.9,1.2) #creates the selling price of the mutual fund
			newfund={"%s"%name:[self.contents["mutual funds"]["%s"%name][0]-quantity]} #creates the new dictionary entry for the specific mutual fund
			self.contents["mutual funds"].update(newfund) #puts the new fund in the mutual fund dictionary
			self.contents["cash"]+=newprice*quantity #adds the cash
			self.log.append("On %s, %s sold %i unit(s) of the mutual fund %s. The original price was $1 and the new price was $%r. Cash Balance at time of transation: %r" %(self.helper(),self.client,quantity,name,newprice,self.contents["cash"]))#this makes sure they have enough money to purchase the stock


class Stock(object): #the stock class only has two attributes
	def __init__(self,price,stock_name):
		self.price=price
		self.stock_name=stock_name #the attributes are name and price

	def __str__(self): #I threw in a little print functin but this is pretty uninspired
		return "The stock, %s, has a price of %i" %(self.stock_name,self.price)

class MutualFund(object): #the mutual fund class only has one attribute
	def __init__(self,fund_name):
		self.name=fund_name #the fund_name is the only argument and it is saved as name



#test code

ben=Portfolio("Benjamin")
ben.addCash(50)
ben.withdrawCash(100)
ben.withdrawCash(35)
ben.addCash(1250)
newstock=Stock(30,"APPL")
newstock1=Stock(20,"GOOG")
ben.buyStock(newstock1,2)
ben.buyStock(newstock,6)
ben.buyStock(newstock1,1)
ben.sellStock("APPL",5)
ben.sellStock("GOOG",2)
newfund=MutualFund("Lit")
newfund1=MutualFund("Harambe")
ben.buyMutualFund(newfund,200)
ben.buyMutualFund(newfund,50)
ben.buyMutualFund(newfund1,50)
ben.sellMutualFund("Lit",50)
ben.sellMutualFund("Harambe",11)



