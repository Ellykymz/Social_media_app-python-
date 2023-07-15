import tkinter as tk
from login_window import LoginWindow
from signup_window import SignupWindow

def open_login_window():
    login_window = LoginWindow()

def open_signup_window():
    signup_window = SignupWindow()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Interest Matcher App")

    # Set the initial size of the window to 500x500 pixels
    root.geometry("500x500")

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (500 // 2)
    y = (screen_height // 2) - (500 // 2)
    root.geometry("+{}+{}".format(x, y))

    # Label in the root window  
    label = tk.Label(root, text="Welcome to Connectify, the app that helps you find people who share your interests! Whether you're looking for a hiking buddy, a book club member, or a travel companion, we've got you covered.", font=("Arial", 12), wraplength=450)
    label.pack(pady=20, anchor="center")

    # Button to open login window
    button_login = tk.Button(root, text="Login", command=open_login_window)
    button_login.pack(pady=10, anchor="center")

    # Label and button to open sign up window
    label_signup = tk.Label(root, text="You don't have an account?")
    label_signup.pack(pady=5, anchor="center")
    button_signup = tk.Button(root, text="Sign up", command=open_signup_window)
    button_signup.pack(pady=10, anchor="center")

    root.mainloop()