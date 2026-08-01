import math
import os
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
 
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    text_label.config(text="Timer",fg=GREEN)
    marks_labels.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        text_label.config(text="Break",fg=RED)

    elif reps % 2 == 0:
        countdown(short_break_sec)
        text_label.config(text="Short Break",fg=PINK)
        
    else:
        text_label.config(text="Work",fg=GREEN)


    countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):


    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if count > 0:
        global timer
        timer=window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        marks_labels.config(text=marks)




# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomadro Timer")
window.minsize(width=500,height=500)
window.config(padx=100,pady=50, bg=YELLOW)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image_path = os.path.join(os.path.dirname(__file__), "tomato.png")
pomodoro_img=PhotoImage(file=image_path)
canvas.create_image(100,112, image=pomodoro_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



text_label=Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
text_label.grid(column=1,row=0)


start_button=Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

marks_labels=Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))
marks_labels.grid(column=1,row=3)







window.mainloop()