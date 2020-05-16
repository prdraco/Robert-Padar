# the index() function will search the list and return 
# the index of the position where the value was found
guests = ['christopher', 'susan', 'bill', 'satya', 'sonal']

# this command will return with the index number where the bill is found
print(guests.index('bill'))
nbr = len(guests)
for steps in range(nbr):
    print(guests[steps])

# you can just tell the for loop to go through your list
# specify the name of your list and a variable name now it's guest
# to hold each entry as you go through the loop
for guest in guests:
    # the variable guest will contain the values
    print(guest)

# also you can sort your list with the sort() function
guests.sort()
print(guests)