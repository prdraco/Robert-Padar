# if statements allows you to specfy code that only executes 
# if a specify condition is true
# some of most used symbols for different conditions
# ==    is equal to                 if answer == 'yes':
# !=    is not equal to             if answer != 'no':
# <     is less than                if total < 100:
# >     is greater than             if total > 100:
# <=    is less than or equal to    if total <= 100:
# >=    is greater than or equal to if total >= 100:

answer = input('Would you like express shipping? ')
if answer =='Yes':
    print('That will be an extra £10 ') 
print('Have a nice day!')

favoriteTeam = input('What is your favorite Hockey team? ')
if favoriteTeam.upper() == 'SENATORS':
    print('Yeah go Sens go')
    print('but I miss Alfredsson')
print('It\'s ok if you prefer football or basketball! ')