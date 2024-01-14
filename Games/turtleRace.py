import turtle as t
import random as r
import time

# screen setup
win = t.Screen()
win.setup(1000, 600)
win.bgcolor('green')
win.title("Turtle Race")

# label
label = t.Turtle()
label.penup()
label.goto(x=0, y=200)
label.hideturtle()
label.write("Turtle Race", move=False, align="center", font=("Verdana", 35, "normal"))

# player 1
p1 = t.Turtle()
p1.shape("turtle")
p1.shapesize(2.4, 2.4)
p1.color("red")
p1.penup()
p1.goto(-450, 100)

# player 2
p2 = t.Turtle()
p2.shape("turtle")
p2.shapesize(2.4, 2.4)
p2.color("blue")
p2.penup()
p2.goto(-450, -100)

# player1 button
player1 = t.Turtle()
player1.shape("square")
player1.shapesize(3, 4)
player1.color("white")
player1.penup()
player1.goto(x=-200, y=-220)

# player2 button
player2 = t.Turtle()
player2.shape("square")
player2.shapesize(3, 4)
player2.color("white")
player2.penup()
player2.goto(x=200, y=-220)

# victory line
def p1victory():
    p1.goto(x=400, y=100)
    p1.pendown()
    p1.circle(50)
    p1.penup()
    p1.goto(x=-450, y=100)


def p2victory():
    p2.goto(x=400, y=-100)
    p2.pendown()
    p2.circle(50)
    p2.penup()
    p2.goto(x=-450, y=-100)


p1victory()
p2victory()


# player1 move
def p1Move(x, y):
    choice = [1, 2, 3, 4, 5, 6]
    dist = (r.choice(choice)) * 20
    p1.setx(p1.xcor() + dist)


# player2 move
def p2Move(x, y):
    choice = [1, 2, 3, 4, 5, 6]
    dist = (r.choice(choice)) * 20
    p2.setx(p2.xcor() + dist)

#displsy winner
def display_winner(winner):
    t.penup()
    t.goto(0,0)
    t.write(f"{winner} wins!", align="center", font=("Arial", 30, "normal"))
    time.sleep(3)
    win.bye()


# check winner
def check_winner():
    if p1.xcor() > 400:
        display_winner("Player 1")
    elif p2.xcor() > 400:
        display_winner("Player 2")


def player1_click(x, y):
    if p1.xcor() < 400 and p2.xcor() < 400:
        p1Move(x, y)
        check_winner()
        player2.onclick(p2Move)


def player2_click(x, y):
    if p1.xcor() < 400 and p2.xcor() < 400:
        p2Move(x, y)
        check_winner()
        player1.onclick(p1Move)


win.listen()
player1.onclick(player1_click)
player2.onclick(player2_click)



win.mainloop()
