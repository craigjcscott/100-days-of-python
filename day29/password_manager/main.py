import tkinter as tk
from tkinter import messagebox  # must be explitly imported as it's a sub-module, not a class
import random
import string

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(length=16):
    allow_punctuation = punctuation_button_state.get()
    if allow_punctuation:
        eligible_chars = string.ascii_letters + string.digits + string.punctuation
    else:
        eligible_chars = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password = password + random.choice(eligible_chars)
    password_input.delete(0, tk.END)
    password_input.insert(0, password)
    r = tk.Tk()
    r.withdraw()
    r.clipboard_append(password)
    r.update()


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email_username = email_user_input.get()
    password = password_input.get()
    if website == "" or email_username == "" or password == "":
        print("Oops, you left a field blank!")
        messagebox.showinfo(title="Error", message="You left a field blank!")
    formatted_data = website + " | " + email_username + " | " + password
    confirm = messagebox.askokcancel(title=website, message=f"Please confirm the details below are correct: "
                                                           f"\nEmail: {email_username} "
                                                           f"\nPassword: {password} "
                                                           f"\nClick OK to save.")
    if confirm:
        with open("data.txt", "a") as data_file:
            data_file.write(formatted_data)
            data_file.write("\n")
        website_input.delete(0, tk.END)
        email_user_input.delete(0, tk.END)
        password_input.delete(0, tk.END)



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.minsize(width=400, height=400)
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = tk.Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

email_user_label = tk.Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

email_user_input = tk.Entry(width=35)
email_user_input.grid(row=2, column=1, columnspan=2)

password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = tk.Entry(width=22)
password_input.grid(row=3, column=1)

generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

# Test check button status in the console while app running
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(punctuation_button_state.get() == 1)

punctuation_button_state = tk.IntVar()
punctuation_button = tk.Checkbutton(text="Allow punctuation?", variable=punctuation_button_state)
punctuation_button.grid(row=4, column=2)

add_password_button = tk.Button(text="Add", width=20, command=save_password)
add_password_button.grid(row=4, column=1)

window.mainloop()
