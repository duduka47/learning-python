from turtle import Screen
import pandas

class Game:
   def __init__(self, states_quantity):
      self.correct_gussed_states = []
      self.total_states = states_quantity
      self.score = 0


   def format_text(self, text):
      return text.title()
   
   def exit(self):
      csv = pandas.read_csv("50_states.csv")
      states_to_learn = csv["state"].to_list()

      for state in states_to_learn:
         if state in self.correct_gussed_states:
            states_to_learn.remove(state)

      data = {
         "state": states_to_learn
      }

      states_to_learn = pandas.DataFrame(data)
      states_to_learn.to_csv("states_to_learn.csv")
      
      exit()


   def guess(self, screen: Screen):
      """Checks if its not a already correct guess then returns the user answer already in lowercase for comparision"""
      answer = screen.textinput(title='Guess the state', prompt="What's another state's name?")
      answer = self.format_text(text=answer)

      if answer.lower() == 'exit':
         self.exit()
      elif answer in self.correct_gussed_states:
         return False
      else:
         return answer

   def correct_answer(self, state):
      self.correct_gussed_states.append(self.format_text(state))
      self.score += 1