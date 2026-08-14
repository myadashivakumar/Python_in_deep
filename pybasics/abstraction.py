from abc import ABCMeta,abstractmethod
class BaseClass():
    __metaclass__ = ABCMeta
    @abstractmethod
    def printmethod(self):
       pass

    def function(self):
        pass

""" @abstractmethod
    def printmethod1(self):
        pass
    """


class InClass(BaseClass):
    def printmethod(self):
        print("childclass")
x=InClass()
x.printmethod()
