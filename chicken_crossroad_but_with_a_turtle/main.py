# This is the first solo project without classes.

from turtle import Screen
from game import Game
from player import Player
import time
from cars import Cars

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.tracer(0)
screen.colormode(255)

game = Game()
player = Player()
cars = Cars()
cars.generate_car()

# Controls

screen.listen()

screen.onkey(player.move, 'w')

while game.game_on:
   time.sleep(0.01)

   cars.move_cars()

   # checks if player reached the finish line

   if player.ycor() > 280:
      game.next_level()
      cars.increase_step()
      cars.reset_cars()
      cars.generate_cars()
      player.go_to_start()

   # checks if player collided with a car

   for car in cars.cars:
      if player.distance(car) < 25:
         game.game_over()


   screen.update()


screen.exitonclick()