from tkinter import *
import secrets
import pyperclip

#Global variables
username = ""
password = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_text():
   e_password.delete(0, END)
   e_website.delete(0,END)
   

# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Password Manager")
root.config(padx=20,pady=20)

#Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

#Labels
l_website = Label(text="Please login or register", font=("arial",20,"bold"))
l_website.grid(column=0, row=1,columnspan=2)

l_email_username = Label(text="Email/Username:")
l_email_username.grid(column=0, row=2)

l_password = Label(text="Password:")
l_password.grid(column=0, row=3)

#Entry
e_email_username = Entry(width=35)
e_email_username.grid(column=1, row=2, columnspan=2)

e_password = Entry(width=35)
e_password.grid(column=1, row=3, columnspan=2)

#Functions
def add_button_used():
    global username
    global password
    username = e_email_username.get()
    password = e_password.get()
    
#Buttons
b_generate_password = Button(text="Login", width=30)
b_generate_password.grid(column=1, row=4, columnspan=2, pady=10)

b_register = Button(text="Register", width=30)
b_register.grid(column=1, row=5, columnspan=2)


root.mainloop()