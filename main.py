from tkinter import *
from tkinter import messagebox

import json

from password_generator import generator

FONT = ("Courier", 12)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	password = generator()
	password_entry.delete(0, END)
	password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
	website = website_entry.get().title()
	username = username_entry.get()
	password = password_entry.get()

	new_data = {
		website: {
			"username": username,
			"password": password
		}
	}

	if len(username) == 0 or len(password) == 0 or len(website) == 0:
		messagebox.showinfo(title="Warning", message="Empty entries aren't allowed!")
	else:
		is_ok = messagebox.askokcancel(title=f"{website}", message=f"Are you sure you would like to save the\n"
																	f"Username: {username}\nPassword: {password}")
		if is_ok:
			file_name = "data.json"
			try:
				with open(file_name, "r") as file_data:
					current_data = json.load(file_data)
			except FileNotFoundError:
				to_create_file = messagebox.askokcancel(title="ERROR", message="No Data File Found.\n"
															  f"Do you want to create it?")
				if to_create_file:
					with open(file_name, "w") as file_data:
						json.dump(new_data, file_data, indent=4)
			else:
				current_data.update(new_data)

				with open("data.json", "w") as file_data:
					json.dump(current_data, file_data, indent=4)
			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)


# ---------------------------- SEARCH FOR USERNAME AND PASSWORD ------------------------------- #
def find_credentials():
	searched_website = website_entry.get().title()

	if len(searched_website) == 0:
		messagebox.showinfo(title="Warning", message="Empty entries aren't allowed!")
	else:
		file_name = "data.json"
		try:
			with open(file_name, "r") as file:
				credentials_data = json.load(file)
		except FileNotFoundError:
			messagebox.showinfo(title="ERROR", message=f"No Data File Found.")
		else:
			if searched_website in credentials_data:
				website_data = credentials_data[searched_website]
				username = website_data["username"]
				password = website_data["password"]
				messagebox.showinfo(title=f"{searched_website}", message=f"Username: {username}\n"
																					 f"Password: {password}")
			else:
				messagebox.showinfo(title="ERROR", message=f"You don't have any records for {searched_website}")
		finally:
			website_entry.delete(0, END)

			# try:
			# 	website_data = credentials_data[searched_website]
			# except KeyError:
			# 	messagebox.showinfo(title="ERROR", message=f"You don't have any records for {searched_website} website")
			# else:
			# 	username = website_data["username"]
			# 	password = website_data["password"]
			# 	messagebox.showinfo(title=f"{searched_website} credentials", message=f"Username: {username}\n"
			# 																	 f"Password: {password}")
			# finally:
			# 	website_entry.delete(0, END)

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
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(row=1, column=1)
username_entry = Entry(width=58)
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate Pass", font=FONT, width=14, command=generate_password)
generate_btn.grid(row=3, column=2)
add_btn = Button(text="Add", font=FONT, width=35, command=save_data)
add_btn.grid(row=4, column=1, columnspan=2)
search_btn = Button(text="Search", font=FONT, width=14, command=find_credentials)
search_btn.grid(row=1, column=2)


window.mainloop()
