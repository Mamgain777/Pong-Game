import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.set_ball()
        self.ball_speed = 0.1

    def set_ball(self):
        # self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.penup()
        self.color('green')
        self.shape('circle')
        self.goto(x=0, y=-280)

    def move_ball(self):
        self.forward(20)

    # Setting Ball direction to move
    def start_round(self, side):
        self.goto(x=0, y=-280)
        self.ball_speed = 0.15
        if side == 'blue':
            self.setheading(random.randint(20, 50))
        else:
            self.setheading(random.randint(140, 170))

    def bar_collision(self, bar, xcor, sign):
        if self.xcor() > xcor and (self.distance(bar.top) < 30 or self.distance(bar.bottom) < 30):
            # solving glitch for speed reaching 0.025
            if (self.ball_speed*0.7) > 0.04:
                self.ball_speed *= 0.9
            print(self.ball_speed)
            if self.distance(bar.top) < self.distance(bar.bottom):
                self.setheading(90+(sign*45))
            else:
                self.setheading(270-(sign*45))
