from turtle import Turtle


class Score(Turtle):

    red = 0
    blue = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('green')
        self.goto(x=0, y=270)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(arg=f'{self.red}\tV/S\t{self.blue}', align='center', font=("Arial", 15, 'normal'))

    def increase_score(self, winner):
        if winner == 'r':
            self.red += 1
        else:
            self.blue += 1
        self.score_update()
