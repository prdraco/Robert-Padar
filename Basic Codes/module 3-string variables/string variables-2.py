# variable names have rules as
# can not contain spaces,
# these are case sensitive
# can not start with numbers

# should be descriptive but not too long (favoriteSong and 
# not yourFavoriteSongFromQueen)
# use a casing "scheme" like camelCasing or PascalCasing

# you can combine variables and strings with the + symbol
firstName = input('What is your firs name? ')
lastName = input('What is your last name? ')
print('Hello ' + firstName + ' ' + lastName)

# now you can create a story teller program
animal = input('What is your favorite animal? ')
building = input('Name of a famous builing: ')
color = input('What is your favorite color? ')
print('Hickory Dickory Dock!')
print('The ' + color + ' ' + animal + ' ran up the ' + building)