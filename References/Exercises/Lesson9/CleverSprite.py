from livewires import games
games.init(screen_width=640, screen_height=440, fps=50)
countryScene = games.load_image("WinterBranches.jpg", transparent=False)
games.screen.background = countryScene
butterfly_image=games.load_image("flyingOwl.png")
butterfly=games.Sprite(image=butterfly_image, x=0, y=0, dx=3, dy=3)
games.screen.add(butterfly)
games.screen.mainloop()