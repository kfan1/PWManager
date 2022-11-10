import random
from tkinter import *
import tkinter

LiST_OF_CHARACTERS = list('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?_@#$%&*=')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry3.delete(0, END)
    pw = ""
    for i in range(12):
        pw += random.choice(LiST_OF_CHARACTERS)
    entry3.insert(END, string=pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry1.get()
    username = entry2.get()
    password = entry3.get()
    with open('My Passwords.csv', mode='a') as my_file:
        my_file.write(f'\n{website},{username},{password}')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('PW Manager')
window.config(pady=20, padx=20)
canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(220, 120, image=lock_image)

text1 = Label(text='Website:', font=('Arial', 12, 'normal'))
text2 = Label(text='Email/Username:', font=('Arial', 12, 'normal'))
text3 = Label(text='Password:', font=('Arial', 12, 'normal'))
entry1 = Entry()
entry1.config(width=50)
entry2 = Entry()
entry2.config(width=50)
entry3 = Entry()
entry3.config(width=31)
button1 = Button(text='Generate Password', command=generate_password)
button2 = Button(text='Add', width=10, command=save)

canvas.grid(column=0, row=0, columnspan=3, sticky=tkinter.W + tkinter.E)
text1.grid(column=0, row=1, )
text2.grid(column=0, row=2, )
text3.grid(column=0, row=3, )
entry1.grid(column=1, row=1, columnspan=2, sticky=tkinter.W + tkinter.E)
entry2.grid(column=1, row=2, columnspan=2, sticky=tkinter.W + tkinter.E)
entry3.grid(column=1, row=3)
button1.grid(column=2, row=3)
button2.grid(column=1, row=4, columnspan=2, sticky=tkinter.W + tkinter.E)

window.mainloop()
