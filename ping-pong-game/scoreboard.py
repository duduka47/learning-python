from turtle import Turtle
COLOR = 'white'
FONT = ('Arial', 20, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.player_1_score = 0
      self.player_2_score = 0
      self.hideturtle()
      self.penup()
      self.goto(0, 240)
      self.color("white")
      self.update_score()
      

   def update_score(self):
      self.clear()
      self.write(f"{self.player_1_score} — {self.player_2_score}", font=FONT, align=ALIGNMENT)

   def point(self, player):
      if player == 1:
         self.player_1_score += 1
      if player == 2:
         self.player_2_score += 1

      self.update_score()