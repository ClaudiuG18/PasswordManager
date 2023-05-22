from tkinter import *

class LoginWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        window_width = 350
        window_height = 350
        
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        
        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')



class LoginFrame(Tk):
    def __init__(self, container):
        super().__init__(container)#init for Tkinter
        
        
        
root = LoginWindow()
root.mainloop()
