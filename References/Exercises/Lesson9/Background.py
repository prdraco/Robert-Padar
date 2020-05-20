#inserting a background
from livewires import games
games.init(screen_width=640, screen_height=440, fps=50)
countryScene = games.load_image("WinterBranches.jpg", transparent=False)
games.screen.background = countryScene
games.screen.mainloop()