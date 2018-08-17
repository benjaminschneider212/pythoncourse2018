import re

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

pattern = re.compile(r'[Tt]he\W+')

lit=[]
for line in obama:
 	if pattern.search(line):
		pass
  	else:
		lit.append(line)

# TODO: print lines that contain a word of any length starting with s and ending with e

with open("obama-nh.txt", "r") as f:
	obama = f.readlines()

pattern = re.compile(r'\W+[Ss][a-z]+e\W')
lit=[]
for line in obama:
 	if pattern.search(line):
		lit.append(line)
	elif pattern2.search(line):
		lit.append(line)
  	else:
		pass


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY

date = raw_input("Please enter a date in the format MM.DD.YY: ")

pattern=re.compile(r'(\d*)\.(\d*)\.(\d*)')
search = pattern.search(date)
print "Month: %r \nDay: %r \nYear: %r"%(search.groups(0)[0],search.groups(0)[1],search.groups(0)[2])









