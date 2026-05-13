from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
# User input asking for it's bet
bet = screen.textinput(title="Make your bet", prompt='Who do you think will win the race? Enter a color from the rainbow: ')

# List of competitors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

race_on = False

turtles = []

finish_line = Turtle()
finish_line.penup()
finish_line.width(4)
finish_line.setx(230)
finish_line.sety(200)
finish_line.pendown()
finish_line.sety(-200)

# For each color in the list, it creates a new Turtle and calculates it's position based on its index and holds them in a list of turtles
for color in colors:
   # They're all siblings named the same 😂
   tim = Turtle(shape="turtle")
   tim.penup()
   tim.color(color)
   tim.setx(-230)
   tim.sety(-100 + (50 * colors.index(color)))
   turtles.append(tim)

if bet:
   race_on = True

while race_on:
   for turtle in turtles:
      # Randomizes a distance for each turtle then moves forwards
      random_distance = random.randint(0, 10)
      turtle.forward(random_distance)

      # gets X axis position
      if turtle.position()[0] > 230:
         winner = turtle.pencolor()
         print(f"{winner.capitalize()} turtle won the race!")
         if winner.lower() == bet.lower():
            print("You bet it right!")
         else:
            print("You lost")

         race_on = False


screen.exitonclick()