import Tkinter
from Tkinter import *
import sys
import Tkinter as tk

print "QUESTION 1" 
#QUESTION 1
r=Tk()
r.title('FIRST GUI')
z=Label(r,text="HELLO WORLD",width=20,height=5,bg="green")
z.pack()
button=tk.Button(r, text='exit',width=20,activebackground='#ccff00',activeforeground="white",bg="red",command=sys.exit)
button.pack()




print "QUESTION 2" 
#QUESTION 2
def display():
    w=Label(r,text="GUI=graphic user interface", width=20,bg="green")
    w.pack(side=BOTTOM)


b=tk.Button(r, text='start',width=20,activebackground='#ccff00',activeforeground="white",bg="red",command=display)
b.pack()
r.mainloop()


print "QUESTION 3" 
#QUESTION 3
r=Tk()
def display():
    w.configure(text="TEXT CHANGED")
    w.pack(side=BOTTOM)
s=Frame(r,bg="blue")
w=Label(r,text="FIRST TEXT",bg="yellow",width=20)
w.pack(side=BOTTOM)
s.pack()
button=tk.Button(r, text='start',width=20,activebackground='#ccff00',activeforeground="white",bg="red",command=display)
button.pack()
b=tk.Button(r, text='exit',width=20,activebackground='#ccff00',activeforeground="white",bg="blue",command=sys.exit)
b.pack()
r.mainloop()




print "QUESTION 4" 
#QUESTION 4
root = Tk()
 
def returnEntry(arg=None):
	"""Gets the result from Entry and return it to the Label"""
 
	result = myEntry.get()
	resultLabel.config(text=result)
	myEntry.delete(0,END)
 

myEntry = Entry(root, width=20,bg="yellow")
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()
 

enterEntry = Button(root, text= "Enter", command=returnEntry,width=20,bg="red")
enterEntry.pack()

 
resultLabel = Label(root, text = "",bg="blue")
resultLabel.pack()

 
root.mainloop()
