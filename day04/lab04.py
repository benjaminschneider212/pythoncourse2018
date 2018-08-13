## Go to https://polisci.wustl.edu/faculty/specialization
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib2
import csv 

web_address = 'http://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)

soup = BeautifulSoup(web_page.read())
soup.prettify()
mysoup=soup.find_all('a')
minisoup=mysoup[14:58]

mysoupb=soup.find_all('div',{'class':'views-row'})
namelist=[]
for i in range(0,len(mysoupb)):
	namelist.append(str(mysoupb[i].get_text().split("\n")[1]))
titlelist=[]
for i in range(0,len(mysoupb)):
	titlelist.append(str(mysoupb[i].get_text().split("\n")[2]))

mysoupb.findprevious('h3')

namelist.pop(33)
namelist.pop(16)
namelist.pop(7)

titlelist.pop(33)
titlelist.pop(16)
titlelist.pop(7)

extensionlist=[]
for i in range(0,len(minisoup)):
	extensionlist.append(minisoup[i]['href'])

websitelist=[]
for i in range(0,len(extensionlist)):
	websitelist.append('http://polisci.wustl.edu%s'%extensionlist[i])

finalwebsitelist=[]

for line in websitelist:
	if "http://polisci.wustl.edu/" in line:
		finalwebsitelist.append(line.encode("utf-8"))
	else:
		pass

soupysoup=[]
for line in finalwebsitelist:
	web_address = "%s"%line
	web_page = urllib2.urlopen(web_address)
	soup = BeautifulSoup(web_page.read())
	soupysoup.append(soup)


#####*********
emaillist=[]
for i in range(0,len(soupysoup)):
	examine=soupysoup[i].find_all('div')
	string=examine[2].get_text()
	a=string.find("E-mail")
	b = string.find("@",a+7)
	emaillist.append(string[a+8:b+10].encode("utf-8"))

finalemail=[]
for line in emaillist:
	a=string.find("\xa0")
	finalemail.append(line[a+4:])



newish=[]
for i in range(0,len(soupysoup)):
	examine=soupysoup[i].find_all('div')
	newish.append(examine[58].get_text())

examine=soupysoup[1].find_all('div')
for i in range(0,len(examine)):
	print i
	print(examine[i].get_text())

string=examine[2].get_text()

examine[1].get_text()

a=string.find("E-mail")
a = string.find("E-mail:\xa0")
b = string.find("edu",a+5)
output=string[a+5,b+4]

names=[]
for line in namelist:
	names.append(line.strip())

titles=[]
for line in titlelist:
	titles.append(line.strip())

with open('washupolisci.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames = ( "Name","Title","E-mail","Webpage"))
  my_writer.writeheader()
  for i in range(0,len(names)):
  my_writer.writerow({"Name":names[i], "Title":titlelist[i],"E-mail":emaillist[i],"Webpage":finalwebsitelist[i]})

