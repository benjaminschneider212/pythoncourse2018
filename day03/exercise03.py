## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
	vowellist=["a","e","i","o","u"]
	counter=0
	try:
		for i in range(0,len(word)):
			if word[i] in "%s"%vowellist:
				counter+=1
			else:
				continue
	except TypeError:
		return "That aint a word fool!"
	return counter

