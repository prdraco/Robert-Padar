# Your challenge is to write a program that allows a 
# person to personalize a story.
# Take a page from a book or make up a story. Ask the 
# user to enter information you can replace in the 
# story such as their name, a place, or insert 
# adjectives or adverbs into the story. Then display 
# the personalized story to the user.

name = input('What is your name? ')
name = name.title()
holidayDate = input('When you will go to holiday in this year? ')
favoritePlace = input('What is your favorite holiday place? ')
favoritePlace = favoritePlace.capitalize()
friends = input('Enter 3 of your best friends (... , ... , ...): ')
friends = friends.title()
print(name + ' works hard in the whole year, \
but each year in a same date, on ' + holidayDate + ' \
will \ngo to 3 weeks holiday. In this year the destination is \
' + favoritePlace + '. \nSpent 3 weeks on amazing holiday with the \
best friends: ' + friends + ', \nbut it\'s \
end now and time to go back to work')