import turtle
from turtle import Turtle, Screen

import pandas
import pandas as pd

screen= turtle.Screen()
screen.title("Turkish Provinces Game ")
image="unnamed.gif"
screen.addshape(image)
turtle.shape(image)

provinces_data = pd.read_csv("turkish_provinces_by_plates.csv")
provinces=provinces_data.to_list()

guessed_provinces=[]


while len(guessed_provinces) < 81:
    answer = screen.textinput(
        title=f"{len(guessed_provinces)}/Guess the names of the Turkey's 81 provinces !", prompt="What's the province's name?").title()
    if answer == "Exit":
        provinces_left=[]
        for province in provinces:
            if province not in guessed_provinces:
                provinces_left.append(province)
        new_data =pandas.DataFrame(provinces_left)
        new_data.to_csv("provinces_remaining.csv")
        break
    if answer in provinces:
        guessed_provinces.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = provinces_data[provinces_data == answer]
        t.goto(int(data.x), int(data.y))
        t.write(answer)

