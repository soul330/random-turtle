import turtle as t
#from turtle import Turtle, Screen
import random

tur = t.Turtle()
t.colormode(255)
my_screen = t.Screen()
tur.pensize(10)
tur.speed("fastest")
directions = [0, 90, 180, 270]

def my_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g ,b)
    return my_color

#colors = ["orchid", "green", "light sky blue", "yellow", "rosy brown"]
for _ in range(200):
    tur.color(my_color())
    tur.shape("turtle")
    tur.forward(30)
    tur.setheading(random.choice(directions))




my_screen.exitonclick()








# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tur.forward(100)
#         tur.right(angle)
#
# for draw_shape_n in range(3, 11):
#     tur.color(random.choice(colors))
#     draw_shape(draw_shape_n)
