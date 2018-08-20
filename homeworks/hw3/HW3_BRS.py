#Homework 3

import imp
meetup = imp.load_source('day05', '../../../meetupkey.py')
api = meetup.client

stlgroups = api.GetFindGroups({"zip" : "63130"})

stlgroups[0].__dict__.keys()

memberlist=[]
for g in stlgroups:
	memberlist.append(g.members)

x=max(memberlist)

for g in stlgroups:
	if g.members==x:
		namesave=g.urlname
	else:
		pass

populargroup=api.GetMembers({"group_urlname" : namesave.encode("utf-8")})

people=populargroup.__dict__["results"]

memberid=[]
for member in people:
	memberid.append(member["id"])

groupnum=[]
for i in memberid:
	mygroups = api.GetGroups({"member_id" : i})
	groupnum.append(mygroups.results)

groupmembership=[]
for i in groupnum:
	groupmembership.append(len(i))

for i in range(len(groupmembership)):
	if len(groupnum[i])==58:
		print i

people[101] #this is our Mr. Popular Alf

groupurls=[]
for g in stlgroups:
	groupurls.append(g.urlname)

activemembers=[]
for i in groupurls:
	group=api.GetMembers({"group_urlname" : i.encode("utf-8")})
	activemembercount=0
	for i in range(len(group.results)):
		if group.results[i]['status']=='active':
			activemembercount+=1
		else:
			pass
	activemembers.append(activemembercount)

maxactive=max(activemembers)

for i in range(len(activemembers)):
	if activemembers[i]==maxactive:
		print stlgroups[i].name

#Looks like there are a lot of groups with 200 active users. Because we can only scrape that many, that is the best I can do













