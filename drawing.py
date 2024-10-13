# Import the necessary functions from pixart.py
from pixart import initialization, draw_grid, draw_shape_from_file
import turtle

def main():
    ''' Initialize the turtle object'''
    turta = turtle.Turtle()
    turtle.bgcolor("white")

    initialization(turta)

    '''Ask the user whether to draw a grid or load from a file'''
    choice = input("Would you like to draw a grid (G) or load pixel art from a file (F)? ")

    if choice == 'g':
        draw_grid(turta)
    elif choice == 'f':
        draw_shape_from_file(turta)
    else:
        print("Invalid choice. Please enter 'G' for grid or 'F' for file.")

    # Hide turtle and display the window
    turta.hideturtle()
    turtle.done()

# Ensure the code only runs when this script is executed directly
if __name__ == "__main__":
    main()
