import random
WORDS = (	"PYTHON", "ESTIMATE", "DIFFICULT", "ANSWER", "XYLOPHONE", \
			"UNNECESSARY", "ADEQUATE", "FEASIBLE", "CHARACTER", \
			"CONGRATULATIONS", "SEQUENCE", "POSITION", "PROGRAM" )
MAX_WRONG = 6
wrong = 0
word = random.choice(WORDS)
so_far = "-" * len(word)
used = []
print("\nWelcome to Hangman.")
print("\nYou have", MAX_WRONG, "wrong attempts to guess the word.")
def prologe():
	print("""The object of the game is to get the word what the computer choosed within 6 tries
	-----------			----------
	|/        |			|/	 |
	|		  		|	 O
	|				| 	/|/
	|				|	/ /
	|				|
	----				----  """)

def guesses():
	so_far = "-" * len(word)
	wrong = 0
	while wrong < MAX_WRONG and so_far != word:
		print(so_far)
		guess=input('Enter a letter: ')
		guess=guess.upper()
		while guess in used:
			print("\nYou have already guessed this letter\a", guess)
			guess=input("Enter a letter: ")
			guess=guess.upper()
		used.append(guess)
		if guess in word:
			print('Yes, ', guess , 'is in the word!')
			new= ''
			for i in range(len(word)):
				if guess == word[i]:
					new += guess
				else:
					new += so_far[i]
			so_far = new
		else:
			print('Sorry, ', guess , 'isn\'t in the word.')
			wrong += 1
			left = MAX_WRONG - wrong
			print("\nYou have", left, "guesses left.")
			displayScaffold(wrong)
	if wrong == MAX_WRONG:
		print('You have been hanged!')
		print('The word was ', word)
	else:
		print('You guessed it!')

def displayScaffold(wrong):
	if wrong==1:
		print('____________')
		print('|/         |')
		print('|          O')
		print('|')
		print('|')
		print('|')
		print('|___________')
	if wrong==2:
		print('____________')
		print('|/         |')
		print('|          O')
		print('|         /')
		print('|')
		print('|')
		print('|___________')
	if wrong==3:
		print('____________')
		print('|/         |')
		print('|          O')
		print('|         /|')
		print('|')
		print('|')
		print('|___________')
	if wrong==4:
		print('____________')
		print('|/         |')
		print('|          O')
		print('|         /|/')
		print('|')
		print('|')
		print('|___________')
	if wrong==5:
		print('____________')
		print('|/         |')
		print('|          O')
		print('|         /|/')
		print('|         /')
		print('|')
		print('|___________')
	if wrong==6:
		print('____________')
		print('|/         |')
		print('|          O')
		print('|         /|/')
		print('|         / /')
		print('|')
		print('|___________')

def main():
	prologe()
	guesses()
	displayScaffold(wrong)

main()