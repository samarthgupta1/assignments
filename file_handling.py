

print "QUESTION 1"
#QUESTION 1
fr=open("new.txt","r")
l=fr.readlines()
print l
print len(l)
n=input("enter the no from which ypu want lines")
for i in range(len(l)-n,len(l)):
    print l[i]


print "QUESTION 2"
#QUESTION 2
s=fr.read()
d=s.split()
n=raw_input("enter the word to be counted")
if n in s:
    print s.count(n)


print "QUESTION 3"
#QUESTION 3
a=fr.read()
f=open("second.txt","w")
f.write(a)
f.close()
f=open("second.txt","r")
print f.read()
f.close()
fr.close()


print "QUESTION 4"
#QUESTION 4
fr=open("new.txt","r")
f=open("second.txt","r")
p=fr.readlines()
t=f.readlines()
for i in range(len(p)):
    for j in range(len(t)):
        if(i==j):
            e=str(p[i])+str(t[j])
            print e
f.close()
fr.close()


print "QUESTION 5"
#QUESTION 5
r=[]
p=open("unsorted.txt","w")
f=open("sorted.txt","w")
import random
for i in range(0,10):
    t=random.randint(1,15)
    print t
    r.append(t)

print r
p.writelines(str(r))
p.close()
r.sort()
f.writelines(str(r))
f.close()
p=open("unsorted.txt","r")
o=p.read()
print "unsorted file",o
f=open("sorted.txt","r")
i=f.read()
print "sorted file",i


























