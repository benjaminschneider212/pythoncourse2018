
class Portfolio(object):
	def __init__(self,client):
		self.client=client
		self.contents = {"cash" : int(0), "mutual funds" : [], "stocks" : []}
		self.log =[]

	def __str__(self):
		return "The portfolio of %s contains: \n %s" %(self.client,self.contents)
	
	def addCash(self,cash,daytime):
		self.contents["cash"]+=cash
		self.log.append("On %s %s added %i in cash to their portfolio. Balance at time of transaction: %i" % (daytime,self.client,cash,self.contents["cash"]))

	def withdrawCash(self,cash,daytime):
		if self.contents["cash"]-cash<0:
			self.log.append("On %s %s attempted to withdraw %i in cash from their portfolio, but were denied due to insufficient funds. Balance at time of transaction: %i" % (daytime,self.client,cash,self.contents["cash"]))
			return "Insufficient funds. Must move around assets to remove %i in cash from account. Current balance: %i" % (cash,self.contents["cash"])
		else:
			self.contents["cash"]-=cash
			self.log.append("On %s %s withdrew %i in cash from their portfolio. Balance at time of transaction: %i" % (daytime,self.client,cash,self.contents["cash"]))

	def history(self):
		return self.log

	def buyStock(self,name,quantity):
		if name.price*quantity>self.contents["cash"]:
			return "Insufficent funds to %i of stock %s. %i needed for this transaction. Current balance: %i"%(quantity,name.stock_name,name.price*quantity,self.contents["cash"])
		else:
			self.contents["cash"]-=name.price*quantity
			self.contents["stock"].append({"%s"%name:[name.price,quantity]})

	def buyMutualFund(self):

	def sellMutualFund(self):

	def sellStock(self):

	def withdrawCash(self):

class Stock(object):
	def __init__(self,price,stock_name):
		self.price=price
		self.stock_name=stock_name

	def __str__(self):
		return "The stock, %s, has a price of %i" %(self.stock,self.price)

class MutualFund(object):
	def __init__(self,stock_name):
		self.stock=stock_name



#test code

ben=Portfolio("Benjamin")
ben.addCash(50, "Aug 8, 3:56pm")
print ben

#ben.withdrawCash(100, "Aug 8, 4:04pm")
#ben.withdrawCash(35, "Aug 8, 4:05pm")
ben.history()
newstock=Stock(30,"APPL")
ben.buyStock(newstock,2)
ben.buyStock(newstock,1)
