#Create a function called calculateArea(), which will have two 
# parameters, width and height, passed from the main body, will 
# multiply them together, and return the result
#ask the user to enter the width of a rectangle in cms, then 
# ask for the height in cms
#call the calculateArea() function passing over the widht and 
# height values, and print the result of the calculation; 
#Next create another function called circleArea() to calculate
#  the area of a circle in sq. cms; this function will take one 
# parameter, which is the diameter of the circle in cms, 
# and will return the area of the circle;
#Ask the user to enter the diameter of the circle in cms;
#call the circleArea()function passing over the diameter, 
# and print the result of the calculation.
def calculateArea():
    result = widht * height
    return(result)
widht = int(input('What is the widht in cm? '))
height = int(input('What is the height in cm? '))
print(calculateArea())
def circleArea():
    result = diameter * 3.14159265
    return(result)
diameter = int(input('What is the circle diameter in cm? '))
print(circleArea())