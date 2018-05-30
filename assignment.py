print "QUESTION 1" 
#QUESTION 1
l=[]
n=input("enter no values in a list")
for i in range(1,n):
    val=input("enter a value")
    l.append(val)
print l

print "QUESTION 2"
#QUESTION 2
s=['google','apple','facebook','microsoft','tesla'] 
l.extend(s)
print l

print "QUESTION 3"
#QUESTION 3
w=["object","class","well","object"]
print w.count("object")
print "QUESTION 4"
#QUESTION 4
q=[1,4,2,90,50,45]
q.sort()
print q


print "QUESTION 5"
#QUESTION 5
x=[1,2,3,4]
y=[5,6,7,8,9]
c=[]
c.extend(y)
c.extend(x)
c.sort()
print c

print "QUESTION 6 STACK"
#QUESTION 6 STACK
t=["apple","mango","grape","plum"]
print t
t.append("banana")
print t
t.append("berry")
print t
t.pop()
print t
t.pop()
print t

print "QUESTION 6 QUEUE"
#QUESTION 6 QUEUE
t=["apple","mango","grape","plum"]
print t
t.append("banana")
print t
t.append("berry")
print t
t.pop(0)
print t
t.pop(0)
print t

print "OPTIONAL QUESTION 1"
#OPTIONAL QUESTION 1
v=[]
n=input("enter no values in a list")
for i in range(1,n):
    val=input("enter a value")
    v.append(val)
print v
count1=0
count2=0
for i in v:
    if(i%2==0):
        count1=count1+1
    else:
        count2=count2+1

print "no of even",count1
print "no of odd",count2
