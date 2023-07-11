from turtle import *

speed(0)
bgcolor("black")
color("red")
pensize(1)
for i in range(100):
    left(55)
    for i in range(10):
        backward(150)
        right(60)

    hideturtle()

# speed(0)
# bgcolor("black")
# pensize(3)
# for x in range(6):
#     for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
#         color(colours)
#         left(12)
#         for i in range(4):
#             forward(200)
#             left(90)
#         hideturtle()