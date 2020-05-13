#Get the diameter of the circle in centimeters from the user 
# and convert it to an integer
#Calculate the area of the circle as follows
#(3.14159265 / 4)*(diameter * diameter)
#then display : 'The area of your circle is nnnn.nnnn centimeters.'
#where nnnn.nnnn is the calculated value

diameter = float(input('How much centimeters would you the circle diameter? '))
areaOfCircle = (3.14159265 / 4) * (diameter * diameter)
areaOfCircle = str(areaOfCircle)
print('The area of your circle is ' + areaOfCircle + ' centimeters')