from turtle import Turtle
import random
MIN_Y=-260
MAX_Y=260
MIN_X=300
MAX_X=500

class Cars(Turtle):
   def __init__(self):
      self.step = 1
      self.difficulty = 1
      self.cars: list[Turtle] = []

      self.generate_cars(quantity=10)

   def generate_car(self):
      car: Turtle = Turtle()
      car.color(random.randint(30, 255),random.randint(30, 255),random.randint(30, 255))
      car.penup()
      car.setheading(180)
      car.shape("square")
      car.shapesize(1, 2)
      car.goto(random.randint(MIN_X, MAX_X), random.randint(MIN_Y, MAX_Y))
      return car
   
   def generate_cars(self, quantity = 0):
      for i in range(0, quantity + self.difficulty * 2):
         car = self.generate_car()
         self.cars.append(car)

   def reset_cars(self):
      for car in self.cars:
         car.goto(random.randint(MIN_X, MAX_X), random.randint(MIN_Y, MAX_Y))

   def move_cars(self):
      for car in self.cars:
         if(car.xcor() < -300):
            car.goto(random.randint(MIN_X, MAX_X), random.randint(MIN_Y, MAX_Y))
         car.forward(self.step)

   def increase_step(self):
      self.step += 0.05