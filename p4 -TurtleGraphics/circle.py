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
tommy.speed(50)

for number in range(1000):
    tommy.pencolor(random_color())
    tommy.circle(number)




my_screen = Screen()
my_screen.exitonclick()