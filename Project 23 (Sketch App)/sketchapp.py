from turtle import Turtle, Screen

flippy = Turtle()
screen = Screen()

def move_forward():
    flippy.fd(10)

def move_backward():
    flippy.bk(10)

def move_left():
    flippy.lt(10)

def move_right():
    flippy.rt(10)

def clear_screen():
    flippy.clear()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()