from turtle import *
import random

tommy = Turtle()
tommy.shape("turtle")
colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4", "blue4"]
rotation = [0,90,180,270,360]
speed = 1

for number in range (200):

    if number < 10:
        tommy.pensize(number)

    tommy.pencolor(random.choice(colors))
    tommy.forward(30)
    tommy.right(random.choice(rotation))

    # zvyšujeme rychlost
    tommy.speed(speed)
    speed += 1
    
my_screen = Screen()
my_screen.exitonclick()