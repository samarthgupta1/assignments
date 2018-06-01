print "QUESTION 1"
#QUESTION 1
n=input("enter the year")
if (n%4==0 or n%100==0):
    print "year is leap year"
else:
    print "year is not leap year"

print "QUESTION 2"
#QUESTION 2
l=input("enter the length")
b=input("enter the breadth")
if l==b:
    print "this is square"
else:
    print "this is rectangle"

print "QUESTION 3"
#QUESTION 3
w=input("enter the age of first person ")
a=input("enter the age of second person")
s=input("enter the age of third person")
print max(w,a,s),"this person  is oldest"
print min(w,a,s),"this person is youngest"

print "QUESTION 4"
#QUESTION 4
age= input("enter the age of person")
sex=raw_input("enter the sex of person M or F")
marital_status=raw_input("enter your marital status Y or N")
if sex=="F":
    print "she will work in urban areas"
elif sex=="M"and age>=20 and age<=40:
    print "he will work in any areas"
elif sex=="M"and age>=40 and age<=60:
    print "he will work in urban areas"
else:
    print "ERROR"

print "QUESTION 5"
#QUESTION 5
t=input("enter no of quantity purchased")
s=t*100
if s>=1000:
    print "you get a discount of 10%"
    print "your total cost is= Rs",s-s*0.1
else:
    print"no discount"
    print "your total cost is= Rs",s
