## Fibonacci sequence
## X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
## 1,1,2,3,5,8,....

## Write a for loop, while loop, or function (or all three!) to create a
## list of the first 10 numbers of the fibonacci sequence

#Ben
fib=[]
for i in range(0,10):
	if i==0 or i==1:
		fib.append(1)
	else:
		fib.append(fib[i-1]+fib[i-2])

fib


fib=[]
while len(fib)<11:
	if len(fib)==0 or len(fib)==1:
		fib.append(1)
	else:
		fib.append(fib[-1]+fib[-2])


fib

def fibo(x):
	fib=[]
	for i in range(0,x):
		if i==0 or i==1:
			fib.append(1)
		else:
			fib.append(fib[i-1]+fib[i-2])
	return(fib)

fibo(10)

