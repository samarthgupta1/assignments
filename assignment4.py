#"TUPLES"
print"TUPLES"
print "QUESTION 1" 
#QUESTION 1
t=()
n=input("enter no values in a tuple")
for i in range(1,n+1):
    val=raw_input("enter a value")
    t=t+(val,)
print t
print len(t)

print "QUESTION 2" 
#QUESTION 2
print max(t)      # maximum
print min(t)      # minimum

print "QUESTION 3" 
#QUESTION 3
p=()
n=input("enter no values in a tuple")
for i in range(1,n+1):
    val=input("enter a value")
    p=p+(val,)
print p
q=1
for z in p:
    q=q*z
print q


# SETS
print"SETS"
print "QUESTION 1" 
#QUESTION 1
s=set()
n=input("enter no values in a set")
for i in range(1,n+1):
    val=input("enter a value")
    s.add(val)
print s
w=set()
e=input("enter no values in a set")
for i in range(1,e+1):
    val=input("enter a value")
    w.add(val)
print w
print s&w       #intersection
r=s-w            #difference
print r
q=s<=w          #comparision
print q
z=s>=w
print z




#DICTIONARIES
print"DICTIONARIES"
print "QUESTION 1" 
#QUESTION 1
d={}
for i in range(10):
    student_name=raw_input("enter the name of student")
    marks=input("enter the marks of student")

    d[student_name]="marks=",marks
print d

print "QUESTION 2" 
#QUESTION 2
s=sorted(d.items(),key=lambda t:t[1])
print s


print "QUESTION 3" 
#QUESTION 3
s="MISSISSIPPI"
d={}
d["M"]=s.count("M")
d["I"]=s.count("I")
d["S"]=s.count("S")
d["P"]=s.count("P")
print sorted(d.items(),key=lambda t:t[1])



















