from turtle import *
from random import randint

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(2)

# for _ in range (0,4):
#     tommy.forward(100)
#     tommy.right(90)


# for _ in range (0,100):
#     tommy.forward(10)
#     tommy.penup()
#     tommy.forward(10)
#     tommy.pendown()
#     tommy.left(randint(0,180))

# moves = 3
# angle = 360/moves
# forward_turtle = 100
def draw(moves, forward_turtle):
    while moves != 9:
        for _ in range (moves):
            tommy.forward(forward_turtle)
            tommy.right(360/moves)
        moves += 1
draw(3,100)
        



# tommy.forward(100)
# tommy.right(90)
# tommy.forward(100)
# tommy.right(90)
# tommy.forward(100)
# tommy.right(90)
# tommy.forward(100)
# tommy.right(90)


    


    







my_screen = Screen()
my_screen.exitonclick()