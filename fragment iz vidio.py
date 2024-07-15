from turtle import *
from random import choice

teleport = teleport
def fractal(size, func):
    for i in range(en):
        func(size)
        left(360 / en)


def hexagon(size):
    for i_ in range(6):
        forward(size)
        left(60)


def romb(size):
    for i_ in range(2):
        forward(size)
        right(35)
        forward(size)
        right(145)


def squer(size):
    for i_ in range(4):
        forward(size)
        left(90)


def tringel(size):
    for i_ in range(3):
        forward(size)
        left(120)


Screen().bgcolor("black")
en = 24
col = ["white", "yellow", "green", "blue", "cyan2", "magenta", "DarkViolet", "chartreuse"]
speed(100)
color(choice(col))
fractal(100,squer)
left(45)
penup()
forward(250)  
pendown()
color("green")
fractal(120,tringel)
color("red")
penup()
right(220)
forward(400)
pendown()
fractal(60,hexagon)
color("yellow")
penup()
right(220)
forward(500)
pendown()
fractal(60,hexagon)
color("blue")
right(140)
penup()
forward(400)
pendown()
fractal(120,tringel)
color("purple")
teleport(-420, 0)
fractal(60, squer)
teleport(420, 0)
color("orange")
fractal(60, squer)
teleport(420, -200)
color("cyan2")
fractal(45, romb)
teleport(420, 200)
color("brown")
fractal(40, romb)
color("magenta")
teleport(-420, 200)
fractal(40, romb)
color("MediumAquamarine")
teleport(-420, -200)
fractal(40, romb)
teleport(0, -200)
color("OliveDrab2")
fractal(30, hexagon)
color("pink")
teleport(0, 200)
fractal(30, hexagon)
exitonclick()
