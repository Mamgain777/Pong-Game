import time
from turtle import Screen
from bar import Bar
from ball import Ball
from score import Score
from round import Round

sc = Screen()
sc.setup(width=900, height=600)
sc.bgcolor('black')
sc.tracer(0)

# Creating Bars
left_bar = Bar(-420, 'red')
right_bar = Bar(420, 'blue')

# Creating Ball
play_ball = Ball()

# Creating Scorecard
score_card = Score()

# Creating Center Message
msg = Round()

# Setting Screen Control
sc.listen()
sc.onkey(left_bar.move_up, 'w')
sc.onkey(left_bar.move_down, 's')
sc.onkey(right_bar.move_up, 'Up')
sc.onkey(right_bar.move_down, 'Down')
# sc.update()

# Game Code
game_is_on = True
i = 1
play_ball.start_round('blue')
score_card.score_update()
msg.display()


while game_is_on:
    # Speed Setting
    time.sleep(play_ball.ball_speed)
    sc.update()
    # print("running")

    # Start Round
    # play_ball.start_round('right')
    play_ball.move_ball()

    #  check for collision
    # With ball
    play_ball.bar_collision(left_bar, -410, -1)
    play_ball.bar_collision(right_bar, 392, 1)
    # With wall
    if play_ball.ycor() >= 281 or play_ball.ycor() <= -273:
        if play_ball.heading() == 45:
            play_ball.setheading(315)
        elif play_ball.heading() == 135:
            play_ball.setheading(225)
        elif play_ball.heading() == 225:
            play_ball.setheading(135)
        else:
            play_ball.setheading(45)

    # Ball Missed
    if play_ball.xcor() > 450:
        score_card.increase_score('r')  # Red won
        if score_card.red == 2:
            game_is_on = False
            msg.finish('RED')
        else:
            msg.display()
            play_ball.start_round('red')

    if play_ball.xcor() < -450:
        score_card.increase_score('b')  # Blue won
        if score_card.blue == 2:
            game_is_on = False
            msg.finish("BLUE")
        else:
            msg.display()
            play_ball.start_round('blue')

sc.exitonclick()
