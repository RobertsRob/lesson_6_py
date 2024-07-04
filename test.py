import turtle
import time
import random

screen_size = 500
circles_to_draw = 20
colours = ["green", "red", "blue", "yellow", "orange"]

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=screen_size, height=screen_size)
t = turtle.Turtle()
t.shape("circle")
t.speed(10)

def draw_circle(pos_x, pos_y, how_big, colour, size):
    t.penup()
    t.goto(pos_x, pos_y)
    t.pendown()
    t.color(colour)
    t.pensize(size)
    for _ in range(20):
        t.forward(how_big)
        t.left(18)

for _ in range(circles_to_draw):
    draw_circle(random.randint(-int(screen_size/2), int(screen_size/2)), random.randint(-int(screen_size/2), int(screen_size/2)), random.randint(1, 10), colours[random.randint(0, len(colours)-1)], random.randint(1, 6))
    time.sleep(random.randint(1, 10)/10)

turtle.done()