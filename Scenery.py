"""
Scenery,py will draw a birthday cake using turtle which will rest on a table. The cake will have one cherry and two candles



Izhan Akhtar- https://github.com/IzhanAkhtar/Scenery
Saad Shaikh- https://github.com/saaad4/scenery-.git
Yousef Faisel- https://github.com/yousufaisal/yousufsrepo.git

"""



import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create a turtle object
pen = turtle.Turtle()
pen.pensize(4)
pen.speed(2)

# Function to draw the table with 4 legs
def draw_table(length, color):
    '''This function is going to draw a table with four legs and will be as long as the user wants it to be'''
    pen.penup()
    pen.goto(-length // 2, 0)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    
    pen.forward(length)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(length)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    
    pen.end_fill()

    def draw_leg(x, y):
        pen.penup()
        pen.goto(x, y)
        pen.setheading(270)
        pen.pendown()
        pen.color(color)
        pen.begin_fill()
        
        pen.forward(100)
        pen.left(90)
        pen.forward(20)
        pen.left(90)
        pen.forward(100)
        pen.left(90)
        pen.forward(20)
        pen.end_fill()

    leg_spacing = 30
    draw_leg(-length // 2 + 10, 0)
    draw_leg(length // 2 - 30, 0)
    draw_leg(-length // 2 + 10 + leg_spacing, 0)
    draw_leg(length // 2 - 30 - leg_spacing, 0)


# Function to draw the cake
def draw_cake():

    '''This function is used to draw the main cake. It will sit on top of the table and all the layers will stack ontop of each other'''
    cake_base_y = 20
    
    pen.penup()
    pen.goto(-100, cake_base_y)
    pen.setheading(0)
    pen.pendown()
    pen.color(cake_bottom_color)
    pen.begin_fill()

    pen.forward(200)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
    pen.forward(200)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(-80, cake_base_y + 80)
    pen.setheading(0)
    pen.pendown()
    pen.color(cake_middle_color)
    pen.begin_fill()

    pen.forward(160)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.forward(160)
    pen.left(90)
    pen.forward(60)
    pen.left(90)
    pen.end_fill()

    pen.penup()
    pen.goto(-60, cake_base_y + 80 + 60)
    pen.setheading(0)
    pen.pendown()
    pen.color(cake_top_color)
    pen.begin_fill()

    pen.forward(120)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
    pen.forward(120)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
    pen.end_fill()

    # Position cherry on top of the cake
    pen.penup()
    pen.goto(0, cake_base_y + 70 + 60 + 40 + 10)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.circle(7)
    pen.end_fill()


# Function to draw the candles
def draw_candle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(candle_color)
    pen.begin_fill()
    pen.setheading(90)
    
    pen.forward(50)
    pen.right(90)
    pen.forward(5)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(5)
    pen.end_fill()

    # Candle flame
    pen.penup()
    pen.goto(x + 2.5, y + 50)
    pen.pendown()
    pen.color(flame_color)
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()


# Main part of the program
length = int(input("Enter the length of the table: "))
table_color = input("Enter the color of the table: ")
candle_color = input("Enter the color for the candles: ")
flame_color = input("Enter the color for the candle flames: ")
cake_bottom_color = input("Enter the color of bottom layer: ")
cake_middle_color = input("Enter the color of middle layer: ")
cake_top_color = input("Enter the color of top layer: ")

# Draw the table, cake, and candles
draw_table(length, table_color)
draw_cake()
draw_candle(-40, 200)
draw_candle(40, 200)

# Hide the turtle and display the window
pen.hideturtle()
screen.mainloop()
