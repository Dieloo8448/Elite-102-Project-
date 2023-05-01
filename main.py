import tkinter as tk
import mysql.connector


# Connect to the database
bank = mysql.connector.connect(
    first_name="first name",
    last_name="last name",
    dob="date of birth",
    phone="phone number",
    address="address",
    username="username",
    password="password",
    balance="balance",
)
c = bank.cursor()

def create_user():
    # Get the values from the input fields
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    dob = entry_dob.get()
    phone = entry_phone.get()
    address = entry_address.get()
    username = entry_username.get()
    password = entry_password.get()
    balance = entry_balance.get()
    
    # Insert the values into the database
    c.execute("INSERT INTO users (first_name, last_name, dob, phone, address, username, password,balance) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (first_name, last_name, dob, phone, address, username, password,balance))
    bank.commit()

    # Clear the input fields
    entry_first_name.delete(0, tk.END)
    entry_last_name.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
    entry_balance.delete(0,tk.END)

# Create the UI
root = tk.Tk()
root['background']='#FFFFFF'
root.title("Create User")

# Frames
frame_personal = tk.LabelFrame(root, text="Personal Information", padx=12, pady=12,fg='black', bg='white')
frame_personal.grid(row=0, column=0, padx=12, pady=12)
frame_login = tk.LabelFrame(root, text="Login Information", padx=12, pady=12)
frame_login.grid(row=0, column=1, padx=12, pady=12)

# First Name
label_first_name = tk.Label(frame_personal, text="First Name",bg='white')
label_first_name.grid(row=0, column=0, sticky=tk.W)
entry_first_name = tk.Entry(frame_personal)
entry_first_name.grid(row=0, column=1)

# Last Name
label_last_name = tk.Label(frame_personal, text="Last Name",bg='white')
label_last_name.grid(row=1, column=0, sticky=tk.W)
entry_last_name = tk.Entry(frame_personal)
entry_last_name.grid(row=1, column=1)

# Date of Birth
label_dob = tk.Label(frame_personal, text="Date of Birth (YYYY-MM-DD)",bg='white')
label_dob.grid(row=2, column=0, sticky=tk.W)
entry_dob = tk.Entry(frame_personal)
entry_dob.grid(row=2, column=1)

# Phone Number
label_phone = tk.Label(frame_personal, text="Phone Number",bg='white')
label_phone.grid(row=3, column=0, sticky=tk.W)
entry_phone = tk.Entry(frame_personal)
entry_phone.grid(row=3, column=1)

# Address
label_address = tk.Label(frame_personal, text="Address",bg='white')
label_address.grid(row=4, column=0, sticky=tk.W)
entry_address = tk.Entry(frame_personal)
entry_address.grid(row=4, column=1)

# Username
label_username = tk.Label(frame_personal, text="Username",bg='white')
label_username.grid(row=5, column=0, sticky=tk.W)
entry_username = tk.Entry(frame_personal)
entry_username.grid(row=5, column=1)

# Password
label_password = tk.Label(frame_personal, text="Password",bg='white')
label_password.grid(row=6, column=0, sticky=tk.W)
entry_password = tk.Entry(frame_personal)
entry_password.grid(row=6, column=1)

# Balance
label_balance = tk.Label(frame_personal, text="Balance",bg='white')
label_balance.grid(row=7, column=0, sticky=tk.W)
entry_balance = tk.Entry(frame_personal)
entry_balance.grid(row=7, column=1)

# Create User button
button_create = tk.Button(root, text="Create User", command=create_user,fg='black', bg='lightgreen')
button_create.grid(row=7, column=0)

def close_account():
    username = input("Enter the account number to close: ")

    # Delete the account and associated records from the database
    c.execute("DELETE FROM users WHERE username = %s", (username,))
    c.execute("DELETE FROM accounts WHERE username = %s", (username,))
    c.execute("DELETE FROM transactions WHERE username = %s", (username,))
    c.commit()

    print("Account " + username + " has been closed")


def login():
    username = input("Enter your account number: ")
    password = input("Enter your PIN: ")

    # Validate the user's credentials
    c.execute("SELECT * FROM users WHERE account_number = %s AND pin = %s", (username, password))
    user = c.fetchone()

    if user is None:
        print("Invalid account number or PIN")
        return False
    else:
        print("Welcome, " + user[1])
        return user[0]

def check_account_balance(id: int) -> int:
    username = input("Enter your username: ")
    password = input("Enter your Password: ")
    sql = "SELECT balance FROM accounts WHERE account_number = %s AND pin = %s"
    val = (username, password)
    c.execute(sql, val)
    result = c.fetchone()
    
    if result:
      balance = result[0]
      print("Your account balance is:", balance)
    else:
      print("Invalid username or password.")
      
      bank.close()
    
    if result:
      balance = result[0]
      print("Your account balance is:", balance)
    else:
      print("Invalid username or password.")
