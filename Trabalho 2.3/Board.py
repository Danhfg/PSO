import turtle
import random
from Snake import Snake

class Board:
    def __init__(self):
        self._snakeList = []
        self._food = None
        self.changeFood()
        self._mainWindows = turtle.Screen()
        self._mainWindows.title("SnakeGame")
        self._mainWindows.bgcolor("green")
        self._mainWindows.setup(width = 600, height = 600)
        self._mainWindows.tracer(0)
        self.listen()
        #self._mainWindows.mainloop()
    
    def update(self):
        self._mainWindows.update()

    def add_snake(self, snake):
        self._snakeList.append(snake)

    def changeFood(self):
        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("red")
        food.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        self._food = food

    def listen(self):
        self._mainWindows.listen()
        for snake in self._snakeList:
            self._mainWindows.onkeypress(snake.goUp,"Up")
            self._mainWindows.onkeypress(snake.goDown,"Down")
            self._mainWindows.onkeypress(snake.goLeft,"Left")
            self._mainWindows.onkeypress(snake.goRight,"Right")

    def loop(self):
        self._mainWindows.mainloop()    

    def getSnakes(self):
        return self._snakeList       
    def getFood(self):
        return self._food

    #def add_fruit(self):   