from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- VARIABLES ------------------------------- #

timeout = WORK_MIN * 60
cycle = 1
break_time = False
scheduled_id = None
countdown_text="25:00"

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
   global timeout, cycle, break_time, scheduled_id

   timeout = WORK_MIN * 60
   cycle = 1
   break_time = False

   update_countdown(timeout)

   window.after_cancel(scheduled_id)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def update_countdown(time_left_in_seconds):
   minutes = math.floor(time_left_in_seconds / 60)
   seconds = time_left_in_seconds % 60

   if minutes < 10:
      minutes = f"0{minutes}"

   if seconds < 10:
      seconds = f"0{seconds}"

   canvas.itemconfig(countdown, text=f"{minutes}:{seconds}")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
   global timeout, cycle, break_time, scheduled_id

   if timeout == 0 and not break_time:
      break_time = True
      cycle += 1

      if cycle <= 3:
         timeout = SHORT_BREAK_MIN * 60
      if cycle == 4:
         timeout = LONG_BREAK_MIN * 60
         cycle == 0
   elif timeout == 0 and break_time:
      break_time = False
      timeout = WORK_MIN * 60


   timeout -= 1

   update_countdown(timeout)
   
   scheduled_id = window.after(1000, start)
      
# ---------------------------- UI SETUP ------------------------------- #

# Screen

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# App Title

title = Label(text="Timer", bg=YELLOW, foreground=GREEN, font=(FONT_NAME, 48, "bold"))
title.grid(row=0, column=1)

# Tomato Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
countdown = canvas.create_text(100, 130, text=countdown_text, fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

# Buttons

start_btn = Button(text="Start", command=start, padx=5, pady=3, bg=PINK, fg='white', font=(FONT_NAME, 12, "bold"))
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=reset, padx=5, pady=3, bg=RED, fg='white', font=(FONT_NAME, 12, "bold"))
reset_btn.grid(row=2, column=2)



window.mainloop()