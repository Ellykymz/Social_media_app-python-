import tkinter as tk
import tkinter
from dashboard import DashboardWindow
import sqlite3
from tkinter import messagebox
from signup_window import SignupWindow


class LoginWindow(tkinter.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Login")

        # Email label and entry field
        self.label_email = tk.Label(self, text="Email:")
        self.label_email.grid(row=0, column=0, sticky="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=0, column=1)

        # Password label and entry field
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=1, column=1)

        # Sign up button
        self.button_signup = tk.Button(self, text="Sign up", command=self.open_signup_window)
        self.button_signup.grid(row=2, column=0, columnspan=2)

        # Login button
        self.button_login = tk.Button(self, text="Login", command=self.login)
        self.button_login.grid(row=3, column=0, columnspan=2)

    def open_signup_window(self):
        SignupWindow()

    def login(self):
        email = self.entry_email.get()
        password = self.entry_password.get()

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
        result = cursor.fetchone()

        if result:
            self.destroy() # Close the login window
            DashboardWindow(result[1]) # Create instance of dashboard window
        else:
            messagebox.showerror("Error", "Invalid email or password")

        conn.close()
