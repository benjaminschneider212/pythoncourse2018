#Homework 4

x=[4,7,2,9,3,1,6,8,5]

x=[4,7,2,9,3,1,6,8,5,15,14,13,12,11,10]


import random

from timeit import default_timer as timer

benchmark=[]
for i in range(1,20):
	benchmark.append(1000*i)

selectionsorttimer=[]
bubblesorttimer=[]
quicksorttimer=[]
for i in benchmark:
	tester=[]
	for i in range(0,i):
		tester.append(random.randint(1,20000000000))
	start = timer()
	selectionsort(tester)
	end = timer()
	selectionsorttimer.append(end-start)
	start = timer()
	bubblesort(tester)
	end = timer()
	bubblesorttimer.append(end-start)
	start = timer()
	qsort(tester)
	end = timer()
	quicksorttimer.append(end-start)

def bubblesort(x):
	test=x[:]
	j=len(test)-1
	while j>0:
		for i in range(0,j):
			if test[i]>test[i+1]:
				bigger=test[i]
				smaller=test[i+1]
				test[i+1]=bigger
				test[i]=smaller	
			else:
				pass
		j-=1
	return test

def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

def selectionsort(x):
	newx=x[:]
	output=[]
	while len(newx)>0:
		val=min(newx)
		output.append(val)
		for i in range(0,len(newx)):
			if newx[i]==val:
				newx.pop(i)
				break
			else:
				pass
	return output

x=[4,7,2,9,3,1,6,8,5,15,14,13,12,11,10]

def quicksort(x):
	lower=[]
	upper=[]
	finish=[]
	for i in range(len(x)):
		if i<x[-1]:
			lower.append(i)
		elif i>x[-1]:
			upper.append(i)
		else:
			finish.append(i)
			return finish
	return quicksort(lower)




import matplotlib.pyplot as plt

x = benchmark 
y = selectionsorttimer
z = bubblesorttimer
w = quicksorttimer

# I found this code online and thought it was a really good thing to adapt and I was having trouble with colors on the other one
fig, ax = plt.subplots()
ax.plot(x, y, 'k--', label='Selection Sort')
ax.plot(x, z, 'k:', label='Bubble Sort')
ax.plot(x, w, 'k', label='Quick Sort')

legend = ax.legend(loc='upper left', shadow=True, fontsize='large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.savefig('plot.pdf')


