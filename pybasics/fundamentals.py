#ternary operator
x,y=10,20
print("x is greater" if x>y else  "y is greater")


print("************************************************************************")
#variables

class CSStudent:
    stream = 'cse'  # Class Variable or static variable

    def __init__(self, name):
        self.name = name  # Instance Variable or non static variable
        self.stream = "constuor"

    def rollno(self):
        self.roll=768   # Instance Variable or non static variable
        self._sname="xyz"
        self.stream="ece"
a = CSStudent('jhon')
b = CSStudent('mickel')
a.rollno()#invoke
print(a.stream)
print(b.stream)
print(b.name)
print(a.name)

print(a.roll)
print(a._sname)
print(CSStudent.stream)


print("************************************************************************")
#methods

class MyClass:
    def method(self):
        return "instance method called",self
    @classmethod
    def classmethod(cls):
        return "class method called",cls
    @staticmethod
    def staticmethod():
        return "static method called"
obj=MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
print(MyClass.classmethod())
print(MyClass.staticmethod())


print("************************************************************************")
#inheritance
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"

   def parentMethod(self):
      print 'Calling parent method'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent):
   def __init__(self):
      print "Calling child constructor"

   def childMethod(self):
      print 'Calling child method'
c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

print("************************************************************************")

 #multiple inheritance
class A:
    def __init__(self):
        print("class A")
    def nameof(self):
        print("super class")
class B:
 name="jhon"
 def __init__(self):
     print("class b")

class C(A,B):
    def __init__(self):
        print("class c")

C1=C()
print(C1.name)

print(C1.nameof())

print("************************************************************************")

 #multilevel inheritance
class parent1:
    def fun1(self):
        return "parent1"
class parent2(parent1):
    def fun2(self):
      return "parent2"
class child(parent2):
    def fun3(self):
        return "parent3"
obj=child()
print(obj.fun1())
print(obj.fun2())
print(obj.fun3())



print("************************************************************************")

#abstraction
from abc import ABCMeta,abstractmethod
class BaseClass():
    __metaclass__ = ABCMeta
    @abstractmethod
    def printmethod(self):
        pass

class InClass(BaseClass):
    def printmethod(self):
        print("childclass")
x=InClass()
print(x.printmethod())




print("************************************************************************")
#Encapsulation:
class speed:
    def __init__(self):
      self.speed=10
      self.__speed_limit=20#private variable
    def get_speed(self):
       return self.speed
    def get_speed_limit(self):
        return self.__speed_limit
    def set_speed_limit(self,new_speed_limit):
        self.__speed_limit=new_speed_limit

s=speed()
s.speed=100
s.__speed_limit=50# no effect
s.set_speed_limit(80)
print(s.get_speed(),s.get_speed_limit())



print("************************************************************************")
#polymorphism
class Animal:
   # def talk(self):
    #   print("goat ghjkjkk")

    def talk(self,name):
      self.fname=name

      print (self.fname +""+"bow bow")
    def talk(self,name,action):
        self.fname=name
        self.faction=action
        print(self.fname+''+self.faction)
obj=Animal()
#obj.talk()
obj.talk("dog")
obj.talk("cat","meow")





