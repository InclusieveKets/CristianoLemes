import turtle
#t = turtle.Turtle()
#for x in range(60):
#  t.forward(x*2)
#  t.left(120)

#t = turtle.Turtle()
#for x in range(100):
#  t.forward(x)
#  t.left(82.5)
#  t.backward(x)
#  t.right(45)

#t = turtle.Turtle()
#colors = ["red", "yellow", "blue", "green", 9]
#for x in range(100):
#  t.pencolor(colors[x%5])
#  t.forward(x)
#  t.left(91)

t = turtle.Turtle()
colors = ["red", "yellow", "blue", "green", 9]
for x in range(100):
  t.pencolor(colors[x%5])
  turtle.circle(x*5)
  t.forward(x)
  t.left(91)