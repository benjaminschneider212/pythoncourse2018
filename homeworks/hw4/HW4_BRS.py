#Homework 4
import random #this is to create random data to sort

from timeit import default_timer as timer #this is to import a timer


def bubblesort(x): #this is my bubble sort function
	test=x[:] #reverses to I can index smaller and smaller each round 
	j=len(test)-1 #this is a baseline and makes sure that I have room in func below (needed to do this, so the original list is not sorted)
	while j>0: #while loop that tracks when the last element is sorted
		for i in range(0,j):
			if test[i]>test[i+1]: #sees if unit it greater than one to its right
				bigger=test[i] #if s0 switches them
				smaller=test[i+1]
				test[i+1]=bigger
				test[i]=smaller	
			else: #if not, goes to next pair
				pass
		j-=1 #takes a digit off while loop
	return test

def qsort(arr): #I did not write this, i found it to put in the graph. This is not me attempting to write the function for extra credit and I couldnt figure out how it worked
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

def selectionsort(x):#beginning of this is same
	newx=x[:]
	output=[]
	while len(newx)>0:#while loop used because I remove lowest option
		val=min(newx) #finds the min value
		output.append(val)#append the lowest to the new list
		for i in range(0,len(newx)):
			if newx[i]==val: #this removes the first iteration of the value so not all of the same value are removed
				newx.pop(i)
				break
			else: #keep looking
				pass
	return output 

benchmark=[] #I am creating the different sizes of data to sort
for i in range(1,20):
	benchmark.append(1000*i) #1000,2000,3000.....


def timerbench(sortmech,data): #look! I am functionalizing. This function times how long it takes to execute
	start = timer()
	sortmech(data)
	end = timer()
	return end-start #returns the time

selectionsorttimer=[] #create a list that holds timers for all of the sorting mechanisms
bubblesorttimer=[]
quicksorttimer=[]
for i in benchmark: #this is a for loop that generates a bunch of datasets of growing size
	tester=[]
	for i in range(0,i):
		tester.append(random.randint(1,20000000000)) #big option for the numers
	selectionsorttimer.append(timerbench(selectionsort,tester)) #uses the function to measure the time of the sort
	bubblesorttimer.append(timerbench(bubblesort,tester))#uses the function to measure the time of the sort
	quicksorttimer.append(timerbench(qsort,tester))#uses the function to measure the time of the sort


import matplotlib.pyplot as plt #import

x = benchmark #the length of data
y = selectionsorttimer #the timer lists
z = bubblesorttimer
w = quicksorttimer

# I found this code online and thought it was a really good thing to adapt and I was having trouble with colors on the other one
fig, ax = plt.subplots()
ax.plot(x, y, 'k--', label='Selection Sort') #creates plots
ax.plot(x, z, 'k:', label='Bubble Sort')
ax.plot(x, w, 'k', label='Quick Sort')

legend = ax.legend(loc='upper left', shadow=True, fontsize='large')

# Put a nicer background color on the legend.
legend.get_frame().set_facecolor('#00FFCC')

plt.savefig('plot.pdf') #I will put this on Git


