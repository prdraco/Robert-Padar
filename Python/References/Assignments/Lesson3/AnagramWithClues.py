# The Anagram Game
import random
WORDS =["python", "estimate", "difficult", "answer", "xylophone", "unnecessary", "adequate", "feasible", "character", "congratulations", "sequence", "position", "program"]
clues = ["A program language", "An approximate calculation", "Needing much effort", "A reaction to a question", "A musical instrument", "Do not really need", "Acceptable in quality or quantity", "possible to do easily", "A printed or written letter or symbol",  "Good wishes when done something", "A set of related events or movements", "To located in something", "Coded application or game"]
# Choose a random word from the Word list
word = random.choice(WORDS)
position1 = WORDS.index(word)
print(position1)
clue = clues[position1]
print(clue)
correct = word
anagram = ""
# Mix up the letters in the word
for n in range(0, len(word)):
	position = random.randrange(len(word))
	anagram += word[position]
	word = word[:position] + word[(position+1):]
# Welcome the user, print the anagram, and get the first guess
print("\nWelcome to the anagram game.")
print("\nUnscramble the letters to make a word.")
print("\nThe anagram is:", anagram ," Clue:" ,clue)
answer = input("\nYour answer: ")
# Loop until the answer is correct or an empty string is input
while answer != correct and answer != "":
	print("\nSorry, that's not quite right.")
	answer = input("\nYour answer: ")
# The answer is correct
if answer == correct:
	print("\nWell done, you got it!")