# The import statement gives us access to 
# the functionality of the datetime class
import datetime

# today is a function that returns today's date
print(datetime.date.today())

# you can access different parts of the date
currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)