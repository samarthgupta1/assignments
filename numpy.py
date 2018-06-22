
import numpy as np


print "QUESTION 1"
#QUESTION 1
a=np.random.rand(10,1)
print"mean is",np.mean(a)


print "QUESTION 2"
#QUESTION 2
r=np.random.rand(20,1)
print r
print"varience", r.var()
print r.std()


print "QUESTION 3"
#QUESTION 3
w=np.random.rand(10,20)
e=np.random.rand(20,25)
t=np.dot(w,e)
print t
print np.sum(t)


print "QUESTION 4"
#QUESTION 4
A=np.random.rand(10,1)
def func(x):
    return(1/(1+np.exp(-x)))
final= np.apply_along_axis(func,0,A)
print(final)





