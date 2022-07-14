from tkinter import *
from tkinter import messagebox
import random
import pyperclip
"""
Pyperclip is a cross-platform Python module for copy and paste clipboard functions.
So what we want our program to do that when we generate the password then we want to automatically copied to the
clipboard and then we can paste it anywhere.
"""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    final_pwd = ""
    for x in range(1, nr_letters + 1):
        num = random.randint(0, len(letters) - 1)
        final_pwd += letters[num]
    for y in range(1, nr_symbols + 1):
        sy = random.randint(0, len(symbols) - 1)
        final_pwd += symbols[sy]
    for z in range(1, nr_numbers + 1):
        zz = random.randint(0, len(numbers) - 1)
        final_pwd += numbers[zz]
    list_pwd = list(final_pwd)
    random.shuffle(list_pwd)
    random_pwd = ''.join(list_pwd)
    password_entry.insert(0, string=random_pwd)
    pyperclip.copy(random_pwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#We want our file to be open in append mode as we will be writing everytime we don't want our previous file content to
#be deleted. If the file(data.txt) is not created manually then it will automatically create our file when we use append
#("a") or write("w") mode


def save():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    """
    If the user left any of the entry then we should pop-up a message and if all the fields are properly filled then we
    will again ask the user whether the details they entered are correct or not and if they opt for Ok then it would
    return True in is_ok variable and if opt for Cancel then the variable is_ok will store False.
    So if the user will opt for Ok then we will be adding all the content to the file otherwise the user can change or 
    modify the fields.
    """
    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \n"
                                                              f"Password: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                #Here delete() is used to delete the entry
                #delete between two indices, 0-based
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
#focus() will enable the cursor on website_entry box when we open the window
website_entry.focus()
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
"""
We know that we use a single email in every website to signup, so it will be a very good idea that if we launch our
email_entry box with by-default email.
Now we will be giving the by-default email and if user wants they can change.This is somehow behaves like a dummy email
Here 0 specify the index position starting it means the text going to be inserted in the first position whereas END
is a constant which defines the end point. Since in our case it doesn't matter we can place anywhere as we are starting
with empty box.In other words the index value just put the cursor where we want to write the string.
"""
email_entry.insert(0, string="mohammadtauseef284@gmail.com")
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(row=3, column=2)
"""
The aim of the project is that when th user hit the 'Add' button it will should save the 
"""
add_button = Button(text="Add", width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
