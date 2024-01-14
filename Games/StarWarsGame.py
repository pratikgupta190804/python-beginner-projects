import turtle
import time
import random

# Set up the screen
ts = turtle.Screen()
ts.title("Snake Game by PRATIK")
ts.bgcolor("green")
ts.setup(width=600, height=600)


#snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color("red")
food.penup()
food.goto(100,0)



segments = []

#function
def go_up():
  if head.direction != "down":
    head.direction = "up"
  
def go_down():
  if head.direction != "up":
    head.direction = "down"

def go_left():
  if head.direction != "right":
    head.direction = "left"
  
def go_right():
  if head.direction != "left":
    head.direction = "right" 

def move():
  if head.direction == "up":
    head.sety(head.ycor() + 20)
    
  if head.direction == "down":
    head.sety(head.ycor() - 20)

  if head.direction == "right":
    head.setx(head.xcor() + 20)
    
  if head.direction == "left":
    head.setx(head.xcor() - 20)

# screen binding
ts.listen()
ts.onkeypress(go_up, "w")
ts.onkeypress(go_down, "s")
ts.onkeypress(go_left, "a")
ts.onkeypress(go_right, "d")

#main loop
while True:
  ts.update()

  if head.xcor()>190 or head.xcor()<-190 or head.ycor()>290 or head.ycor()<-290:
    time.sleep(1)
    head.goto(0,0)
    head.direction ="stop"
    for segment in segments:
      segment.goto(1000,1000)
      
    segments.clear()
  if head.distance(food) < 20:
    x = random.randint(-190,190)
    y = random.randint(-290,290)
    food.goto(x,y)
    
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("gray")
    new_segment.penup()
    segments.append(new_segment)
  
  for index in range(len(segments)-1,0,-1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x,y)
    
  if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x,y)

  move()

  for segment in segments:
    if segment.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction ="stop"
      
      for segment in segments:
        segment.goto(1000,1000)

      segments.clear()

  
  time.sleep(0.1)


ts.mainloop()

