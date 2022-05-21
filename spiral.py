import turtle as hey
import random

buddy = hey.Turtle()
hey.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


#going_where = [0, 90, 180, 270]
#buddy.pensize(12)
buddy.speed("fastest")

def spin_spiralgraph(size_gap):
    for _ in range(int(360 / size_gap)):
        buddy.color(random_color())
        buddy.circle(100)
        going_currently = buddy.heading()
        buddy.setheading(going_currently + size_gap)
        buddy.circle(100)

spin_spiralgraph(5)


screen_window = hey.Screen()
screen_window.exitonclick()








##for _ in range(250):
##    buddy.color(random_color())
##    buddy.forward(33)
##    buddy.setheading(ramdom.choice(going_where)
