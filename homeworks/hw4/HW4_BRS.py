#Homework 4

x=[4,7,2,9,3,1,6,8,5]

x=[4,7,2,9,3,1,6,8,5,15,14,13,12,11,10]


import random

from timeit import default_timer as timer

benchmark=[]
for i in range(1,11):
	benchmark.append(1000*i)

selectionsorttimer=[]
bubblesorttimer=[]
for i in benchmark:
	tester=[]
	for i in range(0,i):
		tester.append(random.randint(1,20000000000))
	start = timer()
	selectionsort(tester)
	end = timer()
	selectionsorttimer.append(end-start)
for i in benchmark:
	tester=[]
	for i in range(0,i):
		tester.append(random.randint(1,20000000000))
	start = timer()
	sorter(tester)
	end = timer()
	bubblesorttimer.append(end-start)

def sorter(x):
	j=len(x)-1
	while j>0:
		for i in range(0,j):
			if x[i]>x[i+1]:
				bigger=x[i]
				smaller=x[i+1]
				x[i+1]=bigger
				x[i]=smaller	
			else:
				pass
		j-=1
	return x

def selectionsort(x):
	newx=[]
	while len(x)>0:
		val=min(x)
		newx.append(val)
		for i in range(0,len(x)):
			if x[i]==val:
				x.pop(i)
				break
			else:
				pass
	return newx

