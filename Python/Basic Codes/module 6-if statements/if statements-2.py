# What if we try an if statements  with numbers instead of strings

deposit = 150
if deposit > 100:
    print('You get a free toaster! ')
print('Have a nice day! ')

deposit = int(input('How much deposit you want to pay? '))

if deposit > 100:
    print('Enjoy you new toaster!')
else:
    print('You get a mug!')
print('Have a nice day! ')

# You can use boolean variables to remember if a condition is true or false
freeToaster = False
deposit = input('How much would you like to deposit? ')
if float(deposit) > 100:
    # set the boolean variable freeToaster to True
    freeToaster=True

# if the variable freeToaster is True
# the print statement will execute
if freeToaster :
    print('Enjoy your toaster! ')
print('Have a nice day! ')