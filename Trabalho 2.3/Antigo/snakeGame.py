import turtle
import time
import random

class Snake:
    def __init__(self):
        self._name = name
        self._head = turtle.Turtle()          
        self._head.speed(0)
        self._head.shape("square")
        self._head.color("blue")
        self._head.penup()
        self._head.goto(0,0)
        self._head.direction = "stop"
        self._segments = [] 



# set up Main Windows 

delay = 0.1

mainWindows = turtle.Screen()
mainWindows.title("SnakeGame")
mainWindows.bgcolor("green")
mainWindows.setup(width = 600, height = 600)
mainWindows.tracer(0)


heads = []
for i in range(2):
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("blue")

    head.penup()
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    head.goto(x,y)
    head.direction = "stop"
    heads.append(head)


# Head of the snake
"""
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")

head.penup()
head.goto(0,0)
head.direction = "stop"
"""

# food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
x = random.randint(-290, 290)
y = random.randint(-290, 290)
food.goto(x, y)

# function to set dirction

def goUp(pos=0):
    print("A")
    heads[pos].direction = "UP"
    
def goDown(pos=0):
    heads[pos].direction = "DOWN"

def goLeft(pos=0):
    heads[pos].direction = "LEFT"

def goRight(pos=0):
    heads[pos].direction = "RIGHT"

    


#funtion for movement

def move():
    """
    if(head.direction == "UP"):
        y = head.ycor()
        head.sety(y + 20)
        
    if(head.direction == "DOWN"):
        y = head.ycor()
        head.sety(y - 20)
        
    if(head.direction == "LEFT"):
        x = head.xcor()
        head.setx(x - 20)
        
    if(head.direction == "RIGHT"):
        x = head.xcor()
        head.setx(x + 20)
    """

    for i in range(len(heads)):
        if(heads[i].direction == "UP"):
            y = heads[i].ycor()
            heads[i].sety(y + 20)
            
        if(heads[i].direction == "DOWN"):
            y = heads[i].ycor()
            heads[i].sety(y - 20)
            
        if(heads[i].direction == "LEFT"):
            x = heads[i].xcor()
            heads[i].setx(x - 20)
            
        if(heads[i].direction == "RIGHT"):
            x = heads[i].xcor()
            heads[i].setx(x + 20)

        
mainWindows.listen()

#for i in range(len(heads)):
mainWindows.onkeypress(goUp(),"Up")

mainWindows.onkeypress(goDown(),"Down")

mainWindows.onkeypress(goLeft(),"Left")

mainWindows.onkeypress(goRight(),"Right")

segments = [[],[]]
        
while (True):
    
    mainWindows.update()
    for i in range(len(heads)):
        if(heads[i].xcor() > 290 or heads[i].xcor() < -290 or heads[i].ycor() > 290 or heads[i].ycor() < -290):
        #time.sleep(1)
            heads[i].goto(0,0)
            heads[i].direction = "stop"

            for segment in segments[i]:
                segment.goto(1000, 1000)
            segments[i].clear()
    """
    if(head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
      #time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

      for segment in segments:
          segment.goto(1000, 1000)
      segments.clear()  
    """  
    aux = False
    for i in range(len(heads)):
        if heads[i].distance(food) < 20 and ~aux:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            # adding body of the snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("red")
            new_segment.penup()
            segments[i].append(new_segment)
            aux = True



    """
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # adding body of the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
    """

    for i in range(len(heads)):
        for index in range(len(segments[i])-1, 0 , -1):
            x = segments[i][index-1].xcor()
            y = segments[i][index-1].ycor()
            segments[i][index].goto(x, y)
    """
    for index in range(len(segments)-1, 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    """
    for i in range(len(segments)):
        if(len(segments[i]) > 0):
            x = heads[i].xcor()
            y = heads[i].ycor()
            segments[i][0].goto(x, y)
    """
    if(len(segments) > 0):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    """ 
    move()

    for i in range(len(heads)):
        for segment in segments[i]:
            if (segment.distance(heads[i]) < 20):
                time.sleep(1)
                heads[i].goto(0, 0)
                heads[i].direction = "Stop"

                for segment in segments[i]:
                    segment.goto(1000, 1000)
                segments[i].clear()  
    """
    for segment in segments:
        if (segment.distance(head) < 20):
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
              segment.goto(1000, 1000)
            segments.clear()  
    """
    time.sleep(delay)

mainWindows.mainloop()

