x=input("enter the number")
c=0
if x>1:
 for i in range(2,x):
   if x%i==0:
    c+=1
   else:
     pass
 if c==0:
  print(x,"is prime number")
 else:
   print(x,"is not a prime number")

else:
 print(x,"is not a prime")
