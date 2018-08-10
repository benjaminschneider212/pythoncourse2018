## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
	vowellist=["a","e","i","o","u"]
	counter=0
	try:
		for letter in word:
			if letter in "%s"%vowellist:
				counter+=1
	except TypeError:
		print "That ain't a word, fool!"
		raise TypeError
	return counter