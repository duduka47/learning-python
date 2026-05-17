import turtle
from states import States
from game import Game

screen = turtle.Screen()

screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# answer_state = screen.textinput(title='Guess the state', prompt="What's another state's name?")

states_c = States()
states_quantity = len(states_c.states)
game = Game(states_quantity=states_quantity)
timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")

while len(game.correct_gussed_states) < states_quantity:
   guess = game.guess(screen=screen)

   if guess:
      if states_c.check_state(state=guess):
         game.correct_answer(state=guess)
         states_c.write_state_in_screen(turtle=timmy, state=guess)


turtle.mainloop()