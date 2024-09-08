from tkinter import *
from password_generator import password_generator
FONT = ("Courier", 11)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	password = password_generator()
	password_entry.delete(0, END)
	password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
	username = username_entry.get()
	website = website_entry.get()
	password = password_entry.get()
	try:
		with open("../data.txt", mode="a") as file:
			file.write(f"{username} | {website} | {password}\n")
	except FileNotFoundError as e:
		print(e)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# Labels
website_name = Label(text="Website:", font=FONT)
website_name.grid(row=1, column=0)
username_label = Label(text="Username/Email:", font=FONT)
username_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry = Entry(width=55)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate Pass", font=FONT, width=14, command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", font=FONT, width=37, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
