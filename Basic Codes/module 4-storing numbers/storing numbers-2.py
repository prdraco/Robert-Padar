# Sometimes you will need to format 
# the numbers when you display them to user
print('I have %d cats' % 6)     # I have 6 cats
print('I have %3d cats' % 6)     # I have   6 cats
print('I have %03d cats' % 6)     # I have 006 cats
print('I have %f cats' % 6)     # I have 6.000000 cats
print('I have %.2f cats' % 6)     # I have 6.00 cats

# You can also use a format method to format numeric values
print('I have {0:d} cats' .format(6))     # I have 6 cats
print('I have {0:3d} cats' .format(6))     # I have   6 cats
print('I have {0:03d} cats' .format(6))     # I have 006 cats
print('I have {0:f} cats' .format(6))     # I have 6.000000 cats
print('I have {0:.2f} cats' .format(6))     # I have 6.00 cats

area = 0
height = 10
widht = 20

#calculate the area of a triangle
area = widht * height /2
print('The area of the triangle would be %d' % area)