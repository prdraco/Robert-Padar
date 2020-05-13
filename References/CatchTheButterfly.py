#inserting a background
from livewires import games, color
import random
games.init(screen_width=640, screen_height=440, fps=50)

class Net(games.Sprite):
    # An owl net controlled by the player.
    image=games.load_image("flyingOwl.png")
    
    def __init__(self):
        # Initialise the net object and create text object for the score.
        super(Net, self).__init__( image=Net.image, x=games.mouse.x, \
            bottom=games.screen.height)
        self.score=games.Text(value=0, size=25, color=color.black,
        top=5, right=games.screen.width - 10)
        games.screen.add(self.score)
    
    def update(self):
        # Move to mouse x position.
        self.x=games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for owl in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            owl.handle_caught()

class Mouse(games.Sprite):
	# a mouse that falls to the ground.
	image=games.load_image("mouse.png")
	speed=3
	
	def __init__(self, x, y=70):
		# Initialise a mouse object.
		super(Mouse, self).__init__(image=Mouse.image,
										x=x, y=y,
										dy=Mouse.speed)

	def update(self):
		# Check if the bottom edge of the mouse sprite
		# has reached the screen bottom.
		if self.bottom > games.screen.height:
			self.end_game()
			self.destroy()

	def handle_caught(self):
		# Destroy mouse object if caught.
		self.destroy()
	
	def end_game(self):
		# End the game.
		end_message=games.Message(	value="Game Over!", size=90,
									color=color.yellow,
									x=games.screen.width/2,
									y=games.screen.height/2,
									lifetime= 5 * games.screen.fps,
									after_death = games.screen.quit)
		games.screen.add(end_message)

class Caterpillar(games.Sprite):
	# A caterpillar that moves left and right dropping mouses.
	image=games.load_image("mouseHole.png")
	
	def __init__(self, y=20, speed=3, odds_change=200):
		# Initialise the caterpillar object.
		super(Caterpillar, self).__init__(	image=Caterpillar.image,
											x=games.screen.width/2,
											y=y, dx=speed)
		self.odds_change = odds_change
		self.time_til_drop = 0
	
	def update(self):
		# Check if direction should be reversed
		if self.left < 0 or self.right > games.screen.width:
			self.dx = -self.dx
		elif random.randrange(self.odds_change) == 0:
			self.dx = -self.dx
		self.check_drop()
		
	def check_drop(self):
		# Decrease countdown or drop mouse and reset countdown.
		if self.time_til_drop > 0:
			self.time_til_drop -= 1
		else:
			new_mouse = Mouse(x=self.x)
			games.screen.add(new_mouse)
			# Set buffer to 20% of mouse height
			self.time_til_drop = int(new_mouse.height * 1.2 / Mouse.speed) + 1

def main():
	# Play the game.
	countryScene = games.load_image("winterBranches.jpg", transparent = False)
	games.screen.background = countryScene

	the_caterpillar = Caterpillar()
	games.screen.add(the_caterpillar)
	
	the_net = Net()
	games.screen.add(the_net)

	games.mouse.is_visible = False
	games.screen.event_grab = True
	
	games.screen.mainloop()

# Start the program.
main()