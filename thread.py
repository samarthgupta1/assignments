import time
import threading
from threading import Thread
import math

print "QUESTION 1"
#QUESTION 1
def sleepMe():
    print"Thread is sleeping",threading.currentThread().getName()
    time.sleep(5)
    print"Thread is awake",threading.currentThread().getName()

t=Thread(target=sleepMe,args=())
t.start()


print "QUESTION 2"
#QUESTION 2
for i in range(1,11):
    print i,
    time.sleep(1)


print "QUESTION 3"
#QUESTION 3
l=[1,2,3,4,5]
z=0
for i in l:
    time.sleep(z)
    z=z+2
    print i


print "QUESTION 4"
#QUESTION 4
class factorial(threading.Thread):
     def __init__(self, number):
         threading.Thread.__init__(self)
         self.Number = number

     def run(self):
         print math.factorial(self.Number),"\n"
         



threads = []
while True:
    input_var = int(input("\nnumber:"))
    if input_var < 1:
        break
    thread = factorial(input_var)
    threads += [thread]
    print threads
    thread.start()

for x in threads:
           x.join()
