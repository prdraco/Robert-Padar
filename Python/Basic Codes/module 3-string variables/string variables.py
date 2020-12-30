# how we can ask a user for information?

name = input('What is your name? ')
# the input function allows you to specify a message to 
# display and returns the value typed in by user
# we use a variable to remember the value entered by the user
# we called our variable "name" but you can call it just about 
# anything as long the variable name doesn't contain spaces
print(name)

# You can also change the value of the variable later in the code
name = 'Ronald'
print(name)
name = name.replace('Ronald','Lazzlo')
print(name)

# or count the variable
name = name.count('z')
print(name)