#create a list containing at least 5 elements of your 
# choice and print the list
#appent a new item to your list using the append() 
# method and print the list
#insert a new item in index position 3 of your list 
# using the insert() method and print the list
#delete an item from your list using the remove() 
# method and print the list
#create a new list with 3 items and append this list to 
# your original list using the extend() method and print the list
#sort your list into ascending sequence using the sort() 
# method and print it, then sort it into descending 
# order and print it again
fruits = ['banana' , 'orange' , 'kiwi' , 'apple' , 'lemon']
fruits.append('pear')
print(fruits)
fruits.insert(3, 'melon')
print(fruits)
fruits.remove('kiwi')
print(fruits)
drinks = ['cola' , 'juice' , 'milk']
fruits.extend(drinks)
print(fruits)
fruits.sort(reverse=False)
print(fruits)
fruits.sort(reverse=True)
print(fruits)