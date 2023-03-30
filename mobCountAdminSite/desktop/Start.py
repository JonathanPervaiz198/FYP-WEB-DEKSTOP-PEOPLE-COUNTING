import time
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import Login_Register

splashWindow = Tk()
splashWindow.configure(background='#0FB5DA')
appWidth = 720
appHeight = 680
screenWidth = splashWindow.winfo_screenwidth()
screenHeight = splashWindow.winfo_screenheight()

xCoordinates = (screenWidth / 2) - (appWidth / 2)
yCoordinates = (screenHeight / 2) - (appHeight / 2)

splashWindow.overrideredirect(True)
splashWindow.geometry(f'{appWidth}x{appHeight}+{int(xCoordinates)}+{int(yCoordinates)}')
splashBackground = PhotoImage(file="Logo.png")
pictureLabel = Label(splashWindow, image=splashBackground, bg='#0FB5DA')
pictureLabel.place(x=0, y=0, relwidth=1, relheight=1)

progressBar = ttk.Progressbar(splashWindow, orient=HORIZONTAL, length=300, mode='determinate')
progressBar.place(x=170, y=450, relwidth=0.5, relheight=0.05)


def splash_screen():
    progressBar.start(20)
    for x in range(5):
        progressBar['value'] += 20
        splashWindow.update_idletasks()
        time.sleep(1)


class PreDashboard:
    def __init__(self):
        self.main = None

    def select_choice(self):
        splashWindow.destroy()
        self.main = Tk()
        self.main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
        #self.main.iconbitmap('Logo.ico')
        self.main.minsize(1000, 700)
        self.main.maxsize(1000, 700)
        self.main.geometry('1000x700')

        self.main.configure(background='#0FB5DA')

        logo = Image.open('Logo.PNG')
        resized_logo = logo.resize((310, 130))
        logo = ImageTk.PhotoImage(resized_logo)
        logo_label = Label(self.main, image=logo, background='#0FB5DA')
        logo_label.pack(pady=(10, 10))
        custom_font = ("Times", 14, 'bold')
        text_logo = Label(self.main, text='UAV-Based People Counting System', fg='black', bg='#0FB5DA')
        text_logo.config(font=('verdana', 24))
        text_logo.pack()

        login_button = Button(self.main, text='Login', font=custom_font, command=self.login_panel, bg='black', fg='white', width=30,
                              height=2)
        login_button.pack(pady=(80, 5))

        registration_button = Button(self.main, text='Sign Up', font=custom_font, command=self.registration_panel,
                                     bg='black', fg='white',
                                     width=30,
                                     height=2, )
        registration_button.pack(pady=(50, 5))

        exit_button = Button(self.main, text='Exit', font=custom_font, command=self.main.destroy, bg='black', fg='white',
                             width=30,
                             height=2)
        exit_button.pack(pady=(50, 5))

        self.main.mainloop()

    def login_panel(self):
        login = Login_Register.Login()
        self.main.destroy()
        login.login_screen()

    def registration_panel(self):
        registration = Login_Register.Registration()
        self.main.destroy()
        registration.registration_screen()


if __name__ == '__main__':
    splash_screen()
    pre_dashboard_screen = PreDashboard()
    splashWindow.after(3500, pre_dashboard_screen.select_choice())
