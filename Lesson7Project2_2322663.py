"""Name of program: Lesson7Project2_2322663.py
   Author of program: Stephanie Roussy
   Last date program was modified: 10/23/21
   Summary of the program's intent:This program
   will define and test a function
   createRestaurantLogo that expects a name and
   creates a logo for your restaurant with a
   geometric shape and text.."""

import turtle
# creating style elements for logo
turtle.bgcolor("purple")
turtle.hideturtle()
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("pink")
style = ("Courier", 120, "italic")
turtle.up()
turtle.goto(-500, 200)
turtle.down()

# creating logo
def drawcircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def createRestaurantLogo():
    for i in range(10):
        drawcircle(90)
        turtle.right(36)

createRestaurantLogo()
# restaurant name for logo
turtle.up()
turtle.goto(-290, 100)
turtle.down()
turtle.write("Stephanie's", font=style)

#printing menu for restaurant under logo
style = ("Courier", 30, "italic")
turtle.up()
turtle.goto(-370, -320)
turtle.down()
turtle.write("Burrito          24.56\nChicken Nuggets  21.56\nChicken Breasts  24.09\nCheese Burger    20.34\nChef's Salad     11.90\nPoutine          23.48\nEggrolls         18.90\nPizza            23.46\nDonuts           12.00\nSpaghetti        16.90\nTacos            24.85", font=style)
turtle.up()
turtle.goto(100, -290)
turtle.down()
turtle.write("French Fries      7.00\nSandwich         25.79\nCaesar salad     15.08\nSteak            30.55\nFish             21.55\nGarlic Bread      5.06\nNachos            8.00\nMeatloaf         22.00\nCheddar Balls    23.00\nKabobs           18.99", font=style)
        



