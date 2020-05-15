# Your challenge is ask the user to enter the 
# deadline for their project
# Tell them how many days they have to complete the project
# For extra credit, give them the answer as a combination 
# of weeks & days (Hint: you will need some of the math 
# functions from the module on numeric values)
import datetime

deadline = input('Please enter, when the project ends (dd/mm/yyyy) ')
projectEnds = datetime.datetime.strptime(deadline, '%d/%m/%Y').date()
currentDate = datetime.date.today()
daysLeft = projectEnds - currentDate
print(daysLeft.days, 'days left to complete the project!')
daysLeft = int(daysLeft.days)
weeks = daysLeft/7
weeks = '%d' % weeks
weeks = int(weeks)
day = daysLeft - (weeks*7)
print(weeks, 'weeks and' ,day, 'days left' )