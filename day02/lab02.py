## Fill in the following methods for the class 'Clock'
import random

class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        if self.minutes==0:
            displaymins="00"
        elif self.minutes<10:
            displaymins="0%s"%self.minutes
        else:
            displaymins=str(self.minutes)
        if self.hour==0:
            displayhours="00"
        elif self.hour<10:
            displayhours="0%s"%self.hour
        else:
            displayhours=str(self.hour)
        return "%s:%s" %(displayhours,displaymins)
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        newtime=self.minutes+minutes
        houradd=newtime/60
        newmins=newtime%60
        self.minutes=newmins
        if self.hour+houradd>=24:
            overdays=(self.hour+houradd)/24
            self.hour=self.hour+houradd-(24*overdays)
        else:
            self.hour=self.hour+houradd

    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        if self.minutes-minutes<0 and self.minutes-minutes>-60:
            newtime=60-abs(self.minutes-minutes)
            hoursub=(newtime/60)+1
        elif self.minutes-minutes<-60:
            hoursub=abs((self.minutes-minutes)/60)
            newtime=60-abs(self.minutes-minutes)%60
        else:
            newtime=self.minutes-minutes
            hoursub=newtime/60
        self.minutes=newtime
        if hoursub-self.hour>=24:
            overdays=(hoursub-self.hour)/24
            self.hour=hoursub-self.hour-(24*overdays)
        else:
            self.hour=self.hour-hoursub

    ## Are two times equal?
    def __eq__(self, other):
        if self.minutes==other.minutes and self.hour==other.hour:
            print "TRUE"
        else:
            print "FALSE"
    
    ## Are two times not equal?
    def __ne__(self, other):
        if self.minutes!=other.minutes and self.hour!=other.hour:
            print "TRUE"
        else:
            print "FALSE"

lit=Clock(12,30)
lit-25
print lit


####This is what erin did and is way better
class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return "%02d:%02d" %(self.hour,self.minutes)
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        allmins=self.hour*60+self.minutes+minutes
        leftovermins=allmins%1440
        self.hour=leftovermins/60
        self.minutes=leftovermins%60

    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        self.__add__(-1*minutes)

    ## Are two times equal?
    def __eq__(self, other):
        return self.minutes==other.minutes and self.hour==other.hour
    
    ## Are two times not equal?
    def __ne__(self, other):
        return self.minutes!=other.minutes and self.hour!=other.hour

lit=Clock(12,30)
lit-25
print lit
