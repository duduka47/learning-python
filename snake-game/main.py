from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("🐍 - Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(snake.up,"w")
screen.onkeypress(snake.left,"a")
screen.onkeypress(snake.down,"s")
screen.onkeypress(snake.right,"d")

screen.onkeypress(snake.up,"Up")
screen.onkeypress(snake.left,"Right")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.right,"Left")


game_on = True

while game_on:
   screen.update()
   time.sleep(0.1)
   snake.move()

   # checking colission with food

   if snake.head.distance(food) <= 15:
      food.refresh()
      scoreboard.increase_score()
      snake.increase()

   # Detect collision with wall

   if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      scoreboard.game_over()
      game_on = False

   # Detect collision with tail
   
   for segment in snake.segments[1:]:
      if snake.head.distance(segment) < 10:
         scoreboard.game_over()
         game_on = False
      

screen.exitonclick()