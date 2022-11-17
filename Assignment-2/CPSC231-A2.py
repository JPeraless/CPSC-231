# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: T01, Wei
# Name: Jose Perales Rivera
# ID: 30143354
# Date: 20/10/2021

##################################################################
# Assignment 2
# Basic graphical calculator that uses the turtle library to draw
# expressions based on input from the user.
##################################################################

from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
AXIS_COLOR = "black"


def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """
    # determine which will be the color of the expression
    if equation_counter % 3 == 2:
        return "blue"
    elif equation_counter % 3 == 1:
        return "green"
    else:
        return "red"



def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """
    screen_x = x_origin + (x * ratio)
    screen_y = y_origin + (y * ratio)

    return screen_x, screen_y


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    # smallest integer x value
    min_x = int(floor((0 - x_origin) / ratio))

    # largest integer x value
    max_x = int(ceil((WIDTH - x_origin) / ratio))

    return min_x, max_x


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    # smallest integer y value
    min_y = int(floor((0 - y_origin) / ratio))

    # largest integer y value
    max_y = int(ceil((WIDTH - y_origin) / ratio))

    return min_y, max_y


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between tow pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """
    pointer.up()
    pointer.goto(screen_x1, screen_y1)
    pointer.down()
    pointer.goto(screen_x2, screen_y2)


def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # uses the draw_line function to draw one tick
    draw_line(pointer, screen_x, screen_y - 10, screen_x, screen_y + 10)


def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.up()
    pointer.goto(screen_x - 7, screen_y - 20)
    pointer.down()
    pointer.write(label_text)
    pointer.up()


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw a y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # uses the draw_line function to draw one tick
    draw_line(pointer, screen_x - 10, screen_y, screen_x + 10, screen_y)


def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw a y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.up()
    pointer.goto(screen_x - 13, screen_y)
    pointer.down()
    pointer.write(label_text)
    pointer.up()


def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # get the minimum and maximum x values
    lower_x, upper_x = calc_minmax_x(x_origin, ratio)

    # draw the ticks and labels
    for i in range(lower_x, upper_x + 1):
        x_coordinate, y_coordinate = calc_to_screen_coord(i, 0, x_origin, y_origin, ratio)

        draw_x_axis_tick(pointer, x_coordinate, y_coordinate)
        draw_x_axis_label(pointer, x_coordinate, y_coordinate, i)

    # get the coordinates to draw the line
    x1, y1 = calc_to_screen_coord(lower_x, 0, x_origin, y_origin, ratio)
    x2, y2 = calc_to_screen_coord(upper_x, 0, x_origin, y_origin, ratio)

    # change the pointer color to black and draw the line
    pointer.color("#000000")
    draw_line(pointer, x1, y1, x2, y2)


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw a y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # get the minimum and maximum y values
    lower_y, upper_y = calc_minmax_y(y_origin, ratio)

    # draw the ticks and labels
    for i in range(lower_y, upper_y + 1):
        x_coordinate, y_coordinate = calc_to_screen_coord(0, i, x_origin, y_origin, ratio)

        draw_y_axis_tick(pointer, x_coordinate, y_coordinate)
        draw_x_axis_label(pointer, x_coordinate, y_coordinate, i)

    # get the coordinate to draw the line
    x1, y1 = calc_to_screen_coord(0, lower_y, x_origin, y_origin, ratio)
    x2, y2 = calc_to_screen_coord(0, upper_y, x_origin, y_origin, ratio)

    # change the pointer color to black and draw the line
    pointer.color("#000000")
    draw_line(pointer, x1, y1, x2, y2)


def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    # set delta
    delta = 0.1

    # get the minimum and maximum x values
    lower_x, upper_x = calc_minmax_x(x_origin, ratio)

    while lower_x <= upper_x:
        # get the y values for both x values
        y1 = calc(expr, lower_x)
        y2 = calc(expr, lower_x + delta)

        # use the initial coordinates to get the coordinates for the calculator
        x1_screen, y1_screen = calc_to_screen_coord(lower_x, y1, x_origin, y_origin, ratio)
        x2_screen, y2_screen = calc_to_screen_coord(lower_x + delta, y2, x_origin, y_origin, ratio)

        # draw the line between the coordinates
        pointer.color(colour)
        draw_line(pointer, x1_screen, y1_screen, x2_screen, y2_screen)

        # increase delta so that the while loop does not become infinite
        lower_x += delta


# Code provided by instructor below

def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """
    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1


main()
turtle.exitonclick()
