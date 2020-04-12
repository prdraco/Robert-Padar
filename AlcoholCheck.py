#Ask the  user to enter the total number of alcoholic units he
#or she drinks in a week and convert the response to an integer
#If the number of units is equal to zero, print 'Are you a saint?
#Or perhaps you are lying?'
#If the number of units is less than or equal to 10, print
#'You are a moderate drinker. Pat yourself on the back.'
#If the number of units is less than or equal to 20, print
#'You are a heavy drinker and borderline alcoholic!'
#If the number of units is greater than 20, print 'You are
#a lush! You desperately need to join Alcoholics Anonymus!'
print('\n\t\tThis is an self acohol check...\n')
drink = input("How many times do you drink on a week? ")
drink = int(drink)
if drink == 0:
    print('Are you a Saint? Or perhaps you are lying?')
elif drink <= 10:
    print('You are a moderate drinker. Pat yourself on the back!')
elif drink <= 20:
    print('You are a heavy drinker and borderline alcoholic!')
else:
    print('You are a lush! You desperately need to join Alcoholics Anonymus!')
    


