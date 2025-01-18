import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Polygon Drawing")
screen.bgcolor("lightblue")  # Set background color

# Function to draw an equilateral triangle
def draw_triangle():
    triangle = turtle.Turtle()
    triangle.color("green")
    triangle.begin_fill()
    for _ in range(3):
        triangle.forward(100)
        triangle.left(120)
    triangle.end_fill()
    triangle.hideturtle()

# Function to draw a rectangle
def draw_rectangle():
    rectangle = turtle.Turtle()
    rectangle.color("red")
    rectangle.begin_fill()
    for _ in range(2):
        rectangle.forward(150)
        rectangle.left(90)
        rectangle.forward(100)
        rectangle.left(90)
    rectangle.end_fill()
    rectangle.hideturtle()

# Function to draw a hexagon
def draw_hexagon():
    hexagon = turtle.Turtle()
    hexagon.color("blue")
    hexagon.begin_fill()
    for _ in range(6):
        hexagon.forward(80)
        hexagon.left(60)
    hexagon.end_fill()
    hexagon.hideturtle()

# Main program
def main():
    # Position for drawing triangle
    draw_triangle()

    # Move to position for rectangle
    rectangle_turtle = turtle.Turtle()
    rectangle_turtle.penup()
    rectangle_turtle.goto(-200, -100)
    rectangle_turtle.pendown()
    rectangle_turtle.hideturtle()
    draw_rectangle()

    # Move to position for hexagon
    hexagon_turtle = turtle.Turtle()
    hexagon_turtle.penup()
    hexagon_turtle.goto(200, -100)
    hexagon_turtle.pendown()
    hexagon_turtle.hideturtle()
    draw_hexagon()

    # Keep the window open until clicked
    screen.mainloop()

if __name__ == "__main__":
    main()
