# The Python Test Quiz
import sys

def open_file(file_name, mode):
	# Open the file contained in file_name
	try:
		file = open('MyQuizQuestions.txt', 'r')
	except IOError:
		print("Unable to open the file", file_name, "\n")
		print("Program aborted!")
		sys.exit()
	else:
		return file

def next_line(file):
	# Get the next line from the questions file, formatted.
	line = file.readline()
	return line

def next_block(file):
	# Get the next block of data from the questions file.
	category = next_line(file) # Get first line in block (category)
	question = next_line(file) # Get next line in block (question)
	answers = [] # Create a list to contain the answers
	for i in range(4):
		answers.append(next_line(file)) # Get the 4 answers
	correct = next_line(file) # Get the correct answer number
	if correct:
		correct = correct[0]
	explanation = next_line(file) # Get the explanation
	return category, question, answers, correct, explanation

def main():
	# The main function
	print("\nWelcome To The Python Test Quiz!")
	name = input("\nWhat is your name? ")
	name = name.title()
	print("\nHi,", name, "\b.")
	quiz_file = open_file("MyQuizQuestions.txt", "r")
	score = 0
	# get first block
	category, question, answers, correct, explanation = next_block(quiz_file)
	numQuestions = 0
	while category:
		# ask a question
		numQuestions += 1
		print(category)
		print(question)
		for i in range(4):
			print(i + 1, "-", answers[i])
		# get user's answer
		answer = input("Choose your answer? ")
		# check user's answer
		if answer == correct:
			print("\nWell done!", end=" ")
			score += 1
		else:
			print("\nSorry.", end=" ")
		print(explanation)
		print("Score:", score, "from", numQuestions, "\b.\n")
		# get next block
		category, question, answers, correct, explanation = next_block(quiz_file)

	quiz_file.close()
	print("That was the last question!")
	print("\nYou're final score is", score, "from", numQuestions, "\b.")
 
main()