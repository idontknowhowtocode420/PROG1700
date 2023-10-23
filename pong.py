import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(0)

paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.shapesize(stretch_vid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
