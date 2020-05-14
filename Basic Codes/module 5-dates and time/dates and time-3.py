# Just like with dates, you can use strftime() to 
# format the way a time is displayed
# %H Hours (24 hr clock)
# %I Hours (12 hr clock)
# %p AM or PM
# %m Minutes
# %S seconds

import datetime
currentTime = datetime.datetime.now()
print(datetime.datetime.strftime(currentTime, '%H:%M'))
print(currentTime.minute)