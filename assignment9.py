print "QUESTION 1"
#QUESTION 1
import math
class circle():
    def __init__(self,radius):
        self.r=radius
    def area(self):
        a=math.pi*self.r**2
        print a
    def circumference(self):
        w=2*math.pi*self.r
        print w
r=input("enetr the radius")
d=circle(r)
d.area()
d.circumference()


print "QUESTION 2"
#QUESTION 2
class student():
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno
    def display(self):
        print self.n
        print self.r


n=raw_input("enter the name")
r=input("enter roll no")
w=student(n,r)
w.display()


print "QUESTION 3"
#QUESTION 3
class temperature():
    def __init__(self,cel,far):
        self.c=cel
        self.f=far
    def celcius(self):
        s=(self.f-32)*0.55
        print s
    def fahrenheit(self):
        w=(self.c+32)*1.8
        print w


c=input("enter temp in celcius")
f=input("enter the temp in fahrenheit")
x=temperature(c,f)
x.celcius()
x.fahrenheit()



print "QUESTION 4"
#QUESTION 4
class moviedetails():
    def __init__(self):
        self.name="NA"
        self.year=0
        self.rating=0
        self.artist="NA"
    def enter(self):
        self.name=raw_input("enter the name of movie")
        self.year=input("enter year of release")
        self.rating=input("enter the rating out of 10")
        self.artist=raw_input("enter the name of artist")
    def display(self):
        print self.name
        print self.year
        print self.rating
        print self.artist
    def update(self):
        s=raw_input ("enter what u want to update")
        if(s=="name"):
            self.name=raw_input("enter the name of movie")
            self.display()
        elif(s=="artist"):
             self.artist=raw_input("enter the name of artist")
             self.display()
        elif(s=="year"):
            self.year=input("enter year of release")
            self.display()
        elif(s=="rating"):
            self.rating=input("enter the rating out of 10")
            self.display()
        elif(s=="new"):
            self.enter()
            self.display()
        else:
            self.display()

s=moviedetails()
s.enter()
s.display()
s.update()


print "QUESTION 5"
#QUESTION 5
class expenditure():
    def __init__(self,r,s):
        self.exp=r
        self.saving=s
        self.w=0
    def display(self):
        print "expenditure is",self.exp
        print "saving",self.saving
    def salary(self):
        self.w=self.exp+self.saving
    def display2(self):
        print "the salary is",self.w
r=input("enter expenditure")
s=input("enter saving")
x=expenditure(r,s)
x.display()
x.salary()
x.display2()












        


























