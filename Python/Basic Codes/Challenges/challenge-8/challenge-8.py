# your challenge is to ask the user to enter the names of everyone
# attending a party, then return a list of the party guests in alphabetic 
# order. This will require pulling together everything we have learned 
# so far, so let's walk through the thought process of idea to code

guests = []
name = ' '

while name != '':
    name = input('Enter the name (press enter if no more names): ')
    guests.append(name)

guests.sort()
print(guests)