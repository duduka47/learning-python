from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 250
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:
   def __init__(self, quiz_brain: QuizBrain):
      self.quiz = quiz_brain
      self.window: Tk = Tk()
      self.window.title('Quizzler')
      self.window.config(padx=20, pady=20, bg=THEME_COLOR)
      
      # Scoreboard
      self.scoreboard = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white')
      self.scoreboard.grid(column=1, row=0)


      # Questions display
      self.canvas = Canvas(bg='white', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
      self.canvas.grid(column=0, row=1, columnspan=2, pady=20)
      self.question_text = self.canvas.create_text(CANVAS_WIDTH/2,CANVAS_HEIGHT/2,text='', font=QUESTION_FONT, width=280)
      self.get_next_question()

      # Buttons
      TRUE_IMG = PhotoImage(file='./images/true.png')
      FALSE_IMG = PhotoImage(file='./images/false.png')

      self.true_btn = Button(image=TRUE_IMG, bg=THEME_COLOR, highlightthickness=0, command=lambda: self.button_pressed(True))
      self.true_btn.grid(column=0, row=2)

      self.false_btn = Button(image=FALSE_IMG, bg=THEME_COLOR, highlightthickness=0, command=lambda: self.button_pressed(False))
      self.false_btn.grid(column=1, row=2)

      self.window.mainloop()

   def get_next_question(self):
      if self.quiz.still_has_questions():
         q_text = self.quiz.next_question()
         self.scoreboard.config(text=f'Score: {self.quiz.score}')
         self.canvas.itemconfig(self.question_text, text=q_text)
      else:
         self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
         self.true_btn.config(state='disabled')
         self.false_btn.config(state='disabled')

   def give_feedback(self, is_right):
      if is_right:
         self.canvas.config(bg='green')
      else:
         self.canvas.config(bg='red')
      self.window.after(1000, self.get_next_question)
      self.window.after(1000, lambda: self.canvas.config(bg='white'))


   def button_pressed(self, type: bool):
      if type:
         is_right = self.quiz.check_answer("True")
         self.give_feedback(is_right)
      else:
         is_right = self.quiz.check_answer("False")
         self.give_feedback(is_right)

      