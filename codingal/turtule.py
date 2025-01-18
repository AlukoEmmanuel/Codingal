import turtle
turtle.Screen().bgcolor("Orange")

sc = turtle.Screen()
sc.setup(300, 300)

turtle.title("Welcome to Turtle window ")

board = turtle.Turtle()

for i in range(8):
    board.forward(100)
    board.right(90)
    i = i+1
turtle.done()