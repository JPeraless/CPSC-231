# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# Name: Jose Perales Rivera
# Date: 12/11/2021

################################################################################
# Assignment 3
# Given constellation information in a .dat file, this program makes use of the
# turtle library to draw each of them in a cartesian plane and in a way that
# different constellations can be easily distinguished.
################################################################################


import sys
import os
import turtle

# STARTER CONSTANTS
BACKGROUND_COLOR = "black"
WIDTH = 600
HEIGHT = 600
# AXIS CONSTANTS
AXIS_COLOR = "blue"
# STAR CONSTANTS
STAR_COLOR = "white"
STAR_COLOR2 = "grey"
TICK_OFFSET = 6
LABEL_OFFSET_X = 24
LABEL_OFFSET_Y = 7
RATIO = 300


# checks the arguments in the command line
# returns a boolean if -names was activated, the file from which the user wants to input the stars and the list of constellations inputted by the user
def commandLineCheck():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments were entered")
    elif not os.path.isfile(sys.argv[0]):  # if the first argument entered is not a file the program won't run
        sys.exit("The file does not exist")
    elif (len(sys.argv) == 3) and ((sys.argv[1] != "-names") and (sys.argv[2] != "-names")):
        sys.exit("Neither input given was '-names'")
    elif (len(sys.argv) == 3) and ((sys.argv[1] == "-names") and (sys.argv[2] == "-names")):
        sys.exit("There cannot be more than one '-names' input")

    constellationsList = []
    names = False
    starsLocationFile = None

    if len(sys.argv) == 1:  # when there is 1 argument

        starsLocationInput = input("Enter a stars location file: ")  # prompt for a stars location file

        if os.path.isfile(starsLocationInput):
            starsLocationFile = starsLocationInput
        else:
            exists = False
            while not exists:  # primer error
                print("The stars location file does not exist")
                starsLocationInput = input("Enter a valid stars location file: ")

                if starsLocationInput == "":
                    sys.exit("No file was inputted")

                if os.path.isfile(starsLocationInput):
                    starsLocationFile = starsLocationInput
                    exists = True

        constellationFile = input("Enter a constellation file: ")  # prompt for constellation files

        while constellationFile != "":
            if os.path.isfile(constellationFile):
                constellationsList.append(constellationFile)
            else:
                exists = False
                while (not exists) or (constellationFile != ""):
                    print("File does not exist")
                    constellationFile = input("Enter a constellation file: ")

                    if os.path.isfile(constellationFile):
                        constellationsList.append(constellationFile)
                        exists = True

    elif len(sys.argv) == 2:  # when there are 2 arguments

        if sys.argv[1] == "-names":  # if the argument is -names
            names = True

            starsLocationInput = input("Enter a stars location file: ")

            if os.path.isfile(starsLocationInput):
                starsLocationFile = starsLocationInput
            else:
                exists = False
                while not exists:
                    print("The stars location file does not exist")
                    starsLocationInput = input("Enter a valid stars location file: ")

                    if starsLocationInput == "":
                        sys.exit("No file was inputted")

                    if os.path.isfile(starsLocationInput):
                        starsLocationFile = starsLocationInput
                        exists = True

        else:  # if the argument is a stars location file
            if os.path.isfile(sys.argv[1]):
                starsLocationFile = sys.argv[1]
            else:  # in case the entered stars location file does not exist
                sys.exit("The file entered does not exist")

        constellationFile = input("Enter a constellation file: ")  # prompt for constellation files

        while constellationFile != "":
            if os.path.isfile(constellationFile):
                constellationsList.append(constellationFile)
            else:
                exists = False
                while (not exists) or (constellationFile != ""):
                    print("File does not exist")
                    constellationFile = input("Enter a constellation file: ")

                    if os.path.isfile(constellationFile):
                        constellationsList.append(constellationFile)
                        exists = True

    elif len(sys.argv) == 3:  # when there are 3 arguments
        if sys.argv[1] == "-names":
            names = True

            if os.path.isfile(sys.argv[2]):
                starsLocationFile = sys.argv[2]
            else:
                sys.exit("The given stars location file does not exist")

        elif sys.argv[2] == "-names":
            names = True

            if os.path.isfile(sys.argv[1]):
                starsLocationFile = sys.argv[1]
            else:
                sys.exit("The given stars location file does not exist")

        constellationFile = input("Enter a constellation file: ")

        while constellationFile != "":
            if os.path.isfile(constellationFile):
                constellationsList.append(constellationFile)
            else:
                exists = False
                while (not exists) or (constellationFile != ""):
                    print("File does not exist")
                    constellationFile = input("Enter a constellation file")

                    if os.path.isfile(constellationFile):
                        constellationsList.append(constellationFile)
                        exists = True

    return names, starsLocationFile, constellationsList


# reads the file containing the stars information
def readStar(starsLocationFile):
    try:
        starsLocationHandle = open(starsLocationFile)
    except:
        sys.exit("The file could not be opened")

    starsList = []
    starsDict = {}  # every name of every star is a different key

    for line in starsLocationHandle:
        line = line.strip()
        line = line.split(",")

        x = line[0]
        y = line[1]
        mag = line[4]
        name = line[6]
        if name != "":
            name.split(";")
        else:
            name = None

        lineTuple = (float(x), float(y), float(mag), name)  # como esto se mete al dict, el tuple para uno de los nombres de una estrella tiene todos sus nombres guardados
        starsList.append(lineTuple)

        if name != None:
            for i in name:
                name.strip()
                starsDict[name] = lineTuple

    return starsList, starsDict


def drawStars(pointer, starsList, namesControl=False):
    for i in starsList:
        x, y, mag, name = i
        screen_x, screen_y = calc_to_screen_coord(x, y, WIDTH/2, HEIGHT/2, RATIO)

        if name == None:
            pointer.color(STAR_COLOR2)
        else:
            pointer.color(STAR_COLOR)

            if namesControl:  # único punto de error
                pointer.goto(screen_x, screen_y)
                pointer.write(name)

        pointer.up()
        pointer.goto(screen_x, screen_y)
        pointer.dot(10 / (mag + 2))
        pointer.up()


def readConstellation(constellationsList):
    constellationStars = []

    for i in constellationsList:
        try:
            constellationHandle = open(i)
        except:
            sys.exit("The file could not be opened")

        for line in constellationHandle:
            line = line.strip()
            line = line.split(",")
            for j in line:
                constellationStars.append(j)

    return constellationStars


def drawConstellation(constellationStars, starsDict):
    starsDraw = []
    for i in constellationStars:
        pass


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
    min_x = int((0 - x_origin) / ratio)

    # largest integer x value
    max_x = int((WIDTH - x_origin) / ratio)

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
    min_y = int((0 - y_origin) / ratio)

    # largest integer y value
    max_y = int((WIDTH - y_origin) / ratio)

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
    pointer.color(AXIS_COLOR)
    draw_line(pointer, screen_x, screen_y - TICK_OFFSET, screen_x, screen_y + TICK_OFFSET)


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
    pointer.goto(screen_x - LABEL_OFFSET_Y, screen_y - LABEL_OFFSET_X)
    pointer.down()
    pointer.write(label_text)


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw a y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    # uses the draw_line function to draw one tick
    draw_line(pointer, screen_x - TICK_OFFSET, screen_y, screen_x + TICK_OFFSET, screen_y)


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
    pointer.goto(screen_x - LABEL_OFFSET_X, screen_y - LABEL_OFFSET_Y)
    pointer.down()
    pointer.write(label_text)


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
    control_x = lower_x

    while control_x <= 1:
        x_coordinate, y_coordinate = calc_to_screen_coord(control_x, 0, x_origin, y_origin, ratio)
        draw_x_axis_tick(pointer, x_coordinate, y_coordinate)
        draw_x_axis_label(pointer, x_coordinate, y_coordinate, control_x)
        control_x += 0.25

    # get the coordinates to draw the line
    x1, y1 = calc_to_screen_coord(lower_x, 0, x_origin, y_origin, ratio)
    x2, y2 = calc_to_screen_coord(upper_x, 0, x_origin, y_origin, ratio)

    # change the pointer color to black and draw the line
    pointer.color("blue")
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
    control_y = lower_y

    while control_y <= 1:
        x_coordinate, y_coordinate = calc_to_screen_coord(0, control_y, x_origin, y_origin, ratio)
        draw_y_axis_tick(pointer, x_coordinate, y_coordinate)
        draw_y_axis_label(pointer, x_coordinate, y_coordinate, control_y)
        control_y += 0.25

    # get the coordinate to draw the line
    x1, y1 = calc_to_screen_coord(0, lower_y, x_origin, y_origin, ratio)
    x2, y2 = calc_to_screen_coord(0, upper_y, x_origin, y_origin, ratio)

    # change the pointer color to black and draw the line
    pointer.color("blue")
    draw_line(pointer, x1, y1, x2, y2)


def constellationColor(constellation_count):
    if constellation_count % 3 == 0:
        return "red"
    elif constellation_count % 3 == 1:
        return "green"
    else:
        return "yellow"


def setup():
    """
    Setup the turtle window and return drawing pointer
    :return: Turtle pointer for drawing
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.delay(delay=0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main constellation program
    :return: None
    """
    # Handle arguments
    pointer = setup()

    # Read star information from file (function)
    names, starsLocationFile, constellationList = commandLineCheck()
    starsList, starsDict = readStar(starsLocationFile)

    # Draw Axes (function)
    draw_x_axis(pointer, WIDTH/2, HEIGHT/2, RATIO)
    draw_y_axis(pointer, WIDTH/2, HEIGHT/2, RATIO)

    # Draw Stars (function)
    drawStars(pointer, starsList, names)

    # Loop getting filenames
    constellationStars = readConstellation(constellationList)
    drawConstellation(constellationStars, starsDict)

    while False:
        # Read constellation file (function)
        # Draw Constellation (function)
        # Draw bounding box (Bonus) (function)
        pass


main()

print("\nClick on window to exit!\n")
turtle.exitonclick()
