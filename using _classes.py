from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class LoginWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        window_width = 400
        window_height = 400
        
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #pack the LoginFrame in the Login window
        LoginFrame(self).grid(row=0, column=0, padx=50, pady=150)
        FirstTimeLoginFrame(self).grid(row=0, column=0)

class FirstTimeLoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        #checking input
        def login_button_used():
            if self.create_password_input.get() == self.password_input.get():
                 messagebox.showinfo("Password created successfully!", "Password created successfully!")
            else:
                messagebox.showerror("Passwords do not match!", "Passwords do not match!")     
       
        #entry variables
        self.create_password_input = StringVar()
        self.password_input = StringVar()
       
        #creating widgets
        create_password_label = ttk.Label(self, text="Create a main password")
        repeat_password_label = ttk.Label(self, text="Repeat password")
        create_password_entry = ttk.Entry(self, textvariable=self.create_password_input)
        repeat_password_entry = ttk.Entry(self, textvariable=self.password_input)
        login_button = ttk.Button(self, text="LOGIN", command=login_button_used)
        
        
        #placing widgets on the window
        create_password_label.grid(row= 1, column=0, padx=10, pady=10)
        repeat_password_label.grid(row= 2, column=0, padx=10, pady=10)
        create_password_entry.grid(row= 1, column=1, padx=10, pady=10)
        repeat_password_entry.grid(row= 2, column=1, padx=10, pady=10)
        login_button.grid(row=3, column=1, padx=10, pady=10)
        
       
        
class LoginFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        #entry variables
        self.password_input = StringVar()
        
        #creating widgets
        password_label = ttk.Label(self, text="Enter your password:")
        password_entry = ttk.Entry(self, textvariable=self.password_input)
        login_button = ttk.Button(self,text="LOGIN")
        
        #placing widgets on the window
        password_label.grid(row=0, column=0, padx=10, pady=10)
        password_entry.grid(row=0, column=1, padx=10, pady=10)
        login_button.grid(row=2, column=1, padx=10, pady=10)

root = LoginWindow()
root.mainloop()
