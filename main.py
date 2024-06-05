from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Lists of possible characters for the password
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    # Generate random characters for the password
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    # Combine all the characters and shuffle them
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Create the final password
    password = "".join(password_list)

    # Clear the password entry field and insert the new password
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Copy the password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Get the entered details
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if any field is empty
    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    # Ask for confirmation to save the details
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                          f"\nPassword: {password} \nIs it ok to save?")
    if is_ok:
        # Save the details to a file
        with open("data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

            # Clear the website and password entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create a canvas to hold the logo image
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()  # Focus on the website entry field when the app starts

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")  # Pre-fill with a default email

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Run the application
window.mainloop()
