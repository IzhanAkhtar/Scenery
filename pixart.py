







PIXEL_SIZE = 30  # Adjusted to match pixel size from the image
ROWS = 20
COLUMNS = 20
DEFAULT_PEN_COLOR = 'black'
DEFAULT_PIXEL_COLOR = 'white'

def initialization(turta):
    '''Sets the speed, pencolor, and the starting point of the turtle to start drawing'''
    turta.speed(9)
    turta.penup()
    turta.goto(-PIXEL_SIZE * COLUMNS / 2, PIXEL_SIZE * ROWS / 2)  # Start in the top left of the grid
    turta.pendown()
    turta.pencolor(DEFAULT_PEN_COLOR)
    turta.fillcolor(DEFAULT_PIXEL_COLOR)

def get_color(char):
    '''Returns a corresponding color for the provided character'''
    color_dict = {
        '0': 'black',
        '1': 'white',
        '2': 'red',
        '3': 'yellow',
        '4': 'orange',
        '5': 'green',
        '6': 'yellowgreen',
        '7': 'sienna',
        '8': 'tan',
        '9': 'gray',
        'A': 'darkgray'
    }
    return color_dict.get(char, None)

def draw_color_pixel(color_string, turta):
    '''Draws a single pixel of the specified color'''
    turta.fillcolor(color_string)
    turta.begin_fill()
    for _ in range(4):
        turta.forward(PIXEL_SIZE)
        turta.right(90)
    turta.end_fill()

def draw_pixel(char, turta):
    '''Draws a pixel using the character's color code'''
    color = get_color(char)
    if color is None:
        return False
    draw_color_pixel(color, turta)
    return True

def draw_line_from_string(string, turta):
    '''Draws a line of pixels from a string of color codes'''
    for char in string:
        if not draw_pixel(char, turta):
            return False
        turta.penup()
        turta.forward(PIXEL_SIZE)
        turta.pendown()
    return True

def draw_shape_from_string(turta, lines):
    '''Draws a shape from a list of strings where each string represents a line of pixel color codes'''
    for line in lines:
        if not draw_line_from_string(line, turta):
            print("Invalid color in input! Stopping.")
            break
        turta.penup()
        turta.setheading(270)  # Move down to the next row
        turta.forward(PIXEL_SIZE)
        turta.setheading(180)  # Return to the start of the row
        turta.setx(-PIXEL_SIZE * COLUMNS / 2)
        turta.setheading(0)
        turta.pendown()

def draw_grid(turta):
    '''Draws a checkerboard grid of alternating red and black colors'''
    for row in range(ROWS):
        if row % 2 == 0:
            line = '02' * (COLUMNS // 2)
        else:
            line = '20' * (COLUMNS // 2)
        draw_line_from_string(line, turta)
        turta.penup()
        turta.setheading(270)
        turta.forward(PIXEL_SIZE)
        turta.setheading(180)
        turta.setx(-PIXEL_SIZE * COLUMNS / 2)
        turta.setheading(0)
        turta.pendown()


def draw_shape_from_file(turta):
    '''Prompts the user for a file name, reads the file content, and generates the image using draw_shape_from_string.'''
    file_path = input("Enter the path of the pixel art file (e.g., 'drawing03.txt'): ")

    try:
        with open(file_path, 'r') as f:
            lines = f.read().splitlines()  # Read and split file content into lines
            draw_shape_from_string(turta, lines)  # Pass lines to draw_shape_from_string to generate the image
    except FileNotFoundError:
        print(f"File {file_path} not found!")

