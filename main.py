from tkinter import *
import secrets

username = ""
password = ""
website  = ""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    list1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","!","§","$","%","&","/","(",")","=","?","'","#"]
    password = ''.join(secrets.choice(list1) for i in range(30))
    e_password.insert(0, password)
    
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_text():
   e_password.delete(0, END)
   e_website.delete(0,END)
   
def save_data():
    add_button_used()
    f = open("database.txt","a")
    f.write(website + ";" + username + ";" + password + ";"+"\n")
    f.close()
    clear_text()
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

#Canvas
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
l_website = Label(text="Website:")
l_website.grid(column=0, row=1)

l_email_username = Label(text="Email/Username:")
l_email_username.grid(column=0, row=2)

l_password = Label(text="Password:")
l_password.grid(column=0, row=3)

#Entry
e_website = Entry(width=35)
e_website.grid(column=1, row=1, columnspan=2)

e_email_username = Entry(width=35)
e_email_username.grid(column=1, row=2, columnspan=2)
e_email_username.insert(0,"claudiughise@gmail.com")

e_password = Entry(width=35)
e_password.grid(column=1, row=3, columnspan=2)

#Functions
def add_button_used():
    global username
    global password
    global website
    website = e_website.get()
    username = e_email_username.get()
    password = e_password.get()
    
#Buttons
b_generate_password = Button(text="Generate Password", width=30, command=generate_password)
b_generate_password.grid(column=1, row=4, columnspan=2, pady=10)

b_add = Button(text="Add", width=30, command=save_data)
b_add.grid(column=1, row=5, columnspan=2)


window.mainloop()