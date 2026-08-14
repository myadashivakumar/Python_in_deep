class A:

    def nameof(self):
        print(" class A")

class B:
 name="jhon"
 def function(self):
    print("class B")

class C(A,B):
    def __init__(self):
     print("class c")

    def function1(self):
     print("class C")


C1=C()
print(C1.name)
C1.nameof()
C1.function()
C1.function1()
