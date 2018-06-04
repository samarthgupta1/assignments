
print "QUESTION 1" 
#QUESTION 1
for i in range(10):
    s=input("enter the no")
    print s


print "QUESTION 2" 
#QUESTION 2
while True:
    print "infinite"



print "QUESTION 3" 
#QUESTION 3
l=[]
n=input("enter no values to be input")
for i in range(n):
    val=input("enter the values")
    l.append(val)
print l

p=[]
for i in l:
    p.append(i**2)

print p



print "QUESTION 4" 
#QUESTION 4
r=[]
s=[]
w=[]
z=[]
r=[23,"acadview",45,4.5,7.8,"python"]
for i in r:
    if type(i)==int:
        z.append(i)
    elif type(i)==str:
        w.append(i)
    else:
        s.append(i)
print"list contain integer",z
print"list contain string",w
print"list contain float",s



print "QUESTION 5" 
#QUESTION 5
e=[]
for a in range(1,101):
    k=0
    if a==1:
        continue
    else:
        for i in range(2,a//2+1):
            if(a%i==0):
                k=k+1
        if(k<=0):
            e.append(a)
print e
        


print "QUESTION 6" 
#QUESTION 6
i="*"
for z in range(1,5):
    print i*z



print "QUESTION 7" 
#QUESTION 7
d={}
n=input("enter no values to be input")
for i in range(n):
    s=raw_input("enter the student name")
    r=input("enter roll no")
    d[s]=r
    
print d

for i in d:
    print "%s %d"%(i,d[i])



print "QUESTION 8" 
#QUESTION 8
l=[]
n=input("enter no values to be input")
for i in range(n):
    val=raw_input("enter the values")
    l.append(val)
print l

m=input("enter how many elements to search")
for i in range(m):
    z=raw_input("enter the element to be searched ")
    if (z in l):
        l.remove(z)
    else:
        print "element not in list"
print l 

