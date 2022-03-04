import turtle
import colorsys

a = turtle.Turtle()
x = turtle.Screen()
x.bgcolor('black')
a.speed(0)
n = 36
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h,1,0.8)
    h += 1/n
    a.color(c)
    a.circle(180)
    a.left(10)