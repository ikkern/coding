import turtle

# --- Name Input Interface ---
print("Welcome to Pong — Apple Edition 🍏")
player_a_name = input("Enter Player A's name (W/S): ") or "Player A"
player_b_name = input("Enter Player B's name (↑/↓): ") or "Player B"

# Global ball speed
ballSpeed = 3.

# Set up the screen
wn = turtle.Screen()
wn.title("Pong — Apple Edition 🍏")
wn.bgcolor("#1c1c1e")  # Apple dark mode style
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle Style
def create_paddle(x_pos):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("#d1d1d6")  # Light gray
    paddle.shapesize(stretch_wid=5.5, stretch_len=1)
    paddle.penup()
    paddle.goto(x_pos, 0)
    return paddle

# Paddles
paddle_a = create_paddle(-350)
paddle_b = create_paddle(350)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#0a84ff")  # Apple-style blue
ball.penup()
ball.goto(0, 0)
ball.dx = ballSpeed
ball.dy = ballSpeed

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("#f2f2f7")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"{player_a_name}: 0  {player_b_name}: 0", align="center", font=("Arial", 22, "bold"))

# Center Divider
divider = turtle.Turtle()
divider.color("#3a3a3c")
divider.hideturtle()
divider.penup()
divider.goto(0, 300)
divider.setheading(-90)
for _ in range(30):
    divider.pendown()
    divider.forward(10)
    divider.penup()
    divider.forward(10)

# Paddle movement functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        paddle_b.sety(y - 20)

# Controls
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce on top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right side miss
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -ballSpeed
        ball.dy = ballSpeed
        score_a += 1
        pen.clear()
        pen.write(f"{player_a_name}: {score_a}  {player_b_name}: {score_b}", align="center", font=("Arial", 22, "bold"))

    # Left side miss
    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ballSpeed
        ball.dy = ballSpeed
        score_b += 1
        pen.clear()
        pen.write(f"{player_a_name}: {score_a}  {player_b_name}: {score_b}", align="center", font=("Arial", 22, "bold"))

    # Paddle B collision
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 55 < ball.ycor() < paddle_b.ycor() + 55):
        ball.setx(340)
        ball.dx *= -1.2
        ball.dy *= 1.05

    # Paddle A collision
    elif (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 55 < ball.ycor() < paddle_a.ycor() + 55):
        ball.setx(-340)
        ball.dx *= -1.2
        ball.dy *= 1.05
