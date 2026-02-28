from turtle import *
from turtle import Turtle
import time
import random

# Variables
score = 0
highest_score = 0


screen = Screen()
screen.bgcolor("green")
screen.title("Snake Game")
screen.setup(width=600, height=600)


screen.tracer(False)

# Score:
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("white")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0,265)
score_sign.write(f"Skóre: 0   Nejvyšší skóre: 0", align="center", font=("Arial", 12))
# Hadí hlava
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0,0)
head.direction = "stop"

# Jablko
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100,100)

# Body Patrs
body_parts = []

# Funkce
def move():
    if head.direction == "up":
        # Současná souřadnice y
        y = head.ycor()
        # Přenastav y o "20"
        head.sety(y + 20)

    if head.direction == "down":
        # Současná souřadnice y
        y = head.ycor()
        # Přenastav y o "20"
        head.sety(y - 20)

    if head.direction == "left":
        # Současná souřadnice y
        x = head.xcor()
        # Přenastav y o "20"
        head.setx(x - 20)

    if head.direction == "right":
        # Současná souřadnice y
        x = head.xcor()
        # Přenastav y o "20"
        head.setx(x + 20)      

def move_up():
    if head.direction !="down":
        head.direction = "up"
    
def move_down():
    if head.direction !="up":
        head.direction = "down"

def move_left():
    if head.direction !="right":
        head.direction = "left"

def move_right():
    if head.direction !="left":
        head.direction = "right"

# Ovládání
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")



# Main cycle
while True:
    screen.update()

    # Kontrola kolize s hranou obrazovky
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(2)
        head.goto(0,0)
        head.direction = "stop"
        
        # Skryjeme
        for one_body_part in body_parts:
            one_body_part.goto(1500,1500)
        
        body_parts.clear()

        # Score reset
        score = 0

        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 12))


    # Kolize hlavy s jablkem
    if head.distance(apple) <20:
        
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        apple.goto(x, y)

        # Přidání části těla
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("grey")
        new_body_part.penup()
        body_parts.append(new_body_part)

        score += 10

        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 12))
        

    # Další čtverce
    for index in range(len(body_parts)-1, 0, -1):
        x = body_parts[index-1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x,y)

    # První čtverec za tělem
    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x,y)
    move()

    # Hlava narazila do těla
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0,0)
            head.direction = "stop"

            # Skrytá části těl
            for one_body_part in body_parts:
                one_body_part.goto(1500,1500)
        
            body_parts.clear()
                    # Score reset
            score = 0

            score_sign.clear()
            score_sign.write(f"Skóre: {score} Nejvyšší skóre: {highest_score}", align="center", font=("Arial", 12))

    time.sleep(0.1)
    

screen.exitonclick()