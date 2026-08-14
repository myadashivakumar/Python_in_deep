class speed:

    def __init__(self):
      self.speed=10
      self.__speed_limit=20   #private variable
      self.distance=900

    def getspeed(self):
       print(s.distance)
       return self.speed


    def setspeedlimit(self,newspeedlimit):
        self.__speed_limit=newspeedlimit

    def getspeedlimit(self):
        return self.__speed_limit
class Overspeed(speed):
    def __init__(self):
     # print(distance)

v = Overspeed()

s=speed()
s.speed=100
s.setspeedlimit(80)
s.__speed_limit=50# no effect
s._distance=67
print(s._distance)
print s.getspeed(),s.getspeedlimit()

