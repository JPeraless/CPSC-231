# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# OqdOu2Y6ZaT0zZ4f4myL
# DO NOT EDIT THE ABOVE LINES

# Class:    CPSC 231
# Name:     Jose Perales Rivera
# Tutorial: T01
# Date:     30/09/2021

################################################################################
# Assignment 1
# This code calculates the intersections between a circle and a line
# in a 800 x 600 grid and draws small green circles around the intersections.
# The dimensions of the circle and the line are given by the user.
################################################################################

import turtle

# constants
WIDTH = 800
HEIGHT = 600

# set objects
pointer = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()
screen.delay(delay=0)

# setup x and y axis
pointer.up()
pointer.goto(0, HEIGHT/2)
pointer.down()
pointer.forward(WIDTH)
pointer.up()
pointer.goto(WIDTH/2, 0)
pointer.left(90)
pointer.down()
pointer.forward(HEIGHT)
pointer.up()

# get input
circle_x = float(input("Enter circle x coordinate: "))
circle_y = float(input("Enter circle y coordinate: "))
radius = float(input("Enter radius of circle: "))
x1 = float(input("Enter line start x coordinate: "))
y1 = float(input("Enter line start y coordinate: "))
x2 = float(input("Enter line end x coordinate: "))
y2 = float(input("Enter line end y coordinate: "))

# draw circle
pointer.goto(circle_x + radius, circle_y)
pointer.down()
pointer.color("red")
pointer.circle(radius)
pointer.up()

# draw line
pointer.goto(x1, y1)
pointer.down()
pointer.color("blue")
pointer.goto(x2, y2)
pointer.up()

# all the math

# base equations to determine intersections
a = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
b = 2 * (((x1 - circle_x) * (x2 - x1)) + ((y1 - circle_y) * (y2 - y1)))
c = ((x1 - circle_x) ** 2) + ((y1 - circle_y) ** 2) - (radius ** 2)

# for a line
if a != 0:
    # calculating alpha
    alpha_1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    alpha_2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    print(alpha_1)
    print(alpha_2)

    # get the discriminant
    discriminant = (b ** 2) - (4 * a * c)

    # calculate the coordinates of the intersections
    intersection_x1 = ((1 - alpha_1) * x1) + (alpha_1 * x2)
    intersection_y1 = ((1 - alpha_1) * y1) + (alpha_1 * y2)
    intersection_x2 = ((1 - alpha_2) * x1) + (alpha_2 * x2)
    intersection_y2 = ((1 - alpha_2) * y1) + (alpha_2 * y2)

    # draw circles of intersections
    if discriminant > 0 and (0 <= alpha_1 <= 1 or 0 <= alpha_2 <= 1):
        if 0 <= alpha_1 <= 1:
            # draw the first intersection if it has
            pointer.goto(intersection_x1 + 5, intersection_y1)
            pointer.down()
            pointer.color("green")
            pointer.circle(5)
            pointer.up()
        if 0 <= alpha_2 <= 1:
            # draw the second intersection if it has
            pointer.goto(intersection_x2 + 5, intersection_y2)
            pointer.down()
            pointer.color("green")
            pointer.circle(5)
            pointer.up()
    elif discriminant == 0:
        # when there is a tangent
        pointer.goto(intersection_x1 + 5, intersection_y1)
        pointer.down()
        pointer.color("green")
        pointer.circle(5)
        pointer.up()
    else:
        # when there are no intersects
        pointer.goto(WIDTH/2, HEIGHT/2)
        pointer.color("green")
        pointer.write("No intersect!", False, align="center")

# (x1, y1) == (x2, y2)
else:
    if c != 0:
        # the point is not an intersection
        pointer.goto(WIDTH/2, HEIGHT/2)
        pointer.color("green")
        pointer.write("No intersect!", False, align="center")
    else:
        # the point is an intersection
        pointer.goto(x1 + 5, y1)
        pointer.down()
        pointer.color("green")
        pointer.circle(5)

# exit program
screen.exitonclick()
