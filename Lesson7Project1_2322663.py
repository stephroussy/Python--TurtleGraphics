"""Name of program: Lesson7Project1_2322663.py
   Author of program: Stephanie Roussy
   Last date program was modified: 10/23/21
   Summary of the program's intent:Modify the
   Koch Snowflake project from Mindtap to draw
   a 2-Dimensional Sierpinski Carpet. """
import turtle
turtle.hideturtle()
turtle.fillcolor("white")
turtle.bgcolor("blue")



def drawFractalLine(x, y, distance, level):
    # exits method if level reaches 0
    if level == 0:
        return
    else:
    #moves turtle to a specific position
        turtle.goto(x - distance / 2, y + distance / 2)
        turtle.begin_fill()
        #creating squares
        for i in range(4):
            turtle.down()
            turtle.forward(distance)
            turtle.right(90)
            turtle.up()
        turtle.end_fill()

        # using 1/3rd of current length for new squares.
        drawFractalLine(x - distance, y + distance, distance / 3, level - 1)  # top left square
        drawFractalLine(x, y + distance, distance / 3, level - 1)  # top center square
        drawFractalLine(x + distance, y + distance, distance / 3, level - 1)  # top right square
        drawFractalLine(x - distance, y, distance / 3, level - 1)  # left square
        drawFractalLine(x + distance, y, distance / 3, level - 1)  # right square
        drawFractalLine(x - distance, y - distance, distance / 3, level - 1)  # bottom left square
        drawFractalLine(x, y - distance, distance / 3, level - 1)  # bottom center square
        drawFractalLine(x + distance, y - distance, distance / 3, level - 1)  # bottom right square

#providing coordinates, distance and level
def main(width, height, size):
    turtle.speed(0)
    drawFractalLine(0, 0, 200, 4)
main(200, 200, 150)
       





        



