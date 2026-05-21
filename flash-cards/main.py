from tkinter import * 
from pandas import *
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')

CANVAS_WIDTH=800
CANVAS_HEIGHT=526
card = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = card.create_image(CANVAS_WIDTH/2,CANVAS_HEIGHT/2,image=front_img)

flash_card_title = card.create_text(
    CANVAS_WIDTH / 2,
    150,
    text="Title",
    font=TITLE_FONT
)
flash_card_word = card.create_text(CANVAS_WIDTH /2, CANVAS_HEIGHT / 2, text="word", font=WORD_FONT)

card.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

# flashcards start

try:
   records = read_csv('./data/words_to_learn.csv')

   records_dict = records.to_dict(orient="records")
   if len(records_dict) <= 1:
      raise ValueError(f'File should contain at least 2 words to work')
except (FileNotFoundError, ValueError):
   records = read_csv('./data/french_words.csv')

   records_dict = records.to_dict(orient="records")

def flip_card(english_word):
   card.itemconfig(flash_card_title, text="English", fill="white")
   card.itemconfig(flash_card_word, text=english_word, fill="white")

   card.itemconfig(background_img,image=back_img)

card_after = None
current_card = None

def pick_random_word():
   global card_after, current_card

   current_card = random.choice(records_dict)
   french_word = current_card["French"]

   card.itemconfig(flash_card_title, text="French", fill="black")
   card.itemconfig(flash_card_word, text=french_word, fill="black")
   card.itemconfig(background_img, image=front_img)

   card_after = card.after(3000, lambda: flip_card(english_word=[current_card["English"]]))



def handle_check():
   records_dict.remove(current_card)
   words_to_learn = DataFrame(records_dict)
   words_to_learn.to_csv('./data/words_to_learn.csv', index=False)

   window.after_cancel(card_after)
   pick_random_word()

def handle_wrong():
   window.after_cancel(card_after)
   pick_random_word()

right_btn = Button(image=right_img, highlightthickness=0, command=handle_check)
right_btn.grid(row=1, column=1)
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=handle_wrong)
wrong_btn.grid(row=1, column=0)


pick_random_word()

window.mainloop()