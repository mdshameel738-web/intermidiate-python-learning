from pathlib import Path
import os
from tkinter import *
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"




#---------------pandas data----------------#
try:
    data_path = Path(__file__).parent / "data/words_to_learn.csv"
    data = pd.read_csv(data_path)
except FileNotFoundError:
    original_data_path = Path(__file__).parent / "data/french_words.csv"
    original_data = pd.read_csv(original_data_path)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    
current_card = {}

#-------------next card function------------#

def next_card():
    global current_card ,flip_timer
     # Cancel the previous flip_card timer
    window.after_cancel(flip_timer)  
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # Schedule the flip_card function to run after 3 seconds
    flip_timer=window.after(3000,flip_card)  
    
    
#-------------is known function------------#

def is_known():
    to_learn.remove(current_card)
    data_to_learn = pd.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()

#-------- filp card function---------#

def flip_card():
    """Flip the current card to show the English translation."""
    global current_card
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------- window ----------------- #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=800, height=600)
# Schedule the flip_card function to run after 3 seconds
flip_timer=window.after(3000,flip_card) 



#----------------imagepaths----------------#
card_front_path = Path(__file__).parent / "images/card_front.png"
card_back_path = Path(__file__).parent / "images/card_back.png"
right_mark_path = Path(__file__).parent / "images/right.png"
wrong_mark_path = Path(__file__).parent / "images/wrong.png"


#----------------- images ----------------- #
card_front_img = PhotoImage(file=card_front_path)
card_back_img = PhotoImage(file=card_back_path)
right_mark_img = PhotoImage(file=right_mark_path)
wrong_mark_img = PhotoImage(file=wrong_mark_path)

#----------------- canvas front ----------------- #
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0,columnspan=2) 

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))




#----------------- buttons ----------------- #
right_button = Button(image=right_mark_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_mark_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()



































window.mainloop()