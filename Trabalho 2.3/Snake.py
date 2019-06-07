import turtle

class Snake:
    def __init__(self, name):
        self._name = name
        self._head = turtle.Turtle()        
        self._head.speed(0)
        self._head.shape("square")
        self._head.color("blue")
        self._head.penup()
        self._head.goto(0,0)
        self._head.direction = "stop"
        self._segments = []

    def getName(self):
        return self._name

    def goUp(self):
        self._head.direction = "UP"
    
    def goDown(self):
        self._head.direction = "DOWN"

    def goLeft(self):
        self._head.direction = "LEFT"

    def goRight(self):
        self._head.direction = "RIGHT"

    def goto(self, x,y):
        self._head.goto(x,y)

    def eats(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        self._segments.append(new_segment)

    def move(self):
        if(self._head.direction == "UP"):
            y = self._head.ycor()
            self._head.sety(y + 20)
            
        if(self._head.direction == "DOWN"):
            y = self._head.ycor()
            self._head.sety(y - 20)
            
        if(self._head.direction == "LEFT"):
            x = self._head.xcor()
            self._head.setx(x - 20)
            
        if(self._head.direction == "RIGHT"):
            x = self._head.xcor()
            self._head.setx(x + 20)