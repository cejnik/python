from turtle import *
import random
import turtle

turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(2)
tommy.speed(1)
tommy.pen(fillcolor=random_color())

tommy.begin_fill()
for number in range (4):
    tommy.forward(100)
    tommy.left(90)
tommy.end_fill()


my_screen = Screen()
my_screen.exitonclick()