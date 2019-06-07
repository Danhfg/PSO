import turtle

class Apple:
    def __init__(self):
        self._food = turtle.Turtle()
        self._food.speed(0)
        self._food.shape("circle")
        self._food.color("red")
        self._food.penup()
        self._food.goto(0,150)

    def goto(self, x, y):
        self._food.goto(x, y)