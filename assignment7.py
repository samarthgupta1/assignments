print "QUESTION 1"
#QUESTION 1
r=input("enter the radius")
s=4*3.14*r*r
print "area of sphere",s


print "QUESTION 2"
#QUESTION 2
s=input("enter the no")
def perfect(s):
    count=0
    for i in range(1,s):
        if(s%i==0):
            count=count+i


    if(count==s):
        print "no is perfect",s
    else:
        print "no is not perfect",s

perfect(s)
            
for i in range(1,1000):
    perfect(i)

print "QUESTION 3"
#QUESTION 3
def multip(s,d=1):
    if(d>10):
        return
    else:
        print s*d
        multip(s,d+1)
multip(12)

print "QUESTION 4"
#QUESTION 4
def powers(a,b):
    if (b==1):
        return a
    else:
        return a*powers(a,b-1)

q=powers(2,10)
print q

print "QUESTION 5"
#QUESTION 5
def factorial(w):
    e=1
    for i in range(w,1,-1):
        e=e*i
    print "the factorial is",e
    d={}
    d[w]=e
    print d
w=input("enter a no")
factorial(w)
        
    
