print "QUESTION 1"
#QUESTION 1
print ''' We represent time in a way that�s easy for us to understand. However, Python stores it in tuples. These python tuples are made of nine numbers.

Index	Field	Domain of Values
0	Year (4 digits)	Ex.- 1995
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60/61 are leap seconds)
6	Day of Week	0 to 6 (Monday to Sunday)
7	Day of Year	1 to 366 (Julian day)
8	DST	-1,0,1
Leap seconds are added to make up to Earth�s slowing rotation. When DST is 0, it isn�t applied. When it�s 1, it is applied. However, when it is -1, it is up to the library to determine that.
'''

print "QUESTION 2"
#QUESTION 2
import time
t=time.gmtime()
print t
# two methods for time formatting
print time.asctime(t)
print time.ctime(4000)
print time.ctime()


print "QUESTION 3"
#QUESTION 3
import datetime
from datetime import date
d=date.today()
print(d)
print(d.month)

print "QUESTION 4"
#QUESTION 4
print(d.day)

print "QUESTION 5"
#QUESTION 5
s=datetime.date(2045,6,23)
print s
print s.day


print "QUESTION 6"
#QUESTION 6
import time
print time.localtime()

print "QUESTION 7"
#QUESTION 7
import math
w=input("enter a no")
print "factorial of this no is",math.factorial(w)

print "QUESTION 8"
#QUESTION 8
# python 3 syntax
'''
import math
a=input("enter a no")
b=input("enter a no")
print math.gcd(a,b)
'''

print "QUESTION 9"
#QUESTION 9
import os

print os.getcwd()
print os.environ
print os.environ.get('TERM')
































      
