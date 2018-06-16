import re

emails = "zuck26@facebook.com"
e="page33@google.com"
p="jeff42@amazon.com"
regenex=r"([a-z]+\d+)@([a-z]+).([a-z]+)"
m= re.match( regenex,p, re.M|re.I)
w= re.match( regenex,e, re.M|re.I)
a= re.match( regenex,emails, re.M|re.I)

t=()
t1=()
t2=()

q=t+(m.group(1),)+(m.group(2),)+(m.group(3),)
c=t1+(w.group(1),)+(w.group(2),)+(w.group(3),)
v=t2+(a.group(1),)+(a.group(2),)+(a.group(3),)


l=[]
l.append(q)
l.append(c)
l.append(v)
print "desired output =",l

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
regenex=r"[bBa-z]+"
matches = re.findall(regenex,text)
f=[]
for i in matches:
    if(i[0]=="B"or i[0]=="b"):
        f.append(i)
    else:
        pass
print f


sentence = "A,very very;irregular_sentence"
num = re.sub(r',', " ", sentence)
b=re.sub(r'_'," ",num)
y=re.sub(r';'," ",b)
print y



tweet = 'Good advice!RT@TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'
num = re.sub(r'@[]a-zA-z]+:', " ", tweet)
a=re.sub(r"http.*"," ",num)
w=re.sub(r"RT","",a)
i=re.sub(r"!","",w)
print i

















