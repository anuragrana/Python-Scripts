#
# Author - https://www.pythoncircle.com
#

import turtle
import time

# create a screen
screen = turtle.getscreen()
# set background color of screen
screen.bgcolor("white")
# set tile of screen
screen.title("USA Flag - https://www.pythoncircle.com")
# "Yesterday is history, tomorrow is a mystery, 
# but today is a gift. That is why it is called the present.”
# — Oogway to Po, under the peach tree, Kung Fu Panda Movie
oogway = turtle.Turtle()
# set the cursor/turtle speed. Higher value, faster is the turtle
oogway.speed(100)
oogway.penup()
# decide the shape of cursor/turtle
oogway.shape("turtle")

# flag height to width ratio is 1:1.9
flag_height = 250
flag_width = 475

# starting points
# start from the first quardant, half of flag width and half of flag height
start_x = -237
start_y = 125

# For red and white stripes (total 13 stripes in flag), each strip width will be flag_height/13 = 19.2 approx
stripe_height = flag_height/13
stripe_width = flag_width

# length of one arm of star
star_size = 10


def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()

def draw_star(x,y,color,length) :
    oogway.goto(x,y)
    oogway.setheading(0)
    oogway.pendown()
    oogway.begin_fill()
    oogway.color(color)
    for turn in range(0,5) :
        oogway.forward(length)
        oogway.right(144)
        oogway.forward(length)
        oogway.right(144)
    oogway.end_fill()
    oogway.penup()


# this function is used to create 13 red and white stripes of flag
def draw_stripes():
    x = start_x
    y = start_y
    # we need to draw total 13 stripes, 7 red and 6 white
    # so we first create, 6 red and 6 white stripes alternatively    
    for stripe in range(0,6):
        for color in ["red", "white"]:
            draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
            # decrease value of y by stripe_height
            y = y - stripe_height            

    # create last red stripe
    draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
    y = y - stripe_height


# this function create navy color square
# height = 7/13 of flag_height
# width = 0.76 * flag_height
# check references section for these values
def draw_square():
    square_height = (7/13) * flag_height
    square_width = (0.76) * flag_height
    draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')


def draw_six_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 112
    # create 5 rows of stars
    for row in range(0,5) :
        x = -222
        # create 6 stars in each row
        for star in range (0,6) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines


def draw_five_stars_rows():
    gap_between_stars = 30
    gap_between_lines = stripe_height + 6
    y = 100
    # create 4 rows of stars
    for row in range(0,4) :
        x = -206
        # create 5 stars in each row
        for star in range (0,5) :
            draw_star(x, y, 'white', star_size)
            x = x + gap_between_stars
        y = y - gap_between_lines

# start after 5 seconds.
time.sleep(5)
# draw 13 stripes
draw_stripes()
# draw squares to hold stars
draw_square()
# draw 30 stars, 6 * 5
draw_six_stars_rows()
# draw 20 stars, 5 * 4. total 50 stars representing 50 states of USA
draw_five_stars_rows()
# hide the cursor/turtle
oogway.hideturtle()
# keep holding the screen until closed manually
screen.mainloop()

