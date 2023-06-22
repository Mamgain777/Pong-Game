from turtle import Turtle


class Bar:

    def __init__(self, xcor, color):
        # super().__init__()
        self.top = self.create_turtle(xcor, 0, color)
        self.bottom = self.create_turtle(xcor, -50, color)

    @staticmethod
    def create_turtle(xcor, ycor, color):
        new_turtle = Turtle('square')
        new_turtle.color(color)
        # new_turtle.setheading(heading)
        new_turtle.speed(0)
        new_turtle.shapesize(stretch_wid=2.5, stretch_len=0.8)
        new_turtle.penup()
        new_turtle.goto(x=xcor, y=ycor)
        return new_turtle

    def move_down(self):
        if self.bottom.ycor() > -260:
            self.top.goto(x=self.top.xcor(), y=self.top.ycor() - 20)
            self.bottom.goto(x=self.bottom.xcor(), y=self.bottom.ycor() - 20)

    def move_up(self):
        # ycor = self.bar.ycor()
        if self.top.ycor() < 270:
            self.top.goto(x=self.top.xcor(), y=self.top.ycor() + 20)
            self.bottom.goto(x=self.bottom.xcor(), y=self.bottom.ycor() + 20)
