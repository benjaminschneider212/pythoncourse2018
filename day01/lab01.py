## Trick and explanation of base conversion
## http://www.purplemath.com/modules/base_why.htm

"""convert positive integer to base 2"""
def binarify(num): 
	storage=[]
	while num>0:
		storage.append(str(num%2))
		num/=2
	print "".join(storage[::-1])

"""convert positive integer to a string in any base"""
def int_to_base(num, base):
	storage=[]
	while num>0:
		storage.append(str(num%base))
		num/=base
	print "".join(storage[::-1])

"""take a string-formatted number and its base and return the base-10 integer"""
def base_to_int(string, base):
	string=string[::-1]
	counter=0
	for i in range(0,len(string)):
		counter+=(int(string[i])*base**i)
	return counter

"""add two numbers of different bases and return the sum"""
def flexibase_add(str1, str2, base1, base2):
	return base_to_int(str1,base1)+base_to_int(str2,base2)


"""multiply two numbers of different bases and return the product"""
def flexibase_multiply(str1, str2, base1, base2):
	return base_to_int(str1,base1)*base_to_int(str2,base2)

"""given an integer, return the Roman numeral version"""
def romanify(num):
	final=[]
	while num>1000:
		final.append("M"*(num/1000))
		num-=(num/1000)*1000
	if num-900>=0:
		final.append("CM")
		num-=900
	while num>=500:
		final.append("D")
		num-=500
	if num-400>=0:
		final.append("CD")
		num-=400
	while num>100:
		final.append("C"*(num/100))
		num-=(num/100)*100
	if num-90>=0:
		final.append("XC")
		num-=90
	while num>=50:
		final.append("L")
		num-=50
	if num-40>=0:
		final.append("XL")
		num-=40
	while num>10:
		final.append("X"*(num/10))
		num-=(num/10)*10
	if num-9>=0:
		final.append("IX")
		num-=9
	while num>=5:
		final.append("V")
		num-=5
	if num-4>=0:
		final.append("IV")
		num-=4
	while num>1:
		final.append("I"*(num/1))
		num-=(num/1)*1
	print "".join(final)
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.