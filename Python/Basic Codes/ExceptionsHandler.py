#Using try an except, ask the user to enter a decimal number, 
# which you should convert to a floating point number, and 
# print your own error message if an invaild number is 
# entered, e.g. an alphabetic character;
#Also, print the Python error message, and include an else 
# clause to confirm a valid decimal number has been input;
#Ask the user to enter the current hour, If the number 
# entered is not a number, use except to print a 'not a number' 
# message; if a number is entered but is not in the range 
# 0 to 24, raise an 'Invaild hour' error and print it, 
# oterhwise print a ' Vaild hour' message.
number = input('Enter a decimal number: ')
error = False
try:
    number = float(number)
    print(number)
except ValueError as errorMsg:
    print('Invaild number! ', errorMsg)
hour = input('What is the current hour right now? ')
try:
    hour = int(hour)
    if hour not in range(0, 24):
        print('Invaild hour! ')
    else:
        print('Vaild hour! ') 
except:
    print('Not a number! ')