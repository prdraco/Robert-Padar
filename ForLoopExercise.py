#ask the user to enter a word or phrase, create a for loop to count the number of characters entered, and print "You have entered nn characters", where nn is the character count
#create a for loop that will print a count from 20 to 100 in increments of 20
#create a nested for loop (a loop within a loop), where the first loop (the outer loop) executes 3 times printing "The outer loop count = n", where n is the loop counter, and the second loop (the inner loop, which executes inside the firt loop) executes 5 times, printing a tab character then "The inner loop count = i", where i is the loop counter.
word = input('Please enter a word: ')
characters = len(word)
for n in word:
    print(n)
print('You have entered %d characters! ' % characters)
for n in range(20,100,20):
    print(n)

n = 0
for n in range(1,4):
    print('The outer loop counter= %d' % n)
    n += 1
    for i in range(1,6):
        print('\tThe inner loop counter = %d' % i)