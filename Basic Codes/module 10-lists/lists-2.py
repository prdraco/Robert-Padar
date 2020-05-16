 # after create, you can change a value in a list
guests = ['christopher', 'susan', 'bill', 'satya']
print('first value is ' ,guests[0])

# change the value
guests[0] = 'steve'
print('the first value now is ' ,guests[0])

# or you can add a value to a list, and delete a value from the list
guests.append('christopher')
guests.remove('susan')

# if you don't now what exactly the value name, you can 
# delete it by the index number
del guests[2]

# display now the full list
print(guests)