# Your challenge is to create an etch a sketch program
# have the user enter a pen color, a line lenght and an angle
# use turtle to draw a line based on their specifications
# let them specify new lines over and over until they 
# enter a line lenght of 0.

import turtle
print('\tWelcome to my sketch program. \nEnter your details \
about the lines and draw whatever you want. \nIf you finished \
just enter \'0\' to the line lenght to exit.')
color = input('Enter the line color: ')
angle = int(input('Enter the line angle: '))
lenght = int(input('Enter the line lenght: '))
while lenght != 0:
    turtle.color(color)
    turtle.forward(lenght)
    turtle.right(angle)
    color = input('Enter the line color: ')
    angle = int(input('Enter the line angle: '))
    lenght = int(input('Enter the line lenght: '))