# Encapsulation is one of the properties fo OOP which 
# enables us to hide the internal part of object so the 
# developers get benefits as following:
# 1. easy to use an object without knowing what is inside the object
# 2. code change can be easily noticed and measured
# 3' encapsulation provides us the mechanism of restricting 
# the access to some of the object's components
# we can access to the data through special methods: Getters and Setters
class MyClass():
    def setAge(self, num):
         self.age = num
    def getAge(self):
        return self.age

Sara = MyClass()
Sara.setAge(40)
print(Sara.getAge())

Sara.setAge('fourty')
print(Sara.getAge())

# Overriding
# in python when a subclass contains a method that overrides a 
# method of the superclass, you ccan also call the 
# superclass method by calling
# Super(subclass, self) method
# instead of self.method

class skills():
    def __init__(self):
        pass
    def msg(self):
        print('...so, you have the skills!')

class HR():
    def __init__(self):
        super(HR, self).__init__()
    def msg(self):
        print('Good luck another time, you don\'t have the skills needed!')

communication = HR()
communication.msg()