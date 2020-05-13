#write a Python script to include a function called happyBirthday(), 
# which will print "Happy Borthday!" when called from the main body. 
# Create another function called notYourBirthday(), which will print 
# "It's not your birthday, but have a good day!" when called 
# from the main body.
#The main body should ask the user "Is it your birthday today?" and, 
# if the answer is "Y" or "y", call the happyBirthday() function, 
# otherwise call the notYourBirthday() function.
def happyBirthday():
    print('Happy Birthday!')

def notYourBirthday():
    print('It\'s not your birthday, but have a good day!')

birthday = input('Is it your Birthday? (Y or N) ' )
if birthday == 'y' or birthday == 'Y':
    happyBirthday()
elif birthday == 'n' or birthday == 'N':
    notYourBirthday()
else:
    print('Invaild syntax!')
exit