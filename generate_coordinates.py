import turtle
import pandas
screen = turtle.Screen()
screen.title("Turkish Provinces Game")
image = "named.gif"
screen.addshape(image)
turtle.shape(image)


def coordinates_generator(x, y):
    print(x, y)


turtle.onclick(coordinates_generator)
turtle.mainloop()
