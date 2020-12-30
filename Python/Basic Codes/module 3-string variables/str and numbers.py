#Write a Python program to convert these numbers into string then into float types:

#10,20,30,40,50,60,70,80,90,100

number1 = '10'
number2 = '20'
number3 = '30'
number4 = '40'
number5 = '50'
number6 = '60'
number7 = '70'
number8 = '80'
number9 = '90'
number10 = '100'
strNumbers = str(number1 + ',' + number2 + ',' + number3 + ',' + number4 + ',' +\
 number5 + ',' + number6 + ',' + number7 + ',' + number8 + ',' + \
number9 + ',' + number10)
print(strNumbers)
number1 = float(number1)
number2 = float(number2)
number3 = float(number3)
number4 = float(number4)
number5 = float(number5)
number6 = float(number6)
number7 = float(number7)
number8 = float(number8)
number9 = float(number9)
number10 = float(number10)
floatNumbers = [number1,number2,number3,number4,number5,number6,\
number7,number8,number9,number10]
print(floatNumbers)