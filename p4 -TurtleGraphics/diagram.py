from turtle import *
import random
import turtle

colors = ["blue", "green", "red", "yellow", "grey", "black"]

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(2)
tommy.speed(20)
number = 0
distance_turtle = 1
while number < 1000:
    for number in range(6):
        tommy.pencolor(colors[number])
        tommy.forward(distance_turtle)
        tommy.left(80)
        distance_turtle += 1
# Lze řešit i přes modulo, přes for cyklus a pak %6 v pencolor()
my_screen = Screen()
my_screen.exitonclick()