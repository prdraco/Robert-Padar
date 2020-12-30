#create your own text file containing the text of your 
# choice; you might include text from a poem, song lyrics, 
# famous speech, or any other text of your choice
#open your text file in 'read-only' mode and print 
# your file line by line;
#open your text file in 'append' mode; add a block of 
# text to your file, then print the file
#open a new text file in 'write' mode; create a block 
# of text and write it to the new file
file = open('rasmusLyrics.txt', 'w')
lines = '\nNo sleep\n'
lines += 'No sleep until I am done with finding the answer\n'
lines += 'Won\'t stop\n'
lines += 'Won\'t stop before I find a cure for this cancer\n'
lines += 'Sometimes\n'
lines += 'I feel like going down and so disconnected\n'
lines += 'Somehow\n'
lines += 'I know that I am haunted to be wanted\n'
file.write(lines)
file.close()
print('File created')
file = open('rasmusLyrics.txt', 'r')
for line in file:
    print(line)
file = open('rasmusLyrics.txt', 'a')
newLines = 'I\'ve been watching\n'
newLines += 'I\'ve been waiting\n'
file.write(newLines)
file.close()
file = open('rasmusLyrics.txt', 'r')
for line in file:
    print(line)

file = open('justSamlpe.txt', 'w')
blocks = 'Just to write something\n'
blocks += 'in this file to create a new-one\n'
blocks += 'in same Python code!\n'
file.write(blocks)
print(blocks)