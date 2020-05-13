#Your assignment it to build two televisions by creating sony and samsung objects, 
# which should have the following attributes: model, screen_size, volume, and channel, 
# with the volume and channel being designated as private attributes. You should 
# include a constructor, which will print "A new television has been built!" when 
# a new object is created.
#Create the sony objet by passing the attributes "Bravia", 60, 30, 1, and create the 
# samsung object by passing the attributes "KU6020", 65, 30, 1.
#After you have created the sony and saamsung objects, please print the message "It 
# is a Sony [Bravia] with [60] inch screen", assuming you are printing the sony 
# object with the model attribute set to Brave and the screen_size attribute set 
# to 60, to confirm the models that have been created
#Your next job is to create two methods which will allow the user to change the 
# volume and channels. Using the @property and @nnnnn.setter decorators, where nnnnn is 
# the method name, e.g. volume, create two methods, one for changing the private 
# channel attribute.
#With the volume method, check if the new volume supplied by the user is greater 
# than 80 and, if so, print the message "Volume is too loud!", else set the volume 
# attribute equal to the new volume and print the message "Volume set to: ", followed 
# by the new volume.
#The channel method should check if the channel supplied by the user is greater than 
# 50 and, if so, print the message "Invaild channel number.", else set the channel 
# attribute equal to the new channel and print the message "Channel changed 
# to: ", followed by the new channel number.
#In the main body of your program, immediately after creating the two television 
# objects, carry out the following tasks: Print "Changing the volume on the Sony...", 
# then ask the user to provide a volume setting between 1 and 100 and convert it to 
# an integer; now indirectly call the method that will change the volume by assigning 
# the new volume to the sony volume attribute, like this: sony.volume = vol, where vol 
# is the new volume. Repeat the process for the samsung television object.
#Next, print "Changing the channel on the sony...", then ask the user to provide a 
# channel number between 1 and 100 and convert it to an integer; now indirectly call 
# the method that will change the channel by assigning the new channel to the sony 
# channel attribute, like this: sony.channel = chan, where chan is the new channel 
# number. Repeat the process for the samsung television object.
class televisions(object):
    def __init__(self, model, screen_size, volume, channel):
        self.model = model
        self.screen_size = screen_size
        self.__volume = volume
        self.__channel = channel
        print("\nA new television has been built! ")
    
    @property
    def volume(self):
        return self.__volume
    @property
    def channel(self):
        return self.__channel
    
    @volume.setter
    def volume(self, new_volume):
        if new_volume > 80:
            print("Volume is too loud! ")
        else:
            __volume = new_volume
            print("Volume set to: ", new_volume )
        
    @channel.setter
    def channel(self, new_channel):
        if new_channel > 50:
            print("Invalid channel number! ")
        else:
            __channel = new_channel
            print("Channel changed to: ", new_channel )
        
def main():
    print("Changing the volume on the Sony...")
    new_volume = input("Enter the new volume 1-100: ")
    new_volume = int(new_volume)
    sony.volume = new_volume
    print("Changing the volume on the Samsung...")
    new_volume = input("Enter the new volume 1-100: ")
    new_volume = int(new_volume)
    samsung.volume = new_volume
    print("Changing the channel on the Sony...")
    new_channel = input("Enter the new channel 1-100: ")
    new_channel = int(new_channel)
    sony.channel = new_channel
    print("Changing the channel on the Samsung...")
    new_channel = input("Enter the new channel 1-100: ")
    new_channel = int(new_channel)
    samsung.channel = new_channel
sony = televisions("Bravia", "60", "30", "1")
samsung = televisions("KU6020", "65", "30", "1")
print("It is a Sony", sony.model , "with", sony.screen_size , "inch screen!")

main()