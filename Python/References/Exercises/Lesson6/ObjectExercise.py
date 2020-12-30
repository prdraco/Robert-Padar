#create a Car class with two methods, one called 
# fill_up() and the pther called accelerate();
#The fill_up method should simply print "Insert enough 
# fuel to fill me up." and the accelerate() method 
# should print "Press the accelerator pedal to incrase speed.";
#Instantiate two objects based on the car class 
# called audi and volvo; Access both methods for both instances.
class Car(object):
    def fill_up(self):
        print('Insert enough fuel to fill me up. ')

    def accelerate(self):
        print('Press the accelerator pedal to incrase speed. ')

audi = Car()
volvo = Car()
audi.fill_up()
audi.accelerate()
volvo.fill_up()
volvo.accelerate()