## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
	if x==0:
		return y
	elif y==0:
		return x
	elif x>y:
		x=x%y
		return gcd(x,y)
	elif x<y:
		y=y%x
		return gcd(x,y)

## Exercise 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
	lit=0
	if me<1:
		print "done"
	else:
		for i in range(2,me):
			if me%i==0:
				lit=1
				break
			elif me%i!=0:
				pass
		if lit==1:
			me-=2
		else:
			primes.append(me)
			me-=2
		find_primes(me)
	return primes