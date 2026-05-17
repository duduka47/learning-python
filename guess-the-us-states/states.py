import pandas
from turtle import Turtle
class States:
   def __init__(self):
      self.csv = pandas.read_csv("50_states.csv")
      states = self.csv["state"]
      self.states: pandas = states
      
   def check_state(self, state):
      return len(self.states[self.states == state.title()]) == 1
   
   def write_state_in_screen(self, turtle: Turtle, state):
      state_data = self.csv[self.csv["state"] == state.title()]
      turtle.goto(state_data["x"].item(), state_data["y"].item())
      turtle.write(state_data["state"].item())
      