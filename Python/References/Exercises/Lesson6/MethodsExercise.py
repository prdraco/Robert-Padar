#Create a new Computer class which will include the 
# totalDevices class attribute, initially set to zero;
#Create a static method called displayTotal(), which will 
# print "The total number of units produced is", followed 
# by the totalDevices class attribute;
#Create a constructor method which will receive model and 
# type parameters when an object is created and print "A new 
# Vaio laptop has been manufactured.", where VAIO is the model 
# and laptop is the type passed when a Computer object 
# has been substantiated;
#Create four new objects of your choice, perhaps called sony, 
# dell, hp, and asus, passing appropiate model and type parameters;
#Invoke the static method after the object have been created.
class totalDevices(object):
    total = 0
    @staticmethod
    def displayTotal():
        print("The total number of units produced is", totalDevices.total)
    def __init__(self, model, type):
        self.model = model
        self.type = type
        print("A new",self.model, self.type,"has been manufactured.")
        totalDevices.total += 1

computer1 = totalDevices("Vaio", "laptop")
computer2 = totalDevices("Apple", "laptop")
computer3 = totalDevices("Alienware", "Pc")
computer4 = totalDevices("Dell", "Pc")

totalDevices.displayTotal()
