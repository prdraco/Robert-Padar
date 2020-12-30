#create a while loop, which will accept a password entered 
# by the user and will keep doing so until the user input 
# is equal to "", i.e. an empty string with no data
#Check if the password entered is equal to admin1 OR admin2 
# and, if so, set the adminUser variable to True, otherwise False
#Check if the password is equal to user1 OR user2 and, if 
# so, set the normalUser variable to True, otherwise False
#Check if the adminUser AND normalUser are both False if 
# so, print the  message "invaild password." ,otherwise, if 
# the adminUser is equal to True, print the message "Password 
# accepted; you have administrator privileges." and, if the 
# normalUser is equal to True, print the message "Password accepted"
password = input("\nPlease enter your Password: ")
adminUser = 'None'
normalUser = 'None'
while password:
	if password == "admin1" or password == "admin2":
		adminUser = True
		print('Password accepted; you have administrator privileges.')
		break
	if password == 'user1' or password == 'user2':
		normalUser = True
		print('Password accepted! ')
		break
	else:
		adminUser == False
		normalUser == False
		print('Invaild Password!')
		break