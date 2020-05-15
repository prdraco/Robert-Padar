# Imagine you have code that ran earlier which set these two variables
wonLottery = True
bigWin = True

# at the and statements
# print statement only executes if both conditions are true
if wonLottery and bigWin:
    print('You can retire now!')

sport = input('Enter your favorite sport: ').upper()
team = input('Enter your favorite hockey team: ').upper()

if sport == 'HOCKEY' and team == 'RANGERS':
    print('I miss Messier!')
else:
    print('I don\'t know that team! ')

# at the or statements
# print statement executes if one of those statement are true

if sport == 'HOCKEY' and team == 'RANGERS':
    print('I miss Messier!')
elif team == 'LEAFS' or team == 'SENATORS':
    print('Good luck getting the cup in this year! ')
else:
    print('I don\'t know that team! ')

# You can combine multiple 'and'/'or' in a single statement
month = 'Nov'
month = month.upper()
favMovie = 'Star Wars'
favMovie = favMovie.upper()
favBook = 'Harry Potter'
favBook = favBook.upper()
favEvent = 'Sziget'
favEvent = favEvent.upper()
if month == 'SEP' or month == 'APR' or month == 'JUNE' \
or month == 'NOV':
    print('There are 30 days in this month')
if favMovie == 'STAR WARS' and favBook == 'LORD OF THE RINGS' \
and favEvent == 'COMICON' :
    print('You and I should hang out!')

if favMovie == 'STAR WARS' and favEvent == 'COMICON' or \
favBook == 'HARRY POTTER':
    print('Do you play basketball too?')