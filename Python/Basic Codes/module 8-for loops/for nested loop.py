# You can use loos inside an other loop
import turtle

# for steps in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#     for morestepd in range(4):
#         turtle.forward(50)
#         turtle.right(90)

for steps in range(5):
    turtle.forward(100)
    turtle.right(360/5)
    for moresteps in range(5):
        turtle.forward(50)
        turtle.right(360/5)

nbr = 5
for steps in range(nbr):
    turtle.forward(100)
    turtle.right(360/nbr)
    for moresteps in range(nbr):
        turtle.forward(50)
        turtle.right(360/nbr)

for color in ['red', 'blue', 'yellow', 'purple']:
    turtle.color(color)
    turtle.backward(50)
    turtle.left(90)