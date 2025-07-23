import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
import os

from utils.user_utils import add_user, delete_user, modify_user

# Main window
root = tk.Tk()
root.title("PermiControl - User Management")
root.geometry("500x400")

tab_control = ttk.Notebook(root)

# -------------------- Add User Tab --------------------
tab_add_user = ttk.Frame(tab_control)
tab_control.add(tab_add_user, text="Add User")

add_username_label = tk.Label(tab_add_user, text="Username:")
add_username_label.pack()
add_username_entry = tk.Entry(tab_add_user)
add_username_entry.pack()

add_password_label = tk.Label(tab_add_user, text="Password:")
add_password_label.pack()
add_password_entry = tk.Entry(tab_add_user, show="*")
add_password_entry.pack()

def on_add_user():
    username = add_username_entry.get().strip()
    password = add_password_entry.get().strip()

    if not username or not password:
        messagebox.showwarning("Missing Fields", "Please enter both username and password.")
        return

    result = add_user(username, password)
    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

add_button = tk.Button(tab_add_user, text="Add User", command=on_add_user)
add_button.pack()

# -------------------- Delete User Tab --------------------
tab_delete_user = ttk.Frame(tab_control)
tab_control.add(tab_delete_user, text="Delete User")

delete_username_label = tk.Label(tab_delete_user, text="Username:")
delete_username_label.pack()
delete_username_entry = tk.Entry(tab_delete_user)
delete_username_entry.pack()

def on_delete_user():
    username = delete_username_entry.get().strip()

    if not username:
        messagebox.showwarning("Missing Field", "Please enter a username.")
        return

    result = delete_user(username)
    if "does not exist" in result.lower():
        messagebox.showwarning("User Not Found", result)
    elif result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

delete_button = tk.Button(tab_delete_user, text="Delete User", command=on_delete_user)
delete_button.pack()

# -------------------- Modify User Tab --------------------
tab_modify_user = ttk.Frame(tab_control)
tab_control.add(tab_modify_user, text="Modify User")

modify_username_label = tk.Label(tab_modify_user, text="Username:")
modify_username_label.pack()
modify_username_entry = tk.Entry(tab_modify_user)
modify_username_entry.pack()

modify_option_label = tk.Label(tab_modify_user, text="Modify Option:")
modify_option_label.pack()
modify_option_var = tk.StringVar()
option_combobox = Combobox(tab_modify_user, textvariable=modify_option_var)
option_combobox['values'] = ['-l', '-d', '-s', '-c', '-u', '-g']  # Common usermod options
option_combobox.pack()

modify_value_label = tk.Label(tab_modify_user, text="New Value:")
modify_value_label.pack()
modify_value_entry = tk.Entry(tab_modify_user)
modify_value_entry.pack()

def on_modify_user():
    username = modify_username_entry.get().strip()
    option = modify_option_var.get().strip()
    value = modify_value_entry.get().strip()

    if not username or not option or not value:
        messagebox.showwarning("Missing Fields", "Please fill in all fields.")
        return

    result = modify_user(username, option, value)

    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

modify_button = tk.Button(tab_modify_user, text="Modify User", command=on_modify_user)
modify_button.pack()

# -------------------- Finalize GUI --------------------
tab_control.pack(expand=1, fill="both")
root.mainloop()
