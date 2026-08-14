x=raw_input("enter the string")
d={}
for n in x:
 key=d.keys()
 if n in key:
    d[n]+=1
 else:
  d[n]=1
print d
