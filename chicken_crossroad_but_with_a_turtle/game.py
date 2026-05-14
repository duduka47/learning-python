from turtle import Turtle
FONT=('Arial', 20, 'bold')
ALIGNMENT='center'

class Game(Turtle):
   def __init__(self):
      super().__init__()
      self.game_on = True
      self.level = 0
      self.color("black")
      self.penup()
      self.hideturtle()
      self.goto(-230, 260)
      self.next_level()

   def next_level(self):
      self.level += 1
      self.clear()
      self.write(f'Level {self.level}', align=ALIGNMENT, font=FONT)

   def game_over(self):
      self.goto(0,0)
      self.write(f'Game Over', align=ALIGNMENT, font=FONT)
      self.game_on = False