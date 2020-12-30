#Create your own list using using items of your choice; 
# this could be a list of colours, books, food, or anything you choose;
#Pickle the list data, write it to a data file, and close the binary file
#Open the binary file in read mode, un-picle the data, and 
# print your list, which should now be in its original form;
#Create a shelf file and write three separate lists of your 
# choice to it like we did in our example; the lists could be 
# football teams, sports, hobbies, or lists of your own 
# choice; then, close the file
#Open the shelf file in read-only mode, un-pickle the data, 
# and print the contents, which should be your nested 
# lists in their original form
import pickle
import shelve
list1 = ['blue', 'yellow', 'red', 'green']
list2 = ['pizza', 'pasta', 'rice']
file = open('textBinari.txt', 'wb')
pickle.dump(list1, file)
file.close()
file = open('textBinari.txt', 'rb')
data = pickle.load(file)
print(data)
file.close
shelf = shelve.open('newFile.dat', 'c')
shelf['movies'] = ['Holnaputan', 'Jackal', 'Seven', 'Terminator']
shelf['songs'] = ['From the inside', 'In the Shadow', 'What I\'ve done',\
    'I need a Doctor', 'White Flag']
shelf['hobbies'] = ['basketball', 'tennis', 'soccer', 'darts']
shelf.sync()
shelf.close
shelf = shelve.open('newFile.dat', 'r')
for steps in shelf['movies']:
    print(steps)
    for steps in shelf['songs']:
        print(steps)
        for steps in shelf['hobbies']:
            print(steps)
shelf.close()