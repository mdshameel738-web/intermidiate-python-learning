from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=40,pady=40)

#entry

input=Entry()

input.grid(row=0,column=1)


#text
miles_text=Label(text="Miles", font=("Arial",16))
miles_text.grid(row=0,column=2)

text1=Label(text="is equal to", font=("Arial",16))
text1.grid(row=1,column=0)

text2=Label(text=0, font=("Arial",16))
text2.grid(row=1,column=1)

text3=Label(text="Km", font=("Arial",16))
text3.grid(row=1,column=2)

#button
def button_click():
    miles=float(input.get())
    km = miles*1.60934
    text2.config(text=str(km))



button = Button(text="Calculate", command= button_click)
button.grid(column=1,row=2)



window.mainloop()