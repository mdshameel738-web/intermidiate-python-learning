from tkinter import *


window =Tk()
window.title("GUI")
window.minsize(width=500,height=300)
window.config(padx=20,pady=40)

#label

my_label =Label(text="I am a label", font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

#Button

def button_click():
    inp=input.get()
    my_label.config(text=inp)



button = Button(text="Click me ", command= button_click)
button.grid(column=1,row=1)


button1 = Button(text="Click me ")
button1.grid(column=2,row=0)

#enter

input= Entry()
input.grid(column=3,row=2)




















window.mainloop()
