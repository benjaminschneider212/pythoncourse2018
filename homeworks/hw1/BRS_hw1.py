import datetime
now = datetime.datetime.now()


class Portfolio(object):
	def __init__(self,client):
		self.client=client
		self.contents = {"cash" : int(0), "mutual funds" : {}, "stocks" : {}}
		self.log =[]

	def __str__(self):
		return "The portfolio of %s contains: \n %s" %(self.client,self.contents)

	def helper(self):
		now = datetime.datetime.now()
		return now.strftime("%B-%d-%Y %H:%M:%S")

	def addCash(self,cash):
		self.contents["cash"]+=cash
		self.log.append("On %s %s added %i in cash to their portfolio. Balance at time of transaction: %i" % (self.helper(),self.client,cash,self.contents["cash"]))

	def withdrawCash(self,cash):
		if self.contents["cash"]-cash<0:
			self.log.append("On %s %s attempted to withdraw %i in cash from their portfolio, but were denied due to insufficient funds. Balance at time of transaction: %i" % (self.helper(),self.client,cash,self.contents["cash"]))
			return "Insufficient funds. Must move around assets to remove %i in cash from account. Current balance: %i" % (cash,self.contents["cash"])
		else:
			self.contents["cash"]-=cash
			self.log.append("On %s %s withdrew %i in cash from their portfolio. Balance at time of transaction: %i" % (self.helper(),self.client,cash,self.contents["cash"]))

	def history(self):
		return self.log

	def buyStock(self,name,quantity):
		if name.price*quantity>self.contents["cash"]:
			self.log.append("On %s, %s attempted to purchase %i unit(s) of the stock %s. %i was needed for this transation. Balance at time of transaction: %i" %(self.helper(),self.client,quantity,name.stock_name,name.price*quantity,self.contents["cash"]))
			return "Insufficent funds to purchase %i of stock %s. %i needed for this transaction. Current balance: %i"%(quantity,name.stock_name,name.price*quantity,self.contents["cash"])
		elif "%s"%name.stock_name in self.contents["stocks"]:
			self.contents["cash"]-=name.price*quantity
			self.contents["stocks"].update({"%s"%name.stock_name:[name.price,quantity+self.contents["stocks"]["%s"%name.stock_name][1]]})
			self.log.append("On %s, %s purchased %i unit(s) of the stock %s for %i. Cash balance after transaction: %i"%(self.helper(),self.client,quantity,name.stock_name,name.price*quantity,self.contents["cash"]))
		else:
			self.contents["cash"]-=name.price*quantity
			self.contents["stocks"].update({"%s"%name.stock_name:[name.price,quantity]})
			self.log.append("On %s, %s purchased %i unit(s) of the stock %s for %i. Cash balance after transaction: %i"%(self.helper(),self.client,quantity,name.stock_name,name.price*quantity,self.contents["cash"]))

	def sellStock(self,name,quantity):
		if self.contents["stocks"]["%s"%name][1]<quantity:
			self.log.append("On %s, %s attempted to sell %i unit(s) of the stock %s. They only had %i unit(s) of the stock." %(self.helper(),self.client,quantity,name,self.contents["stocks"]["%s"%name][1]))
			return "You are attempting to sell more stocks than you have"
		else:
			newprice=random.uniform(self.contents["stocks"]["%s"%name][0]*.5,self.contents["stocks"]["%s"%name][0]*1.5)
			newstock={"%s"%name:[self.contents["stocks"]["%s"%name][0],self.contents["stocks"]["%s"%name][1]-quantity]}
			self.contents["stocks"].update(newstock)
			self.contents["cash"]+=newprice*quantity
			self.log.append("On %s, %s sold %i unit(s) of the stock %s. The original price was %i and the new price was %r. Cash Balance at time of transation: %r" %(self.helper(),self.client,quantity,name,self.contents["stocks"]["%s"%name][0],newprice,self.contents["cash"]))

	def buyMutualFund(self,fund,quantity):
		if quantity>self.contents["cash"]:
			self.log.append("On %s, %s attempted to purchase %i unit(s) of the mutual fund %s. $%i was needed for this transation. Balance at time of transaction: %i" %(self.helper(),self.client,quantity,fund.name,quantity,self.contents["cash"]))
			return "Insufficent funds to purchase %i of mutual fund %s. $%i needed for this transaction. Current balance: %i"%(quantity,fund.name,quantity,self.contents["cash"])
		elif "%s"%fund.name in self.contents["mutual funds"]:
			self.contents["cash"]-=quantity
			self.contents["mutual funds"].update({"%s"%fund.name:[quantity+self.contents["mutual funds"]["%s"%fund.name][0]]})
			self.log.append("On %s, %s purchased %i unit(s) of the mutual fund %s. Cash balance after transaction: %r"%(self.helper(),self.client,quantity,fund.name,self.contents["cash"]))
		else:
			self.contents["cash"]-=quantity
			self.contents["mutual funds"].update({"%s"%fund.name:[quantity]})
			self.log.append("On %s, %s purchased %i unit(s) of the mutual fund %s. Cash balance after transaction: %r"%(self.helper(),self.client,quantity,fund.name,self.contents["cash"]))

	def sellMutualFund(self,name,quantity):
		if self.contents["mutual funds"]["%s"%name][0]<quantity:
			self.log.append("On %s, %s attempted to sell %i unit(s) of the mutual fund %s. They only had %i unit(s) of the stock." %(self.helper(),self.client,quantity,name,self.contents["mutual funds"]["%s"%name][0]))
			return "You are attempting to sell more mutual funds than you have"
		else:
			newprice=random.uniform(.9,1.2)
			newfund={"%s"%name:[self.contents["mutual funds"]["%s"%name][0]-quantity]}
			self.contents["mutual funds"].update(newfund)
			self.contents["cash"]+=newprice*quantity
			self.log.append("On %s, %s sold %i unit(s) of the mutual fund %s. The original price was $1 and the new price was %r. Cash Balance at time of transation: %r" %(self.helper(),self.client,quantity,name,newprice,self.contents["cash"]))


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



