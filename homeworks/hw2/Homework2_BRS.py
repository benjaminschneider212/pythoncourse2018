#HOMEWORK 2

# • Go to the petition page for each of the petitions.
# • Create a .csv file with the following information for each petition:
# 	– Title
# 	– Published date
# 	– Issues
# 	– Number of signatures

from bs4 import BeautifulSoup
import urllib2
import re
import csv
import wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

with open('homework2.csv', 'wb') as f:
	w = csv.DictWriter(f, fieldnames = ("Title", "Issues", "Pubdate", "Signum"))
	w.writeheader()
	for i in range(0,10):
		if i==0:
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov")
		else:
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov/petitions?page=%s"%i)
		all_html = BeautifulSoup(web_page.read())
		petitions=all_html.find_all("article",{"class":"node node-petition node-promoted node-teaser node-even"})   
		petitionsmore=(all_html.find_all("article",{"class":"node node-petition node-promoted node-teaser node-odd"}))
		for petition in petitions:
			petitionentry={}
			data=petition.a
			websiteext=data["href"]
			petitionentry["Title"]=data.get_text().encode("utf-8")
			internalissues=petition.find_all("h6")
			issueholder=[]
			for issue in internalissues:
				issueholder.append(issue.get_text().encode("utf-8"))
			petitionentry['Issues']=issueholder
			petitionentry['Signum']=petition.find_all("span")[1].get_text().encode("utf-8")
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov%s"%websiteext)
			all_html = BeautifulSoup(web_page.read())
			text=all_html.find_all("h4")[0].get_text().encode("utf-8")
			a=text.find("on")
			petitionentry['Pubdate']=text[a+2:]
			#petitionentry['Pubdate']=all_html.find_all("h4")[0].get_text().encode("utf-8")
			w.writerow(petitionentry)
		for petition in petitionsmore:
			petitionentry={}
			data=petition.a
			websiteext=data["href"]
			petitionentry["Title"]=data.get_text().encode("utf-8")
			internalissues=petition.find_all("h6")
			issueholder=[]
			for issue in internalissues:
				issueholder.append(issue.get_text().encode("utf-8"))
			petitionentry['Issues']=issueholder
			petitionentry['Signum']=petition.find_all("span")[1].get_text().encode("utf-8")
			web_page = urllib2.urlopen("https://petitions.whitehouse.gov%s"%websiteext)
			all_html = BeautifulSoup(web_page.read())
			text=all_html.find_all("h4")[0].get_text().encode("utf-8")
			a=text.find("on")
			petitionentry['Pubdate']=text[a+2:]
			#petitionentry['Pubdate']=all_html.find_all("h4")[0].get_text().encode("utf-8")
			w.writerow(petitionentry)#me