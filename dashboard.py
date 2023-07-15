import tkinter as tk
from tkinter import ttk
import sqlite3

class DashboardWindow(tk.Toplevel):
    def __init__(self, name):
        super().__init__()
        self.title("Dashboard")
        self.geometry("800x600")
        self.resizable(False, False)
        self.configure(bg="#FFFFFF")

        # Create table title
        table_title = tk.Label(self, text="People using Connectify", font=("Helvetica", 16), bg="#FFFFFF")
        table_title.pack(pady=10)

        # Create table
        table = ttk.Treeview(self, columns=("Name", "Location", "Interest", "Email"), show="headings")
        table.heading("Name", text="Name")
        table.heading("Location", text="Location")
        table.heading("Interest", text="Interest")
        table.heading("Email", text="Email")
        table.pack(padx=10, pady=10)

        # Connect to database and retrieve data
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT name, location, interests, email FROM users")
        data = c.fetchall()
        conn.close()

        # Insert data into table
        for row in data:
            table.insert("", "end", values=row)
