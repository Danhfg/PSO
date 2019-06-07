import turtle
from Snake import Snake

class Board:
    def __init__(self):
        self._snakeList = []
        self._mainWindows = turtle.Screen()
        self._mainWindows.title("SnakeGame")
        self._mainWindows.bgcolor("green")
        self._mainWindows.setup(width = 600, height = 600)
        self._mainWindows.tracer(0)
    
    def update(self):
        self._mainWindows.update()

    def add_snake(self, snake):
        self._snakeList.append(snake)

    def listen(self):
        self._mainWindows.listen()
        self._mainWindows.onkeypress(goUp,"Up")
        self._mainWindows.onkeypress(goDown,"Down")
        self._mainWindows.onkeypress(goLeft,"Left")
        self._mainWindows.onkeypress(goRight,"Right")

    def loop(self):
        self._mainWindows.mainloop()    