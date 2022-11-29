import turtle

import pandas as pd

screen= turtle.Screen()
screen.title("Turkish Provinces Game ")
image="unnamed.gif"
screen.addshape(image)
turtle.shape(image)

provinces_data = pd.read_csv("turkish_provinces_by_plates.csv")
provinces_data = provinces_data.rename(columns = {'x ':'x'})
all_provinces = provinces_data.provinces.to_list()

guessed_provinces=[]
provinces_left=[]

while len(guessed_provinces) < 81:
    answer = screen.textinput(title=f"{len(guessed_provinces)}/Guess the names of the Turkey's 81 provinces !", prompt="What's the province's name?").title()
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
        t.write(answer, font=('Arial',10,'normal'))


pen=turtle.Turtle()
screen.clear()
pen.goto(0, 0)
end_text = ""
score = len(guessed_provinces)

if score == 81:
	end_text = 'You Guessed Them All Correctly'
elif score >= 60:
	end_text = f"Good Work: {score}/81"
elif score >= 30:
	end_text = f"Average Performance: {score}/81"
else:
	end_text = f"Poor Performance: {score}/81"

pen.write(f"{end_text}", align='center', font=("Arial", 22, 'normal'))

turtle.mainloop()