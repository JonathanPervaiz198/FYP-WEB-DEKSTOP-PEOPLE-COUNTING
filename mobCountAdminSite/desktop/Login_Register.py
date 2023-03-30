from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import bcrypt
import re
import Main

# Temporary Database
registered_users_emails = []
registered_users_passwords = []
registered_users_hashed_passwords = []
user_index = 0


def isValid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return 0
    else:
        return 1


class Registration:
    def __init__(self):
        self.confirm_password_entry = None
        self.main = None
        self.password_entry = None
        self.email_entry = None
        self.credentials = [0, 0]

    def registration_screen(self):
        self.main = Tk()
        self.main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
       # self.main.iconbitmap('Logo.ico')
        self.main.minsize(1000, 700)
        self.main.maxsize(1000, 700)
        self.main.geometry('1000x700')
        self.main.configure(background='#0FB5DA')

        logo = Image.open('Logo.PNG')
        resized_logo = logo.resize((310, 130))
        logo = ImageTk.PhotoImage(resized_logo)
        logo_label = Label(self.main, image=logo, background='#0FB5DA')
        logo_label.pack(pady=(10, 10))

        text_logo = Label(self.main, text='UAV-Based People Counting System', fg='black', bg='#0FB5DA')
        text_logo.config(font=('verdana', 24))
        text_logo.pack()

        email_label = Label(self.main, text='Enter your Email', fg='black', bg='#0FB5DA')
        email_label.config(font=('verdana', 20))
        email_label.pack(pady=(40, 10))

        self.email_entry = Entry(self.main)
        self.email_entry.config(width=30, font=20)
        self.email_entry.pack()

        password_label = Label(self.main, text='Enter your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 20))
        password_label.pack(pady=(20, 10))

        self.password_entry = Entry(self.main)
        self.password_entry.config(width=30, font=20, show="*")
        self.password_entry.pack()

        password_label = Label(self.main, text='Confirm your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 20))
        password_label.pack(pady=(20, 10))

        self.confirm_password_entry = Entry(self.main)
        self.confirm_password_entry.config(width=30, font=20, show="*")
        self.confirm_password_entry.pack()

        add_image_button = Button(self.main, text='Register', command=self.add_user, bg='black', fg='white',
                                  width=30,
                                  height=2)
        add_image_button.config(font=('verdana', 11), border=10)
        add_image_button.pack(pady=(40, 5))

        exit_button = Button(self.main, text='Exit', command=self.main.destroy, bg='black', fg='white',
                             width=30,
                             height=2)
        exit_button.pack(pady=(50, 5))

        self.main.mainloop()

    def add_user(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password == '' or email == '':
            messagebox.showinfo("Message", "Enter Credentials")

        elif isValid(email):
            messagebox.showinfo("Message", "Enter a Valid Email")

        elif password == confirm_password:
            # PASSWORD ENCRYPTION
            byte_password = password.encode('utf-8')
            salt = bcrypt.gensalt()
            pwd_hash = bcrypt.hashpw(byte_password, salt)
            password = password.encode('utf-8')
            registered_users_emails.insert(user_index, email)
            registered_users_passwords.insert(user_index, password)
            registered_users_hashed_passwords.insert(user_index, pwd_hash)
            messagebox.showinfo("Message", "Successfully Registered!")
            login_screen = Login()
            self.main.destroy()
            login_screen.login_screen()
        elif password != confirm_password:
            messagebox.showinfo("Message", "Password Does Not Match!")


class Login:
    def __init__(self):
        self.main = None
        self.password_entry = None
        self.email_entry = None
        self.credentials = [0, 0]

    def login_screen(self):
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

        text_logo = Label(self.main, text='UAV-Based People Counting System', fg='black', bg='#0FB5DA')
        text_logo.config(font=('verdana', 24))
        text_logo.pack()

        email_label = Label(self.main, text='Enter your Email', fg='black', bg='#0FB5DA')
        email_label.config(font=('verdana', 20))
        email_label.pack(pady=(60, 10))

        self.email_entry = Entry(self.main)
        self.email_entry.config(width=30, font=20)
        self.email_entry.pack()

        password_label = Label(self.main, text='Enter your Password', fg='black', bg='#0FB5DA')
        password_label.config(font=('verdana', 20))
        password_label.pack(pady=(30, 10))

        self.password_entry = Entry(self.main)
        self.password_entry.config(width=30, font=20, show="*")
        self.password_entry.pack()

        add_image_button = Button(self.main, text='Login', command=self.check_credentials, bg='black', fg='white',
                                  width=30,
                                  height=2)
        add_image_button.config(font=('verdana', 11), border=10)
        add_image_button.pack(pady=(60, 5))

        registration_button = Button(self.main, text='Sign Up', command=self.registration_panel, bg='black', fg='white',
                                     width=10,
                                     height=2)
        registration_button.config(font=('verdana', 7), border=5)
        registration_button.pack(pady=(10, 5))

        exit_button = Button(self.main, text='Exit', command=self.main.destroy, bg='black', fg='white',
                             width=30,
                             height=2)
        exit_button.pack(pady=(30, 5))

        self.main.mainloop()

    def check_credentials(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # PASSWORD ENCRYPTION
        byte_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        pwd_hash = bcrypt.hashpw(byte_password, salt)
        password = password.encode('utf-8')

        if password == '' or email == '':
            messagebox.showinfo("Message", "Enter Credentials")

        elif email == registered_users_emails.pop() and bcrypt.checkpw(registered_users_passwords[0],
                                                                       registered_users_hashed_passwords[0]):
            self.main.destroy()
            Main.main_window()

    def registration_panel(self):
        registration = Registration()
        self.main.destroy()
        registration.registration_screen()


if __name__ == '__main__':
    mainloop()
