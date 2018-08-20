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



stlgroups[0].__dict__.keys()