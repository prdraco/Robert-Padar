# there are functions to convert from one datatype to another.
# int(value)        converts to an integer
# long(value)       converts to a long integer
# float(value)      converts to a floating number (12.34567)
#str(value)         converts to a string

salary = input('please enter your salary ')
bonus = input('please enter your bonus ')

paycheckAmount = float(salary) + float(bonus)
print(paycheckAmount)