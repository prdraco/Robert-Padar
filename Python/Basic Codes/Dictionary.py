#create a dictionary of your choice, perhaps an employees dictionary 
# with employees names and lenght of service or a stock dictionary 
# with product name and quality in stock, or one of your choice; 
# include at least 5 kye:value pairs in your dictionary;
#print your dictionary using a for loop eith columns containing the 
# key and the value, and include appropitae headings
#add a new entry to your dictionary and print it again;
#modify an entry's value and print the dictionary;
#delete an entry and print the dictionary;
#print a single item from your dictionary
employees = {'DLF':'Packing grass seeds', 'BDM':'Packing fragrancies',
'Patent':'pipe cutting', 'Finisher':'Painting items', 'McDonalds':'Fast food restaurant'}
for term in employees:
	definition = employees[term]
	print(term, "\b:", definition)
employees['KFC'] = 'Fast food restaurant'
for term in employees:
	definition = employees[term]
	print(term, "\b:", definition)
employees['Patent'] = 'Cutting pipes'
for term in employees:
	definition = employees[term]
	print(term, "\b:", definition)
del employees['McDonalds']
for term in employees:
	definition = employees[term]
	print(term, "\b:", definition)
print(employees.get('DLF'))