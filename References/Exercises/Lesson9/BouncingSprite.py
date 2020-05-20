#inserting a background
from livewires import games, color
import random
games.init(screen_width=640, screen_height=440, fps=50)
class Net(games.Sprite):
    def update(self):
        self.x=games.mouse.x
        self.y=games.mouse.y
        self.check_collide()
    def check_collide(self):
        for owl in self.overlapping_sprites:
            owl.handle_collide()
class Owl(games.Sprite):
	# A clever owl.
	def handle_collide(self):
		# Move the owl to a random location.
		self.x = random.randrange(games.screen.width)
		self.y = random.randrange(games.screen.height)
      
def main():
    winter = games.load_image("WinterBranches.jpg", transparent=False)
    games.screen.background = winter
#inserting a sprite
    owl_image=games.load_image("Owl.png")
    owl_x=random.randrange(games.screen.width)
    owl_y=random.randrange(games.screen.height)
    the_owl=Owl(image=owl_image, x=owl_x, y=owl_y)
    games.screen.add(the_owl)
    
    net_image=games.load_image("flyingOwl.png")
    the_net=Net(image=net_image, x=games.mouse.x, y=games.mouse.y)
    games.screen.add(the_net)

    games.mouse.is_visible=False
    games.screen.event_grab=True
    user_message = games.Message(value="Try to catch the owl!", 
							size=50, color=color.yellow,
							x=games.screen.width/2,
							y=games.screen.height/2,
							lifetime=100)
    games.screen.add(user_message)
    games.screen.mainloop()

main()