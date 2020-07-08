# Simple Ping-Pong game in Python
# Very sort of old-school game, not too many classes, etc.
# References: @TokyoEdTech

# Turtle Graphics
import turtle
import os

win = turtle.Screen()
win.title("Ping Pong by Julian Murillo")

win.bgcolor("blue")
win.setup(width = 900, height = 700)
win.tracer(0)

# Scoring Points
score_1 = 0
score_2 = 0

# Create Paddle for player 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("black")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)

paddle_1.penup()
paddle_1.goto(-350,0)

# Create Paddle for player 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("black")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)

paddle_2.penup()
paddle_2.goto(350,0)


# Create Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx = 3.5
ball.dy = 1

# Pen...drawing/writing dynamic graphic
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,310)
pen.write("Player 1: 0 Player 2: 0", align="center", font = ("Courier",24,"italic"))


# Functions for moving player paddles up and down:
def paddle_1_up():
    y = paddle_1.ycor()
    y+=40
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y-=40
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y+=40
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y-=40
    paddle_2.sety(y)

# Keyboard binding for paddles (which keys to press to move paddles)
win.listen()
win.onkey(paddle_1_up, "w")
win.onkey(paddle_1_down,"d")

win.onkey(paddle_2_up, "Up")
win.onkey(paddle_2_down,"Down")

# Main loop for the game
while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border check... we don't want ball magically floating off the screen

    # Top/bottom bounds
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1
        # access sound we downloaded from the internet and add '&' so there isn't a delay
        os.system("afplay PongSound.mp3&")


    if ball.ycor() < -335:
        ball.sety(-335)
        ball.dy *= -1
        os.system("afplay PongSound.mp3&")

    # Side bounds
    if ball.xcor() > 430:
        ball.goto(0,0)
        ball.dx *= -1
        score_1+=1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1,score_2), align="center", font=("Courier", 24, "normal"))
        os.system("afplay bounce.wav&")

    if ball.xcor() < -440:
        ball.goto(0,0)
        ball.dx *= -1
        score_2+=1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score_1,score_2), align="center", font=("Courier", 24, "normal"))
        os.system("afplay bounce.wav&")

    # Ball bouncing off of paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40):
        ball.setx(340)
        # Reverse direciton of ball after collision
        ball.dx *= -1
        os.system("afplay PongSound.mp3&")


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40):
        ball.setx(-340)
        # Reverse direction of ball after collision
        ball.dx *= -1
        os.system("afplay PongSound.mp3&")




