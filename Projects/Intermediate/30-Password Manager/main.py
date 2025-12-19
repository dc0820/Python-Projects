from tkinter import *
from tkinter import messagebox
import json
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8,10)
    nr_numbers = randint(2,4)
    nr_symbols = randint(2,4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().capitalize()
    username = username_entry.get()
    password = password_entry.get()

    new_entry = {website:
                     {"email/username": username,
                      "password": password}
                 }

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/username: {username}"
                                                  f"\nPassword: {password}\nIs it okay to save?")

    if len(website) == 0 or len(password)==0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")

    if is_ok:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_entry, data_file, indent=4)

        else:
            data.update(new_entry)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

#---------------------------Find Password------------------------------ #
def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")

    else:
        if website in data:
            email = data[website]["email/username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message="No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(row=0, column=0, columnspan=3)

#Label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

#entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
username_entry.insert(0, "danielwcook5@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#generate password
generate_password = Button(text="Generate Password", command=generate)
generate_password.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=35, command = save)
add_button.grid(row=4, column=1, columnspan=2,sticky="ew")

search_button = Button(text="Search", command= find_password)
search_button.grid(row=1, column=2, sticky="ew")

window.mainloop()
