import turtle
import random
random.seed()
t = turtle.Turtle()
ts = turtle.getscreen()
ts.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

your_name = input("Enter your name", "What is your name?")

for x in range(80):
  t.pencolor(colors[x%4])
  t.fillcolor(colors[x%4])
  if random.randint(0,1) == 1:
	  t.penup()
  t.forward(x*4)
  t.pendown()
  t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
  t.left(90 + random.randint(0, 4))