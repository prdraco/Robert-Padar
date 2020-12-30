#inserting a background
from livewires import games
games.init(screen_width=640, screen_height=440, fps=50)
countryScene = games.load_image("WinterBranches.jpg", transparent=False)
games.screen.background = countryScene
#inserting a sprite
owl_image=games.load_image("owl.png")
owl=games.Sprite(image=owl_image, x=420, y=60)
games.screen.add(owl)
games.screen.mainloop()