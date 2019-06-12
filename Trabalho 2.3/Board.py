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

        self.mainWindows = turtle.Screen()
        self.mainWindows.title("SnakeGame")
        self.mainWindows.bgcolor("green")
        self.mainWindows.setup(width = 600, height = 600)
        self.mainWindows.tracer(0)
        self.listen()
        #self.mainWindows.mainloop()
    
    def update(self):
        self.mainWindows.update()
    
    def update2(self, data):
        aux = data.copy()
        if len(aux.keys()) > 4:
            for i in aux:
                print(aux[i])
                for snake in self._snakeList:
                    if aux[i] == snake.getName():
                        if aux[i]['direction'] == 'A':
                            snake.goLeft()
                        if aux[i]['direction'] == 'S':
                            snake.goDown()
                        if aux[i]['direction'] == 'D':
                            snake.goRight()
                        if aux[i]['direction'] == 'W':
                            snake.goUp()
        self.mainWindows.update()

    def add_snake(self, snake):
        self._snakeList.append(snake)

    def getSnakeList(self):
        return self._snakeList

    def getSnake(self, snakeName):
        for i in self._snakeList:
            if i.getName() == snakeName:
                return i

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
        self.mainWindows.onkeypress(self._upPressioned,"Up")
        self.mainWindows.onkeypress(self._downPressioned,"Down")
        self.mainWindows.onkeypress(self._leftPressioned,"Left")
        self.mainWindows.onkeypress(self._rightPressioned,"Right")
        return self._comandNow

    def listen(self):
        self.mainWindows.listen()
        for snake in self._snakeList:
            self.mainWindows.onkeypress(snake.goUp,"Up")
            self.mainWindows.onkeypress(snake.goDown,"Down")
            self.mainWindows.onkeypress(snake.goLeft,"Left")
            self.mainWindows.onkeypress(snake.goRight,"Right")
            
    def listenEspecificSnake(snake):
        self.mainWindows.listen()
        self.mainWindows.onkeypress(snake.goUp,"Up")
        self.mainWindows.onkeypress(snake.goDown,"Down")
        self.mainWindows.onkeypress(snake.goLeft,"Left")
        self.mainWindows.onkeypress(snake.goRight,"Right")

    def loop(self):
        self.mainWindows.mainloop()    

    def getFood(self):
        return self._food

    def setFood(self, x, y):
        self._food.goto(x,y)

    def listPlayersNames(self):
        playersNames = []

        for snake in _snakeList:
            playersNames.append(snake.getName())

        return playersNames