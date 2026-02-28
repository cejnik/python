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
tommy.speed(100)

def spirograph(gap):
    for number in range(int(360/gap)):
        tommy.pencolor(random_color())
        tommy.circle(200)
        tommy.left(gap)
   
spirograph(1)
spirograph(2)
    
my_screen = Screen()
my_screen.exitonclick()