from tkinter import *

login = Tk()
login.title("Login")
login.minsize(width=300, height=400)

#Labels
l_title = Label(text="Please login or register !")
l_title.grid(row = 0, column=1)

#Entry
e_login = Entry(width=30)
e_login.grid(row=2,column=1, columnspan=2)

e_register = Entry(width=30)
e_register.grid(row=2,column=2, columnspan=2)


#Button
b_login = Button(text="Login")
b_login.grid(row=1,column=0)
b_register = Button(text="Register")
b_register.grid(row=2,column=0)





login.mainloop()