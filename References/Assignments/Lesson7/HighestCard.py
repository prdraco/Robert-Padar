#Your assignment is to build the Highest Card game, where from 2 
#to 7 players play aganist each other, each receiving one random 
#card and the program deciding who has the highest ranking card; 
#the event of more than one player having the highest ranking 
#card, then a draw is declared.
#Base your program on the Blackjack game but be aware that, in 
#this game, an ace is the highest card in rank and many of the 
#Blackjack methods, which, for example, check if a player is 
#still playing or requires additional cards, are not required 
#for this assingment.
#You will be required to insert code into the play() method to 
#check which player has the highest card and you will need to 
#print out each player's name and the card they have been dealt,
#followed by "And the winner is...", followed by the name of 
#the winning player or "Draw" in the event of a tie.
import Cards, Games

class Highest_Card(Cards.Card):
# Defines a Highest game cards
	ACE_VALUE = 1
	@property
	def value(self):
		if self.is_face_up:
			val = Highest_Card.CARDS.index(self.card) + 1
			if val > 10:
				val = 10
		else:
			val = None
		return val
	# This object returns a number between 1 and 10,
	# representing the value of a Highest card

class Highest_Deck(Cards.Deck):
# Defines a Highest game deck
	def populate(self):
		for suit in Highest_Card.SUITS:
			for card in Highest_Card.CARDS:
				self.cards.append(Highest_Card(card, suit))

class Highest_Hand(Cards.Hand):
# Defines a cards in hand
	def __init__(self, name):
		super(Highest_Hand, self).__init__()
		self.name = name
	def __str__(self):
		rep = self.name + ":\t" + super(Highest_Hand, self).__str__()
		if self.total:
			rep += "(" + str(self.total) + ")"
		return rep
	@property
	def total(self):
	# If a card has the value None, then total is None
		for card in self.cards:
			if not card.value:
				return None
		# Add card values, treating Ace as 1
		t = 0
		for card in self.cards:
			t += card.value
		# Check if hand contains an Ace
		contains_ace = False
		for card in self.cards:
			if card.value == Highest_Card.ACE_VALUE:
				contains_ace = True
		# If hand is low enough treat Ace as 11
		if contains_ace and t<= 11:
			# Add 10 since we already added 1 for the Ace
			t += 10
		return t

class Highest_Player(Highest_Hand):
# Defines a Highest Card player
	def lose(self):
		print(self.name, "loses.")
	def win(self):
		print(self.name, "wins.")
	def push(self):
		print(self.name, 'draws.')
		
class Highest_Game(object):
# Defines a Highest Card game
	def __init__(self, names):
		self.players = []
		for name in names:
			player = Highest_Player(name)
			self.players.append(player)
		self.dealer = Highest_Player(Highest_Hand)
		self.deck = Highest_Deck()
		self.deck.populate()

	def play(self):
		# Deal initial 1 cards to all players
		self.deck.deal(self.players, per_hand = 1)
		for player in self.players:
			print(player)
		max = 1
		winner = 'NoBudy'
		for player in self.players:
			if player.total > max:
				max = player.total
				winner = player
		print('\nAnd the winner is: ', winner)

		# Remove everyone's cards
		for player in self.players:
			player.clear()

def main():
	print("\nWelcome to the Python Highest Card game.\n")
	names = []
	number = Games.askForNumber("How many players? (2-7): ", low = 2, high = 8)
	print()
	i = 1
	for i in range(number):
		name = input("Enter player name: ")
		if name == "":
			names.append("Anon")
			print()
			i += 1
		else:
			names.append(name)
			print()
			i += 1
	game = Highest_Game(names)
	again = "Y"
	while again == "y" or again == "Y":
		game.play()
		again = Games.askYesNo("\nDo you want to play again?: ")
	
main()