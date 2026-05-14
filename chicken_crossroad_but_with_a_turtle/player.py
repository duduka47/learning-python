STEP=5
STARTING_POSITION=(0,-280)

from turtle import Turtle
class Player(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("turtle")
      self.penup()
      self.goto(STARTING_POSITION)
      self.setheading(90)
      self.color("black")

   def move(self):
      self.forward(STEP)

   def go_to_start(self):
      self.goto(STARTING_POSITION)
