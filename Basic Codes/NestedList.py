#create a parent list containing at least 3 nested list each 
# containing two related elements; for example your parent 
# list could represent the english premier league and the 
# nested list could each contain the name of a football team 
# and its position in the league, however, you are welcome 
# to use another theme of your choice
#print the contents of your parent list
#print the contents of the nested list at index position 1
#append a new nested list using the append() method and 
# print the new contents of the parent list
parent = [('Manchester', 1), ('Newcastle', 5), ('Liverpool', 2)]
print(parent)
print(parent[1])
parent.append(('Bristol', 12))
print(parent)