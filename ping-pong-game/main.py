from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

# Game setup

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)

scoreboard = Scoreboard()
ball = Ball()

# Players

player_1 = Paddle(position="right")
player_2 = Paddle(position="left")

# Controls

screen.listen()

screen.onkeypress(player_2.move_down, 'k')
screen.onkeypress(player_2.move_up, 'i')

screen.onkeypress(player_1.move_up, 'w')
screen.onkeypress(player_1.move_down, 's')


def game_loop():
   # detect collision with top and bottom walls
   if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce_y()

   # detect collision with paddles
   if (
      ball.distance(player_1) < 50 and ball.xcor() > 320
   ) or (
      ball.distance(player_2) < 50 and ball.xcor() < -320
   ):
      ball.bounce_x()

   # detects if ball is out of bounds
   if ball.xcor() > 380:
      scoreboard.point(player=2)
      ball.increase_speed()
      ball.reset_ball()

   if ball.xcor() < -380:
      scoreboard.point(player=1)
      ball.increase_speed()
      ball.reset_ball()

   ball.move()

   screen.update()

   # chama o loop novamente
   screen.ontimer(game_loop, 16)  # ~60 FPS


game_loop()

screen.exitonclick()