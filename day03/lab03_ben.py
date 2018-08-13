import string
## 1. write tests in lab03_tests.py
## 2. then code for the following functions

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int

## make all characters capitalized
def shout(txt):
	try:
		output=txt.upper()
	except TypeError:
		output= "This isnt a string"
	except AttributeError:
		output= "This isnt a string"
	return output


## reverse all characters in string
def reverse(txt):
	try:
		output=txt[::-1]
	except AttributeError:
		output= "This isnt a string"
	except TypeError:
		output="This isnt a string"
	return output


## reverse word order in string
def reversewords(txt):
	try:
		dummy=txt.split()
		output=dummy[::-1]
		output=" ".join(output)
	except TypeError:
		output= "This isnt a string"
	except AttributeError:
		output= "This isnt a string"
	return output


## reverses letters in each word
def reversewordletters(txt):
	try:
		dummy=txt.split()
		output=[]
		for word in dummy:
			output.append(word[::-1])
		output=" ".join(output)
	except TypeError:
		output="This isnt a string"
	except AttributeError:
		output= "This isnt a string"
	return output
	

## change text to piglatin.. google it! 
def piglatin(txt):
	try:
		dummy=txt.split()
		output=[]
		for word in dummy:
			first=word[-0]
			output.append("%s%say"%(word[1:],first))
		output=" ".join(output)
	except TypeError:
		output="This isnt a string"
	except AttributeError:
		output= "This isnt a string"
	return output



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 

string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

for i in string_list:
  	print shout(i)

for i in string_list:
 	print reverse(i)


for i in string_list:
	print reversewords(i)

for i in string_list:
	print reversewordletters(i)
	
for i in string_list:
	print piglatin(i)