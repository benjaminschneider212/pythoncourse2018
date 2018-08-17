#HOMEWORK 2 Benjmain Schneider

# • Go to the petition page for each of the petitions.
# • Create a .csv file with the following information for each petition:
# 	– Title
# 	– Published date
# 	– Issues
# 	– Number of signatures

#import the packages
from bs4 import BeautifulSoup
import urllib2
import re
import csv
import wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context #had to do this being urlopen wasnt being kind

with open('homework2.csv', 'wb') as f: #gonna write thatcsv
	w = csv.DictWriter(f, fieldnames = ("Title", "Issues", "Pubdate", "Signum")) #set up the csv fields
	w.writeheader() #set this up to write the csv
	for i in range(0,10): #this is a for loop to get everything out of the pages
		if i==0:
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov") #gets the initial page
		else:
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov/petitions?page=%s"%i) #gets any outside pages
		all_html = BeautifulSoup(web_page.read()) #gets all of the base code
		petitions=all_html.find_all("article",{"class":"node node-petition node-promoted node-teaser node-even"})#I had to get the pbservations on the left and right side separately
		petitionsmore=(all_html.find_all("article",{"class":"node node-petition node-promoted node-teaser node-odd"}))
		for petition in petitions: #loop for even entries
			petitionentry={} #empty observation
			data=petition.a #gets all of the a tags
			websiteext=data["href"] #gets the url of the indidivual page
			petitionentry["Title"]=data.get_text().encode("utf-8") #gets the title
			internalissues=petition.find_all("h6")#gets the issue code
			issueholder=[] #empty
			for issue in internalissues:#Loop to extract all of the issues
				issueholder.append(issue.get_text().encode("utf-8"))
			petitionentry['Issues']=issueholder #imports all of the issues
			petitionentry['Signum']=petition.find_all("span")[1].get_text().encode("utf-8")#snatches the signature number
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov%s"%websiteext) #goes to the individual page
			all_html = BeautifulSoup(web_page.read())
			text=all_html.find_all("h4")[0].get_text().encode("utf-8") #the text for the date
			a=text.find("on") #reference point for when the date started
			petitionentry['Pubdate']=text[a+2:]#took the publish date out
			w.writerow(petitionentry)#This wrote the new entry
		for petition in petitionsmore: #loop for odd entries
			petitionentry={} #empty entry
			data=petition.a #gets all of the a tags
			websiteext=data["href"] #url of individual page
			petitionentry["Title"]=data.get_text().encode("utf-8") #gtes the title
			internalissues=petition.find_all("h6") #gets the issue code
			issueholder=[] #empty
			for issue in internalissues: #Loop to extract all of the issues
				issueholder.append(issue.get_text().encode("utf-8"))
			petitionentry['Issues']=issueholder#imports all of the issues
			petitionentry['Signum']=petition.find_all("span")[1].get_text().encode("utf-8") #snatches the signature number
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov%s"%websiteext) #goes to the individual page
			all_html = BeautifulSoup(web_page.read())
			text=all_html.find_all("h4")[0].get_text().encode("utf-8") #the text for the date
			a=text.find("on") #reference point for when the date started
			petitionentry['Pubdate']=text[a+2:]#took the publish date out
			w.writerow(petitionentry)#This wrote the new entry


