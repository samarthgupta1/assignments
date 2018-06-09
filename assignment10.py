print "QUESTION 1"
#QUESTION 1
class animal():
    def animal_attribute(self):
        print "animal"
class tiger(animal):
    print "tiger"



t=tiger()
t.animal_attribute()


print "QUESTION 2"
#QUESTION 2
#output of following code
#A B
#A B


print "QUESTION 3"
#QUESTION 3
class cop(object):
    def __init__(self):
        self.name="NA"
        self.age=0
        self.work_exp="NA"
        self.des="NA"
    def add(self):
        self.name=raw_input("enter the name of agent")
        self.age=input("enter the age of agent")
        self.work_exp=raw_input("enter the work experience")
        self.des=raw_input("enter the designation")
    def display(self):
        print self.name
        print self.age
        print self.work_exp
        print self.des
    def update(self):
        s=raw_input ("enter what u want to update")
        if(s=="name"):
            self.name=raw_input("enter the name of agent")
            self.display()
        elif(s=="designation"):
             self.des=raw_input("enter the designation")
             self.display()
        elif(s=="age"):
            self.age=input("enter the age of agent")
            self.display()
        elif(s=="workexperience"):
            self.work_exp=input("enter the work experience")
            self.display()
        elif(s=="new"):
            self.enter()
            self.display()
        else:
            self.display()


class mission(cop):
    def add_mission_details(self):
        super(mission,self).display()
        print " Is available for mission"


m=mission()
m.add()
m.update()
m.add_mission_details()


print "QUESTION 4"
#QUESTION 4
class shape():
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        if(self.l==self.b):
            s=self.l*self.l
            print"area of square",s
        else:
            a=self.l*self.b
            print "area of rect",a
class rect(shape):
    print"rectangle"
class square(shape):
    print"square"

r=rect(4,5)
r.area()
s=square(5,5)
s.area()
    
        
        


