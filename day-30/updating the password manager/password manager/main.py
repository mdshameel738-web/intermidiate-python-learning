import os 
from re import search
from tkinter import *
from tkinter import messagebox, TclError
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    if pyperclip is not None:
        pyperclip.copy(password)
    else:
        window.clipboard_clear()
        window.clipboard_append(password)

#---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
                website: {
                    "email": email,
                    "password": password,
                }
            }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you" \
        " haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading the old data
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



script_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(script_dir, "logo.png")

canvas=Canvas(width=200, height=200)
logo_img=PhotoImage(file=logo_path)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#website entry
website_label=Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry=Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

#search button
search_button=Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

#email/username entry
email_label=Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry=Entry(width=39)
email_entry.insert(0, "mdshameel@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2) 

#password entry
password_label=Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry=Entry(width=22)
password_entry.grid(column=1, row=3)

#generate button
generate_button=Button(text="Generate Password", width=14, command=generate_password)
generate_button.grid(column=2, row=3)   

#add button
add_button=Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)














window.mainloop()