print "QUESTION 1"
#QUESTION 1
import Tkinter as tkinter
d={"sam":2345,"we":34332,"qqw":2434514,"tt":853,"ae":123231,"aew":165723231,"ae":12323134,"ae":12343231,"ae":1326543231,"ae":16576523231,"wtdgv":16575623231,"ewfsdx":12657376231,"erffd":12878763231,"wff":12746563231,"ewgr":1657263231,"ewg":15667756723231,"ewf":123567657231,"ew":123657231,"rgdr":12356231,}
F1 = tkinter.Frame()
s = tkinter.Scrollbar(F1)
L = tkinter.Listbox(F1)

s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
L.pack(side=tkinter.LEFT, fill=tkinter.Y)

s['command'] = L.yview
L['yscrollcommand'] = s.set

for line in d:
    L.insert(tkinter.END,line)
#mylist.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )

F1.pack(side=tkinter.TOP)

F2 = tkinter.Frame()
lab = tkinter.Label()


print "QUESTION 2"
#QUESTION 2
dict2={}
name1=raw_input("Enter the name: ")
mob1=input("Enter mobile number: ")
name2=raw_input("Enter the name: ")
mob2=input("Enter mobile number: ")
dict2[name1]=mob1
dict2[name2]=mob2
print dict2
def insert():
    for line2 in dict2:
        d[line2]=dict2[line2]
        L.insert(tkinter.END,line2)
        print d
insert()
def poll():
    lab.after(200,poll)
    sel= L.curselection()
    if len(sel)>0:
        item=all_items[sel[0]]
        #print d[item]
        lab.config(text=d[item])

all_items=L.get(0,tkinter.END)

x=all_items[0]
print d[x]

  

lab.pack()
#F2.pack(side=tkinter.TOP)
poll()

tkinter.mainloop()
