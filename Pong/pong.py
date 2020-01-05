import turtle
import winsound
wn = turtle.Screen()
wn.title("Pong by @arian99")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score_1 = 0
score_2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)  # speed of animation
paddle_1.shape("square")
paddle_1.color("red")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-375, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)  # speed of animation
paddle_2.shape("square")
paddle_2.color("green")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(+370, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3  # x movement
ball.dy = 0.3

# Pen
pen = turtle.Turtle()
pen.speed(0)  # animation speed
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0       Player2: 0", align="center",
          font=("Courier", 20, "normal"))


# Function for moving the paddles
def paddle_1_up():
    y = paddle_1.ycor()  # ycor() returns the y coordinate
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()  # ycor() returns the y coordinate
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()  # ycor() returns the y coordinate
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()  # ycor() returns the y coordinate
    y -= 20
    paddle_2.sety(y)


# Keyboard binding
wn.listen()  # this says to listen for a keyboard input
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

# Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if (ball.xcor() > 390) and (score_1 < 5 and score_2 < 5):
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player1:{}       Player2: {}".format(
            score_1, score_2), align="center", font=("Courier", 20, "normal"))

    if (ball.xcor() < -390) and (score_1 < 5 and score_2 < 5):
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player1:   {}       Player2:{}".format(
            score_1, score_2), align="center", font=("Courier", 20, "normal"))
    # Paddle and ball collisions
    if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < paddle_2.ycor() + 55 and ball.ycor() > paddle_2.ycor() - 55):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("pp", winsound.SND_ASYNC)

    if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < paddle_1.ycor() + 55 and ball.ycor() > paddle_1.ycor() - 55):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("pp", winsound.SND_ASYNC)

    if score_1 == 5:
        pen.clear()
        pen.write("Player 1 win!!!", align="center",
                  font=("Courier", 20, "normal"))
        ball.dx = 0
        ball.dy = 0

    if score_2 == 5:
        pen.clear()
        pen.write("Player 2 win!!!", align="center",
                  font=("Courier", 20, "normal"))
        ball.dx = 0
        ball.dy = 0
