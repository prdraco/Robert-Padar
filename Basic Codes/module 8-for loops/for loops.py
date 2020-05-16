# You can use turlte module to use graphics drawings
# right(x) rotate right x degrees
# left(x)  rotate left x degrees
# color('x') change pen color to x
# forward(x) move forward x
# backward(x) move backward x

import turtle
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)

for steps in range(4):
    turtle.color('red')
    turtle.right(90)
    turtle.forward(100)
turtle.color('blue')
turtle.forward(200)
    