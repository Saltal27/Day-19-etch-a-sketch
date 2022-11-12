from turtle import Turtle, Screen

puck = Turtle()
screen = Screen()


def move_forwards():
    puck.forward(10)


def move_backwards():
    puck.backward(10)


def turn_right():
    puck.right(10)


def turn_left():
    puck.left(10)


def clear():
    puck.reset()


screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.listen()
screen.exitonclick()
