import turtle
import time
import random

# set up Main Windows 

delay = 0.1

mainWindows = turtle.Screen()
mainWindows.title("SnakeGame")
mainWindows.bgcolor("green")
mainWindows.setup(width = 600, height = 600)
mainWindows.tracer(0)

# Head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")

head.penup()
head.goto(0,0)
head.direction = "stop"


# food for snake
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,150)

# function to set dirction

def goUp():
    head.direction = "UP"
    
def goDown():
    head.direction = "DOWN"

def goLeft():
    head.direction = "LEFT"

def goRight():
    head.direction = "RIGHT"

    


#funtion for movement

def move():
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
        
mainWindows.listen()

mainWindows.onkeypress(goUp,"Up")

mainWindows.onkeypress(goDown,"Down")

mainWindows.onkeypress(goLeft,"Left")

mainWindows.onkeypress(goRight,"Right")

segments = []
        
while (True):
    
    mainWindows.update()
    if(head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290):
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

      for segment in segments:
          segment.goto(1000, 1000)
      segments.clear()    
    
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

    for index in range(len(segments)-1, 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if(len(segments) > 0):
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    move()

    for segment in segments:
        if (segment.distance(head) < 20):
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            for segment in segments:
              segment.goto(1000, 1000)
            segments.clear()  
    
    time.sleep(delay)

mainWindows.mainloop()

