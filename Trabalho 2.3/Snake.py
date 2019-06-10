import turtle
import random

class Snake:
    def __init__(self, name):
        self._name = name
        self._head = turtle.Turtle()        
        self._head.speed(0)
        self._head.shape("square")
        cor = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        self._head.color(cor[0])
        #print(cor[0])
        self._head.penup()
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        self._head.goto(x,y)
        self._head.direction = "stop"
        self.segments = []

    def getName(self):
        return self._name

    def getHead(self):
        return self._head

#    def getSegments(self):
#        return self._segments

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

    def setDirection(self,direction):
        self._head.direction("Stop")


    def eats(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        self.segments.append(new_segment)

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