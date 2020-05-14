# strftime to format dates allows you to spcify the date
# srtptime allows you to convert a string to a date

import datetime

currentDate = datetime.date.today()
print(currentDate.strftime('%d %b,%Y'))

# %b is the month abbreviation
# %B is the full month name
# %y is two digit year
# %Y is 4 digit year
# %a is the day of the week abbreviated
# %A is the day of the week

# for full list, visit strftime.org

# Please attend our event Sunday, July 20 in the year 1997
print(currentDate.strftime('Please attend our event %A, \
%B %d in the year %Y'))

# let's get back to calculating days until your birthday, 
# I need to ask your birthday
birthday = input('Enter your next birthday (mm/dd/yyyy) ')
birthdate = datetime.datetime.strptime(birthday, '%m/%d/%Y').date()
# why did we list datetime twice?
# because we are calling the srtptime function
# which is part of the datetime class
# which is in the datetime module
print('Your birth month is ' + birthdate.strftime('%B'))
days = birthdate - currentDate
print('Only ', days.days ,' left')