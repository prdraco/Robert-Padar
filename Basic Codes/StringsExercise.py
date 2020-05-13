#create string varibels containing four or more lines
#from the final single string from 1 above, extract and 
# print the 3rd line
#using the 'in' operator check if they have 'the' word is
#present in the final string and print eighter True or False
#Create a new string variable containing the words 'Try It Now'
#and evaluate it with the istitle() method, printing True or False
#Create another string variable with 'TRY IT NOW' and
#evaluate it with both the islower() and isupper() methods
#printing out is True or False
line1 = "That summer seemed to last forever\n"
line2 = "And if I had the choice\n"
line3 = "Yeah, I'd always want to be there\n"
line4 = "Those were the best days of my life\n "
print(line3[0:27])
checkin = 'the' in line4[33:37]
print(checkin)
code1 = 'Try It Now'
ist = code1.istitle()
print(ist)
code2 = 'TRY IT NOW'
ist2 = code2.isupper()
print(ist2)