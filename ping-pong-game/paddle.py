from turtle import Turtle
MAX_Y_CORD = 230 
STEP = 20

class Paddle(Turtle):
   def __init__(self, position = 'right'):
      super().__init__()
      self.color("white")
      self.shape("square")
      self.penup()
      self.speed('fastest')
      self.shapesize(stretch_wid=5, stretch_len=1)
      
      if position == "right":
         self.goto(350, 0)

      if position == "left":
         self.goto(-350,0)

   def move_up(self):
      if (self.ycor() > MAX_Y_CORD):
         return
      self.goto(self.xcor(), self.ycor() + STEP)

   def move_down(self):
      if (self.ycor() < -MAX_Y_CORD):
         return
      self.goto(self.xcor(), self.ycor() - STEP)