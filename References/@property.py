# python @property is a built in decorator used to change our 
# class methods or attributes, so that the user of our 
# class doesn't need to make any change in their code
# example:
class Fruit():
   def __init__(self, name, color):
       self.name = name
       self.color = color
       self.fruitType = self.name + ' has ' + self.color + ' color'

citrus = Fruit('lemon', 'yellow')
print(citrus.name)
print(citrus.color)
print(citrus.fruitType)

citrus.name = 'Orange'
print(citrus.name)
print(citrus.color)
# the name attribute got changed but the sentence that was 
# created by fruitType attribute remained same as it was set 
# during the initialization of the citrus object, but we 
# want to change fruitType when fruit name is updated so 
# we use of python property decorator

class Fruit():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # self.fruitType = self.name + ' has ' + self.color + ' color'
    def fruitType(self):
        return self.name + ' has ' + self.color + ' color'

citrus = Fruit('lemon', 'yellow')
print(citrus.name)
print(citrus.color)
print(citrus.fruitType())

citrus.name = 'Orange'
print(citrus.name)
print(citrus.color)
# it is solved, but we have removed the fruitType attribute from 
# the constuctor and added a method named fruitType.
# So, now in our class there is no attribute named fruitType and 
# we have a method named fruitType()
# and when any user use our class, will be in trouble as they to 
# replace all the attribute fruitType
# Assume we have long code has lots of lines then how extremely 
# dificult it will be for the coder

# we will solve this problem using the property decorator as following

class Fruit():
    def __init__(self, name, color):
        self.name = name
        self.color = color
    @property
    def fruitType(self):
        return self.name + ' has ' + self.color + ' color'

citrus = Fruit('lemon', 'yellow')
print(citrus.name)
print(citrus.color)
print(citrus.fruitType)

citrus.name = 'Orange'
citrus.color = 'orange'
print(citrus.name)
print(citrus.color)
print(citrus.fruitType)