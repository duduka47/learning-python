from turtle import Turtle
import random

STEP = 3
TOP_RIGHT=45
TOP_LEFT=135
BOTTOM_LEFT=225
BOTTOM_RIGHT=315

class Ball(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.shapesize(1, 1)
      self.color("yellow")
      self.penup()
      self.x_move = STEP
      self.y_move = STEP
   
   def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)
   
   def bounce_y(self):
      self.y_move *= -1
   
   def bounce_x(self):
      self.x_move *= -1

   def increase_speed(self):
      if self.x_move < 0:
         self.x_move -= 1
      else:
         self.x_move += 1

      if self.y_move < 0:
         self.y_move -= 1
      else:
         self.y_move += 1

   def reset_ball(self):
      self.home()
      