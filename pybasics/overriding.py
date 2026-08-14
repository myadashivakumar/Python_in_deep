
class Father:

    def firstname(self):
     print("father name")
    def lastname(self):
     print("surname")
class Son(Father):
    def firstname(self):
      print("sonsfirstname")

obj=Son()
obj.firstname()
obj.lastname()
