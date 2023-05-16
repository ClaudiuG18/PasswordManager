from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
l_website.grid(column=0, row=1, sticky="w" )

l_email_username = Label(text="Email/Username:")
l_email_username.grid(column=0, row=2)

l_password = Label(text="Password:")
l_password.grid(column=0, row=3, sticky="w")

#Entry
e_website = Entry(width=35)
e_website.grid(column=1, row=1, columnspan=2)

e_email_username = Entry(width=35)
e_email_username.grid(column=1, row=2, columnspan=2)

e_password = Entry(width=21)
e_password.grid(column=1, row=3, columnspan=1,sticky="w")




window.mainloop()