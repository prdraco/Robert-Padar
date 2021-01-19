# You can nest if statements inside each other

monday = True
fhresCoffee = False
if monday:
    #you could have code here to check for fresh coffee
    #the if statement is nested, so this if statement
    #is only executed if the other if statement is True
    if not fhresCoffee:
        print('go buy a coffee!')
    print('I hate Mondays')
print('now you can start work')

sport = 'HOCKEY'
team = 'SENATORS'
if sport == 'HOCKEY':
    print('Go hockey!!!')
    if team == 'SENATORS':
        print('Good luck to getting the cup in this year')
        print('We do love hockey')