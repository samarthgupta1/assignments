print "QUESTION 1"
#QUESTION 1
# ZeroDivisionError
a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print "division by zero"


print "QUESTION 2"
#QUESTION 2
#IndexError
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print"out of index"


print "QUESTION 3"
#QUESTION 3
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    raise

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print "An exception"
    #raise 

print "QUESTION 4"
#QUESTION 4
"""-5.0
a/b result in 0"""


print "QUESTION 5"
#QUESTION5
try:
    import Error
except ImportError:
    print"wrong import"

try:
    l=[1,2,3]
    print l[3]
except IndexError:
    print "out of index"

try:
    s=raw_input("enter an integer")
    print int(s)
except ValueError:
    print "value Error"


print "QUESTION 6"
#QUESTION 6
class ValueTooSmallError(Exception):
    #raised when the age is too small
    pass
while True:
    s=input("enter the age")
    try:
        if s<18:
            raise ValueTooSmallError
        else:
           print "correct age"
           break
        
    except  ValueTooSmallError:
        print"age is small"
         


























    
