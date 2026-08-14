class parent1:
    name="jhon"
    def fun1(self):
        return "parent1"
class parent2(parent1):
    name1 = "mickel"
    def fun2(self):
      return "parent2"
class child(parent2):
    def fun3(self):
        return "parent3"

obj=child()
print(obj.fun1())
print(obj.fun2())
print(obj.fun3())
print obj.name
print obj.name1

