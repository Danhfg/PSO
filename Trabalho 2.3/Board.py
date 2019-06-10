import turtle
import random
from Snake import Snake

class Board:
    def __init__(self):
        self._snakeList = []
        self._food = turtle.Turtle()
        self._food.speed(0)
        self._food.shape("circle")
        self._food.color("red")
        self._food.penup()
        self.changeFood()

        self._comandNow = ""

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

    def getSnakeList(self):
        return self._snakeList

    def setSnakeList(self, newSnakeList):
        self._snakeList = newSnakeList        

    def changeFood(self):
        #food = turtle.Turtle()
        #food.speed(0)
        #food.shape("circle")
        #food.color("red")
        #food.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        #food.goto(x, y)
        self._food.goto(x, y)

    def positionFood(self):
        return self._food.pos()

    def setPositionFood(self, x, y):
        self._food.setpos(x, y)

    def _upPressioned(self):
        self._comandNow = "Up"
    
    def _downPressioned(self):
        self._comandNow = "Down"
        
    def _leftPressioned(self):
        self._comandNow = "Left"
        
    def _rightPressioned(self):
        self._comandNow = "Right"

    def buttonPressioned(self):
        self._mainWindows.onkeypress(self._upPressioned,"Up")
        self._mainWindows.onkeypress(self._downPressioned,"Down")
        self._mainWindows.onkeypress(self._leftPressioned,"Left")
        self._mainWindows.onkeypress(self._rightPressioned,"Right")
        return self._comandNow

    def listen(self):
        self._mainWindows.listen()
        for snake in self._snakeList:
            self._mainWindows.onkeypress(snake.goUp,"Up")
            self._mainWindows.onkeypress(snake.goDown,"Down")
            self._mainWindows.onkeypress(snake.goLeft,"Left")
            self._mainWindows.onkeypress(snake.goRight,"Right")
            
    def listenEspecificSnake(snake):
        self._mainWindows.listen()
        self._mainWindows.onkeypress(snake.goUp,"Up")
        self._mainWindows.onkeypress(snake.goDown,"Down")
        self._mainWindows.onkeypress(snake.goLeft,"Left")
        self._mainWindows.onkeypress(snake.goRight,"Right")

    def loop(self):
        self._mainWindows.mainloop()    

    def getFood(self):
        return self._food

    def listPlayersNames(self):
        playersNames = []

        for snake in _snakeList:
            playersNames.append(snake.getName())

        return playersNames