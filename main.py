import turtle

import pandas as pd

screen= turtle.Screen()
screen.title("Turkish Provinces Game ")
image="unnamed.gif"
screen.addshape(image)
turtle.shape(image)

provinces_data = pd.read_csv("turkish_provinces_by_plates.csv")
provinces_data = provinces_data.rename(columns = {'X ':'X'})

guessed_provinces=[]
provinces_left=[]

while len(guessed_provinces) < 81:
    all_provinces = provinces_data.provinces.to_list()

    answer = screen.textinput(
        title=f"{len(guessed_provinces)}/Guess the names of the Turkey's 81 provinces !", prompt="What's the province's name?").title()
    if answer == "Exit":
      provinces_left = list(set(all_provinces) - set(guessed_provinces))
      new_data = pd.DataFrame(provinces_left, columns=['Province to learn'])
      new_data.to_csv('Provinces not guessed-2.csv')
      break

    if answer in all_provinces:
        guessed_provinces.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data = provinces_data[provinces_data.provinces == answer]
        t.goto(int(data.x), int(data.y))
        t.write(answer)

