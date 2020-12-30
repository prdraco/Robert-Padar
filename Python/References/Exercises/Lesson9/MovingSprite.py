#inserting a background
from livewires import games
games.init(screen_width=640, screen_height=440, fps=50)
class Net(games.Sprite):
	# An owl net controlled by the mouse.
	def update(self):
		# Move to mouse co-ordinates.
		self.x = games.mouse.x
		self.y = games.mouse.y
def main():
    countryScene = games.load_image("WinterBranches.jpg", transparent=False)
    games.screen.background = countryScene
    net_image = games.load_image("FlyingOwl.png")
    the_net = Net(image=net_image, x=games.mouse.x, y=games.mouse.y)
    games.screen.add(the_net)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()
main()