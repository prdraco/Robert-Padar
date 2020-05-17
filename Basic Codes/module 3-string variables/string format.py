#Write a program in python that take two string to complete and form 
# a message that we can understand

#msg =  "python is   &      language"
python = 'Objective Oriented Programming'
userType = 'computer'
print('Python is an' , python , '&' , userType , 'language.')
print('Python is an {} & {} language.' .format(python,userType))

print(len(python))

# write a program in python to declare a message for an instructing 
# sign in public place
# and get the lenth of that message and count of the number 
# a specific letter in the message: 
message = 'Someone just singed in your area, send her/his a messge!'
print(message.count('o'))

#Write a program in python to count the vowels in the following string:
#"Are you working as a Python programmer ?"
msg = 'are you working as a Python programmer ?'
a = msg.count('a')
e = msg.count('e')
o = msg.count('o')
u = msg.count('u')
i = msg.count('i')
vowels = a + e + o + u + i
print('In this message have:' , vowels , 'vowels! ')
print('In this message have: {} vowels! ' .format(vowels))