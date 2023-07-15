import tkinter as tk
import sqlite3

class SignupWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Sign up")

        # Name label and entry field
        self.label_name = tk.Label(self, text="Name:")
        self.label_name.grid(row=0, column=0, sticky="w")
        self.entry_name = tk.Entry(self)
        self.entry_name.grid(row=0, column=1)

        # Email label and entry field
        self.label_email = tk.Label(self, text="Email:")
        self.label_email.grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=1, column=1)

        # Password label and entry field
        self.label_password = tk.Label(self, text="Password:")
        self.label_password.grid(row=2, column=0, sticky="w")
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.grid(row=2, column=1)

        # Confirm password label and entry field
        self.label_confirm_password = tk.Label(self, text="Confirm password:")
        self.label_confirm_password.grid(row=3, column=0, sticky="w")
        self.entry_confirm_password = tk.Entry(self, show="*")
        self.entry_confirm_password.grid(row=3, column=1)

        # Age label and entry field
        self.label_age = tk.Label(self, text="Age:")
        self.label_age.grid(row=4, column=0, sticky="w")
        self.entry_age = tk.Entry(self)
        self.entry_age.grid(row=4, column=1)

        # Location label and entry field
        self.label_location = tk.Label(self, text="Location:")
        self.label_location.grid(row=5, column=0, sticky="w")
        self.entry_location = tk.Entry(self)
        self.entry_location.grid(row=5, column=1)

        # Interests label and entry field
        self.label_interests = tk.Label(self, text="Interests:")
        self.label_interests.grid(row=6, column=0, sticky="w")
        self.entry_interests = tk.Entry(self)
        self.entry_interests.grid(row=6, column=1)

        # Sign up button
        self.button_signup = tk.Button(self, text="Sign up", command=self.signup)
        self.button_signup.grid(row=7, column=0, columnspan=2)

    def signup(self):
        # Get the values from the form fields
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        age = self.entry_age.get()
        location = self.entry_location.get()
        interests = self.entry_interests.get()

        # Validate the form data
        if not name or not email or not password or not confirm_password:
            tk.messagebox.showerror("Error", "Please fill in all required fields.")
            return

        if password != confirm_password:
            tk.messagebox.showerror("Error", "Passwords do not match.")
            return

        # Save the user data to the database
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name, email, password, age, location, interests) VALUES (?, ?, ?, ?, ?, ?)", (name, email, password, age, location, interests))
        conn.commit()
        conn.close()

        # Find matches based on common interests
        matches = self.find_matches(interests)

        # Display the matches
        if matches:
            tk.messagebox.showinfo("Matches", "You have been matched with the following users: " + ", ".join(matches))
        else:
            tk.messagebox.showinfo("Matches", "There are no matches at this time.")

        # Inform the user of a successful signup
        tk.messagebox.showinfo("Success", "You have successfully signed up!")

        # Close the signup window
        self.destroy()

    def find_matches(self, interests):
        # Find other users with matching interests
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT name FROM users WHERE interests = ?", (interests,))
        matches = [row[0] for row in c.fetchall()]
        conn.close()

        # Remove the current user from the matches list
        current_user = self.entry_name.get()
        if current_user in matches:
            matches.remove(current_user)

        return matches