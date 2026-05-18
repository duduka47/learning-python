from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
ERASE_INPUT = (0, 'end')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
   password_list = []

   password_list += [choice(letters) for _ in range(randint(8, 10))]
   password_list += [choice(symbols) for _ in range(randint(2, 4))]
   password_list += [choice(numbers) for _ in range(randint(2, 4))]

   shuffle(password_list)

   password = "".join(password_list)

   password_input.delete(*ERASE_INPUT)
   password_input.insert(0, password)
   pyperclip.copy(password)   
   

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():


   with open("password.txt", mode='a') as file:
      website = website_input.get()
      email = email_username_input.get()
      password = password_input.get()

      if len(website) <= 3 or len(email) <= 3 or len(password) <= 6:
         messagebox.showwarning(title="Oops", message="Don't leave fields empty or too short :D")
         return

      ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail:{email} \nPassword: {password} \nIs it ok to save?')

      if ok:
         file.write(f'{website} | {email} | {password} \n')
         website_input.delete(*ERASE_INPUT)
         email_username_input.delete(*ERASE_INPUT)
         password_input.delete(*ERASE_INPUT)
         messagebox.showinfo(title='Success', message="Password saved successfully")
      else:
         messagebox.showinfo(title='Cancelled', message="Operation cancelled")
   



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")


logo = PhotoImage(file='logo.png')

canvas = Canvas(width=200, height=200)
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

# ===== Inputs ===== 

# Website
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# Email/Username
email_username_label = Label(text='Email/Username:')
email_username_label.grid(row=2, column=0)
email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1, columnspan=2)

# Password
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_input = Entry(width=21)
password_input.grid(row=3, column=1)
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)

# Add/Save
add_btn = Button(text="Add", command=save_password, width=36)
add_btn.grid(row=4,column=1, columnspan=2)

window.mainloop()