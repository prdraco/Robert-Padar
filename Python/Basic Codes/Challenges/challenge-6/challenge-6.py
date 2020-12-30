# Your challenge is to get turtle to draw an octagon
# extra challenge to let the user specify how many 
# sides the object will have and draw whatever they ask
# duoble bonus to add a nested loop to draw a smaller 
# version of the object inside!

import turtle

# for steps in range(8):
#     turtle.forward(80)
#     turtle.right(360/8)

sides = int(input('How many sides do you want to draw? '))
for steps in range(sides):
    turtle.forward(80)
    turtle.right(360/sides)
    for moreSteps in range(sides):
        turtle.forward(40)
        turtle.right(360/sides)
