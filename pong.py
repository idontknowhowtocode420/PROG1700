import turtle
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
wn.title("pong")
 
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.speed(10)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
 
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_a.speed(10)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.09
ball.dy = 0.09

player_a = 0
player_b = 0
score_a = 0 
score_b = 0
score_board = turtle.Turtle()
score_board.speed = 0
score_board.shape("square")
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0,260)
score_board.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("courier",24,"normal"))
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
 
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
 
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
 
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
 
#keybind
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
 
 
 
#main
playing=True
while playing:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1
    
    
    if ball.xcor() > 390:
        score_a += 1
        score_board.clear()
        score_board.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("courier",24,"normal"))
    elif ball.xcor() < -400:
        score_b += 1
        score_board.clear()
        score_board.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("courier",24,"normal"))
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx = ball.dx * - 1
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx = ball.dx * - 1













while True:
    wn.update()