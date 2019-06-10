import turtle
import random

class Apple:
    def __init__(self):
        self._food = turtle.Turtle()
        self._food.speed(0)
        self._food.shape("circle")
        self._food.color("red")
        self._food.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self._food.goto(x,y)

    def goto(self, x, y):
        self._food.goto(x, y)