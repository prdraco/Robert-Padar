#Create two different lists containing the items of your choice; 
# the items can be, for example friends, books, music traks, 
# football teams, food, drink or any kind of list you prefer;
#Print all items in each list using a for loop;
#print a single item from each list;
#Add an item to each list;
#delete an item from each list;
#concatenate the two lists and print the concatenated list
friends = ['Anita' , 'Renata' , 'Lazzlo' , 'Melinda' , 'Gabor']
drinks = ['cola' , 'beer' , 'water' , 'wine' , 'juice']
for item in friends:
    print(item)
for item in drinks:
    print(item)
print(friends[2])
print(drinks[4])
friends.append('Roland')
drinks.append('soda')
friends.remove('Lazzlo')
drinks.remove('beer')
con = friends + drinks
print(con)