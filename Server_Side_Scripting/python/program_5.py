import tkinter as tk
from tkinter import messagebox

def authenticate(username, password):
    valid_username = 'client'
    valid_password = 'server'

    return username == valid_username and password == valid_password

def on_login_button_click():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if authenticate(entered_username, entered_password):
        messagebox.showinfo("Login Successful", "Authentication successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

root = tk.Tk()
root.title("Login Screen")

username_label = tk.Label(root, text="Username:")
username_label.pack(pady=10)

username_entry = tk.Entry(root)
username_entry.pack(pady=10)

password_label = tk.Label(root, text="Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

login_button = tk.Button(root, text="Login", command=on_login_button_click)
login_button.pack(pady=10)

root.mainloop()
