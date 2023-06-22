from turtle import Turtle
import time


class Round(Turtle):

    round = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('green')

    def display(self):
        self.round += 1
        self.write(arg=f'ROUND {self.round}', align='center', font=("Arial", 25, 'normal'))
        time.sleep(5)
        self.clear()

    def finish(self, winner):
        # self.goto(x=0, y=0)

        self.write(arg=f'GAME OVER\n {winner} WON', align='center', font=("Arial", 25, 'normal'))
