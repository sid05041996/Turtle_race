import turtle       ## this module is built into python and is used to allow you to build very basic 2-D graphics operations on the screen with this things.!!.
import time
import random

## size of the canvas:
WIDTH,HEIGHT = 500,500
COLORS=['red','blue','orange','yellow','black','green','brown','pink','cyan','violet']


def get_number_of_racers():
    racers=0
    while True:
        racers=input('Enter the number of the racers (2-10): ')
        if racers.isdigit():
            racers=int(racers)
        else:
            print('Invalid input!... Try again!...')
            continue        ## so that anything below the continue statement within the loop would not run once the else condition is or has been encountered.!!.
        if 2<=racers<=10:
            return racers
        else:
            print('Number not in the range of (2-10).,!!...,,.. Please try again.!!.')


def create_turtles(colors):
    ## Here., we will have our list of the turtles and we will show how and where will we place them on the screen and their starting positions.!!.
    turtles=[]
    spacingx=WIDTH //  (len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        ## trying to place these racers in their starting positions.!!.
        racer.left(90)          ## we do this because our racers are pointing towards the left., and in order to move forward or upwards., we need to turn them towards left by an angle of 90 degrees.!!.
        # now we need to use the following two functions in order to / so that we can move the turtles to their starting points without drawing anything on the screen from the center (0,0).!!.
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)   ## sets the position where we want to move our turtle into ., takes the values in terms of (x,y).!!.
        ## The y axis is set to be 20 pixels from the lowest proximity bar/set.!!.
        ## The x-axis starts from -WIDTH., because the first turtle would be placed at the (-)ve of the x axis compared to the origin (0,0).!!.
        racer.pendown()
        turtles.append(racer)
    return turtles
## here we are calculating the spacing the turtles equally in the x-axis.!!.        So if we simply find the number of turtles dividing the total width., then the first turtle would start from the 0th position in terms of x coordinates and would not be visible.!!.
## Now what we can do., is that we can divide the total width / total_no._of_turtles + 1 ., say 400=width; that means 400/5=80 and then we will place the first turtle at 80, second at 160, second at 240, fourth at 320 and the fourth one is also 80 units away from the right proximity.!!.
#This is exactly what we are doing within the spacingx 


## for racing our turtles in/on the screen.,!!.,::--
def race(colors):
    turtles = create_turtles(colors)  ## so the race() function will call the create_turtles() functions for us .!!.

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)  ## This will help the turtles to navigate or the speed of each turtle in a random fashion.!!.
            racer.forward(distance)

            x,y=racer.pos()  ## gives the position of each turtles.!!.
            if y>=HEIGHT//2 - 10:
                return colors[turtles.index(racer)] ## returns the colour of the winning turtle.!!.





def init_turtle():      ## using a function for the screen is because we need to show the screen pop up only after we have taken the input in the above function!!..
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Racing!!..')       ## changes the heading / the title of the generated screen of the game.!!.
    turtle.Screen().bgcolor("grey")



racers=get_number_of_racers()
print(racers)
init_turtle()
## In order to move a turtle around the screen.!!.;;::--
racer=turtle.Turtle() ## creating a new turtle object

'''
## using the object to do certain functions/functionalities.!!.::--
racer.speed(1)  ## increases or decreases the speed of the turtle while it moves/draws on the screen.!!.
#racer.penup() ## so what it does is., it will draw the line but with pen up., so we cannot see the visible line.!!!.
racer.shape('turtle')  ## decides the shape of the pointer / there are a ton of other shapes values present on the internet.!!.
racer.color('orange')  ## to change the colour of the turtle pointer.!!.
racer.forward(100) ## 100 pixels.!!.
racer.left(90) ## Here 90 is not the pixels but the the angle., which would be the same as that of the right as well., unlike the forward and backward functions/methods., where we usually add pixels.!!./
racer.forward(100)
racer.right(90)
racer.forward(100)
#time.sleep(5)       ## so that we can get some time to see the turtle .!!.
'''

random.shuffle(COLORS)      ## randomly shuffles all the colours.!!.
colors=COLORS[:racers]  ## so this will select only 'racers'(which contain the number of turtles entered by us.!!.) number of elements from the COLORS list.!!.

winner=race(colors)
print("The winner is the turtle with color :",winner)
time.sleep(5)