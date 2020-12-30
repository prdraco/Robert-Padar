#Create a new Van object with both model an colour attributes 
# specified in a constructor method, which will (if the model 
# is set to Transit and the colour is set to red) also print 
# "A new red Transit has come off the production line.";
#Instantiate two new oject called Ford and Volkswagen, with 
# the Ford object passing the attributes "Transit" and "red", 
# and the Volkswagen passing the attributes "Transporter" and "blue";
#Create a __str__() method to print the model and color of 
# each object in a structured format, and print both 
# bjects in the main part of the program;
#Print each object's model and colour by directly accessing 
# the attributes using the standard dot notation.
class Van(object):
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour
        print('A new ', self.colour , self.model , ' has come off the production line.')
    def __str__(self):
        rep = "Van object\n"
        rep = "model: " + self.model
        rep += "colour: " + self.colour
        return rep
    def talk(self):
        print("\nThe Van model is ", self.model, "and it\'s colour", self.colour, "\n")
Ford = Van('Transit ' , 'red')
Ford.talk()
Volkswagen = Van('Transporter ' , 'blue')
Volkswagen.talk()
print("Printing Van 1:")
print(Ford)
print("Printing Van 2:")
print(Volkswagen)
print("Directly accessing Van 1's colour:")
print(Ford.colour)
print("Directly accessing Van 2's model:")
print(Volkswagen.model)