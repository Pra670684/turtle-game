import turtle
import random

# Set up screen
screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("lightblue")
screen.setup(width=700, height=400)

# Draw finish line
finish_line = 300
line = turtle.Turtle()
line.penup()
line.goto(finish_line, 150)
line.pendown()
line.right(90)
line.forward(300)
line.hideturtle()

# Create turtles
colors = ["red", "green", "blue", "orange", "purple"]
turtles = []

start_y = 100
for color in colors:
    t = turtle.Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(-300, start_y)
    t.pendown()
    turtles.append(t)
    start_y -= 50

# Start race
race_on = True
while race_on:
    for t in turtles:
        distance = random.randint(1, 10)
        t.forward(distance)
        if t.xcor() >= finish_line:
            race_on = False
            winner = t.pencolor()
            print(f"The winner is {winner} turtle!")
            break

turtle.done()
