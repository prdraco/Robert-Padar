#your assingment is to build a simple ping-pong game, 
#where a bouncing ball has to be intercepted by a paddle
#to stop the ball reaching the bottom of the screen.
#The ball rebounds off the paddle and countinues to 
# bounce off the sides until intercepted again

#inserting a background
from livewires import games, color
games.init(screen_width=640, screen_height=440, fps=50)

class Net(games.Sprite):
    #a paddle Net controlled by the player.
    image=games.load_image('Paddle.png')
    
    def __init__(self):
        super(Net, self).__init__(  image=Net.image,\
                                    x=games.mouse.x,\
                                    bottom=games.screen.height)
        self.score=games.Text(value=0, size=25, color=color.black,
								top=5, right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        #Move to mouse x position.
        self.x = games.mouse.x
        if self.left < 0:
            self.left=0
        if self.right>games.screen.width:
            self.right=games.screen.width
        self.check_catch()
    
    def check_catch(self):
        #Check if ball is caught.
        for ball in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            ball.handle_caught()

class PingPongBall(games.Sprite):
    # A bouncing Ping Pong Ball
    image=games.load_image('PingPongBall.png')
    speed=3

    def __init__(self, x=70, y=70):
        #initialise a ping pong ball object.
        super(PingPongBall,self).__init__(image=PingPongBall.image,\
                                            x=x, y=y, dx=PingPongBall.speed, \
                                            dy=PingPongBall.speed)
    
    def update(self):
        #Check if the bottom edge of the ping pong ball sprite
        #has reached the screen bottom.
        if self.right>games.screen.width or self.left<0:
            self.dx = -self.dx
        if self.top > games.screen.height or self.top <0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        #rebound of the paddle
        self.dy = -self.dy
    
    def end_game(self):
        #End The Game!
        end_message=games.Message(value='Game Over!', size=90,\
            color=color.black, x=games.screen.width/2,
            y=games.screen.height/2, lifetime=5*games.screen.fps, 
            after_death=games.screen.quit)
        games.screen.add(end_message)

def main():
    countryScene = games.load_image("PingPongTable.jpg", transparent=False)
    games.screen.background = countryScene
    the_ball=PingPongBall()
    games.screen.add(the_ball)
    the_net=Net()
    games.screen.add(the_net)
    games.mouse.is_visible=False
    games.screen.event_grab=True
    games.screen.mainloop()

main()