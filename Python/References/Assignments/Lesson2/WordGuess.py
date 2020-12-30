#Your assignment is to build a python program that will select a random word 
# from a list of words, then display the word with alternate letters replaced 
# by a hyphen, for example, if the word were sequence, you would 
# display: -e-u-n-e. The user then has to guess the word.
#To detect if a letter is in an odd or even position in a word, in a for loop, 
# use the modulus operator to divide by two, leaving a remainder, e.g. 
# remainder = n%2; if the remainder is zero the letter is odd, else even, 
# remembering that the letters are accessed starting at position zero
#print congratulatory message if the word is guessed correctly, else print a 
# loser message and disclose the word.
import random
WORDS =("python", "estimate", "difficult", "answer", \
		"mobilephone", "unnecessary", \
		"feasible", "character", "congratulations", \
		"sequence", "position", "program")
randomWord = random.choice(WORDS)
b = ''
for i in range(len(randomWord)):
    if (i%2)==0:
        b+=randomWord[i]
print('\fThis is a guess the word I guessed game! ')
print('\nHere are the possible words: ')
print(WORDS)
print('\nWhich is the word what I choosed? ')
print('Some help with some letters from the word: ')
print(b)
userWord = input('Your answer: ')
if userWord == randomWord:
    print('You are right, congratulation!' )
    exit
if userWord != randomWord:
    print('That\'s wrong! ')
    exit
