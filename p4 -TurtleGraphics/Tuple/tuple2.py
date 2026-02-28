# Praktické využití tuple
from turtle import *
import random
import turtle

# Změna barevného modu - > důležité naimportovat turtle
turtle.colormode(255)

tommy = Turtle()
tommy.shape("turtle")

def random_color ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color



rotation = [0,90,180,270,360]
speed = 1

for number in range (200):

    if number < 10:
        tommy.pensize(number)

    tommy.pencolor(random_color())
    tommy.forward(30)
    tommy.right(random.choice(rotation))

    # zvyšujeme rychlost
    tommy.speed(speed)
    speed += 1
    
my_screen = Screen()
my_screen.exitonclick()