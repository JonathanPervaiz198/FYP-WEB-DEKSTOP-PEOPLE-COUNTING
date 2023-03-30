import tkinter
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
from desktop import Image_Stitching
from tkinter import messagebox
import os


def main_window():
    main = Tk()
    main.title('UAV-BASED PEOPLE COUNTING SYSTEM')
   # main.iconbitmap('Logo.ico')
    main.minsize(1000, 700)
    main.maxsize(1000, 700)
    main.geometry('1000x700')
    custom_font = ("Times", 14, 'bold')

    main.configure(background='#0FB5DA')

    logo = Image.open(os.path.join(os.path.dirname(__file__),'Logo.PNG'))
    resized_logo = logo.resize((310, 130))
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(main, image=logo, background='#0FB5DA')
    logo_label.pack(pady=(10, 10))

    text_logo = Label(main, text='UAV-Based People Counting System', fg='black', bg='#0FB5DA')
    text_logo.config(font=('verdana', 24))
    text_logo.pack()

    add_image_button = Button(main, text='Add Images',font=custom_font, command=add_image, bg='black', fg='white', width=30,
                              height=2)
    add_image_button.pack(pady=(45, 5))

    manage_drone_button = Button(main, text='Provide Coordinates to Drone', font=custom_font, command=manage_drone, bg='black', fg='white', width=30, height=2)
    manage_drone_button.pack(pady=(5, 5))

    collate_image_button = Button(main, text='Collate Images', font=custom_font, command=image_collation, bg='black', fg='white',
                                  width=30
                                  , height=2)
    collate_image_button.pack(pady=(5, 5))

    history_button = Button(main, text='Check History',font=custom_font, command=check_history, bg='black', fg='white', width=30,
                            height=2)
    history_button.pack(pady=(5, 5))

    exit_button = Button(main, text='Exit', command=main.destroy,font=custom_font, bg='black', fg='white', width=30, height=2)
    exit_button.pack(pady=(5, 5))

    main.mainloop()


def select_folder():
    folder_name = filedialog.askdirectory(initialdir="/", title="Select a Folder")
    if folder_name != "":
        stitching_object = Image_Stitching.ImageCollation(folder_name)
        stitching_object.stitching()
    else:
        return 0


def image_collation():
    collate = tkinter.Toplevel()
    collate.title('UAV-BASED PEOPLE COUNTING SYSTEM')
    #collate.iconbitmap('Logo.ico')
    collate.minsize(1000, 700)
    collate.maxsize(1000, 700)
    collate.geometry('1000x700')

    collate.configure(background='#0FB5DA')

    logo = Image.open(os.path.join(os.path.dirname(__file__),'Logo.PNG'))
    resized_logo = logo.resize((310, 130))
    logo = ImageTk.PhotoImage(resized_logo)
    logo_label = Label(collate, image=logo, background='#0FB5DA')
    logo_label.pack(pady=(10, 10))

    text_logo = Label(collate, text='UAV-Based People Counting System', fg='white', bg='#0FB5DA')
    text_logo.config(font=('verdana', 24))
    text_logo.pack()

    folder_label = Label(collate, text='Open a Folder', bg='#0FB5DA', fg='black')
    folder_label.config(font=('verdana', 16))
    folder_label.pack(pady=(20, 10))
    browse_button = Button(collate, text='Browse a Folder', command=select_folder, bg='white', fg='black', width=20,
                           height=2)
    browse_button.pack(pady=(5, 5))

    exit_button = Button(collate, text='Exit', command=collate.destroy, bg='white', fg='black', width=20, height=2)
    exit_button.pack(pady=(5, 5))

    collate.mainloop()


def add_image():
    messagebox.showinfo("Message", "Functionality Under Development.")


def manage_drone():
    messagebox.showinfo("Message", "Functionality Under Development.")


def check_history():
    messagebox.showinfo("Message", "Functionality Under Development.")


if __name__ == '__main__':
    mainloop()
