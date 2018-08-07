

class Portfolio(object):
	def __init__(self,client):
		self.client=client
		self.contents = {"cash" : [int(0)], "mutual funds" : [], "stocks" : []}

	def __str__(self):
		print "The portfolio of %s contains: \n %s" %(self.client,self.contents)
	
	def addCash(self,cash):
		self.contents["cash"]+=cash

	def buyStock(self):

	def buyMutualFund(self):

	def sellMutualFund(self):

	def sellStock(self):

	def withdrawCash(self):

	def history(self):

class Stock(object):
	def __init__(self,stock_name):
		self.stock=stock_name

class MutualFund(object):
	def __init__(self,stock_name):
		self.stock=stock_name
