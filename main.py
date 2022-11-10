import json
import random
from tkinter import *
from tkinter import messagebox

LiST_OF_CHARACTERS = list('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!?_@#$%&*=')


def generate_password():
    entry3.delete(0, END)
    pw = ""
    for i in range(12):
        pw += random.choice(LiST_OF_CHARACTERS)
    entry3.insert(END, string=pw)


def search():
    try:
        with open('My Passwords.json', mode='r') as my_file:
            data = json.load(my_file)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry2.insert(END, data[entry1.get().capitalize()]['Email/Username'])
            entry3.insert(END, data[entry1.get().capitalize()]['Password'])

    except (KeyError, FileNotFoundError):
        entry1.delete(0, END)
        entry1.insert(END, 'PW not on file')


def save():
    website = entry1.get().capitalize()
    username = entry2.get()
    password = entry3.get()
    okay = messagebox.askokcancel(title=website, message=f'Email/Username: {username}\nPassword: {password}')

    if okay:
        my_data = {
            website: {
                'Email/Username': username,
                'Password': password
            }
        }
        try:
            with open('My Passwords.json', mode='r') as my_file:
                data = json.load(my_file)
                data.update(my_data)
            with open('My Passwords.json', mode='w') as my_file:
                json.dump(data, my_file, indent=4)

        except (json.decoder.JSONDecodeError, FileNotFoundError):
            with open('My Passwords.json', mode='w') as my_file:
                json.dump(my_data, my_file, indent=4)

        entry1.delete(0, END)
        entry3.delete(0, END)


window = Tk()
window.title('PW Manager')
window.config(pady=20, padx=20)
canvas = Canvas(height=200, width=200)
lock_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_image)

text1 = Label(text='Website:', font=('Arial', 12, 'normal'))
text2 = Label(text='Email/Username:', font=('Arial', 12, 'normal'))
text3 = Label(text='Password:', font=('Arial', 12, 'normal'))
entry1 = Entry()
entry1.config(width=31)
entry1.focus()
entry2 = Entry()
entry2.config(width=50)
entry2.insert(END, 'kevinlifan@yahoo.com')
entry3 = Entry()
entry3.config(width=31)
button1 = Button(text='Generate Password', command=generate_password)
button2 = Button(text='Add', width=42, command=save)
button3 = Button(text='Search', width=14, command=search)

canvas.grid(column=0, row=0, columnspan=3)
text1.grid(column=0, row=1)
text2.grid(column=0, row=2)
text3.grid(column=0, row=3)
entry1.grid(column=1, row=1, pady=2)
entry2.grid(column=1, row=2, columnspan=2, pady=2)
entry3.grid(column=1, row=3, pady=2)
button1.grid(column=2, row=3, pady=2)
button2.grid(column=1, row=4, columnspan=2, pady=2)
button3.grid(column=2, row=1)

window.mainloop()
