import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox, Notebook, Frame
import os
import subprocess

from utils.user_utils import add_user, delete_user, modify_user
from utils.group_utils import create_group, delete_group, add_user_to_group
from utils.permission_utils import change_permissions, change_owner

# ------------------ User Tab Functions ------------------

def on_add_user():
    username = add_username_entry.get().strip()
    if not username:
        messagebox.showwarning("Missing Field", "Please enter a username.")
        return
    result = add_user(username)
    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

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

def on_user_stats():
    username = modify_username_entry.get().strip()
    if not username:
        messagebox.showwarning("Missing Field", "Enter username to fetch stats.")
        return
    try:
        disk_usage = subprocess.getoutput(f"sudo du -sh /home/{username}").split()[0]
        last_login = subprocess.getoutput(f"lastlog -u {username}")
        messagebox.showinfo("User Stats", f"Disk Usage: {disk_usage}\n\n{last_login}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_user():
    username = search_user_entry.get().strip()
    if not username:
        messagebox.showwarning("Missing Field", "Enter a username to search.")
        return
    try:
        with open("/etc/passwd", 'r') as f:
            matches = [line for line in f if username in line]
            if matches:
                messagebox.showinfo("User Found", "".join(matches))
            else:
                messagebox.showinfo("No Match", "User not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ------------------ Group Tab Functions ------------------

def on_create_group():
    groupname = create_group_entry.get().strip()
    if not groupname:
        messagebox.showwarning("Missing Field", "Please enter a group name.")
        return
    result = create_group(groupname)
    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

def on_delete_group():
    groupname = delete_group_entry.get().strip()
    if not groupname:
        messagebox.showwarning("Missing Field", "Please enter a group name.")
        return
    result = delete_group(groupname)
    if "does not exist" in result.lower():
        messagebox.showwarning("Group Not Found", result)
    elif result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

def on_add_user_to_group():
    username = add_user_group_username_entry.get().strip()
    groupname = add_user_group_group_entry.get().strip()
    if not username or not groupname:
        messagebox.showwarning("Missing Fields", "Please enter both username and group name.")
        return
    result = add_user_to_group(username, groupname)
    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

# ------------------ Permission Tab Functions ------------------

def on_change_permissions():
    path = perm_path_entry.get().strip()
    mode = perm_mode_entry.get().strip()
    if not path or not mode:
        messagebox.showwarning("Missing Fields", "Please enter both path and mode.")
        return
    if not os.path.exists(path):
        messagebox.showerror("Error", f"The path '{path}' does not exist.")
        return
    result = change_permissions(path, mode)
    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

def on_change_owner():
    path = owner_path_entry.get().strip()
    owner = owner_owner_entry.get().strip()
    if not path or not owner:
        messagebox.showwarning("Missing Fields", "Please enter both path and owner.")
        return
    if not os.path.exists(path):
        messagebox.showerror("Error", f"The path '{path}' does not exist.")
        return
    result = change_owner(path, owner)
    if result.lower().startswith("error"):
        messagebox.showerror("Failed", result)
    else:
        messagebox.showinfo("Success", result)

# ------------------ Main GUI Setup ------------------

root = tk.Tk()
root.title("PermiControl - User, Group & Permission Manager")
root.geometry("600x600")


def toggle_dark_mode():
    current_bg = root.cget("bg")
    dark_bg = "#2e2e2e"
    light_bg = "lightgrey"  # Cross-platform safe alternative
    bg = dark_bg if current_bg != dark_bg else light_bg
    fg = "white" if bg == dark_bg else "black"
    
    root.configure(bg=bg)

    for child in root.winfo_children():
        try:
            child.configure(bg=bg, fg=fg)
        except:
            pass



dark_mode_button = tk.Button(root, text="🌗 Toggle Dark Mode", command=toggle_dark_mode)
dark_mode_button.pack(pady=5)

tab_control = Notebook(root)

# -- User Management Tab --
tab_user = Frame(tab_control)
tab_control.add(tab_user, text="User Management")

# Search User Widgets
tk.Label(tab_user, text="Search User").pack(pady=(10, 0))
search_user_entry = tk.Entry(tab_user)
search_user_entry.pack()
tk.Button(tab_user, text="Search", command=search_user).pack(pady=5)

# Add User Widgets
tk.Label(tab_user, text="Add User").pack(pady=(10, 0))
tk.Label(tab_user, text="Username").pack()
add_username_entry = tk.Entry(tab_user)
add_username_entry.pack()
tk.Button(tab_user, text="Add User", command=on_add_user).pack(pady=5)

# Delete User Widgets
tk.Label(tab_user, text="Delete User").pack(pady=(20, 0))
tk.Label(tab_user, text="Username").pack()
delete_username_entry = tk.Entry(tab_user)
delete_username_entry.pack()
tk.Button(tab_user, text="Delete User", command=on_delete_user).pack(pady=5)

# Modify User Widgets
tk.Label(tab_user, text="Modify User").pack(pady=(20, 0))
tk.Label(tab_user, text="Username").pack()
modify_username_entry = tk.Entry(tab_user)
modify_username_entry.pack()

tk.Label(tab_user, text="Modify Option").pack()
modify_option_var = tk.StringVar()
modify_option_combobox = Combobox(tab_user, textvariable=modify_option_var)
modify_option_combobox['values'] = ['-l', '-d', '-s', '-c', '-u', '-g']
modify_option_combobox.pack()

tk.Label(tab_user, text="New Value").pack()
modify_value_entry = tk.Entry(tab_user)
modify_value_entry.pack()

tk.Button(tab_user, text="Modify User", command=on_modify_user).pack(pady=5)

# User Stats Button
tk.Button(tab_user, text="Show User Stats", command=on_user_stats).pack(pady=5)

# -- Group Management Tab --
tab_group = Frame(tab_control)
tab_control.add(tab_group, text="Group Management")

tk.Label(tab_group, text="Create Group").pack(pady=(10, 0))
tk.Label(tab_group, text="Group Name").pack()
create_group_entry = tk.Entry(tab_group)
create_group_entry.pack()
tk.Button(tab_group, text="Create Group", command=on_create_group).pack(pady=5)

tk.Label(tab_group, text="Delete Group").pack(pady=(20, 0))
tk.Label(tab_group, text="Group Name").pack()
delete_group_entry = tk.Entry(tab_group)
delete_group_entry.pack()
tk.Button(tab_group, text="Delete Group", command=on_delete_group).pack(pady=5)

tk.Label(tab_group, text="Add User to Group").pack(pady=(20, 0))
tk.Label(tab_group, text="Username").pack()
add_user_group_username_entry = tk.Entry(tab_group)
add_user_group_username_entry.pack()
tk.Label(tab_group, text="Group Name").pack()
add_user_group_group_entry = tk.Entry(tab_group)
add_user_group_group_entry.pack()
tk.Button(tab_group, text="Add User to Group", command=on_add_user_to_group).pack(pady=5)

# -- Permission Management Tab --
tab_perm = Frame(tab_control)
tab_control.add(tab_perm, text="Permission Management")

tk.Label(tab_perm, text="Change Permissions").pack(pady=(10, 0))
tk.Label(tab_perm, text="File/Directory Path").pack()
perm_path_entry = tk.Entry(tab_perm, width=50)
perm_path_entry.pack()
tk.Label(tab_perm, text="Permission Mode (e.g. 755)").pack()
perm_mode_entry = tk.Entry(tab_perm)
perm_mode_entry.pack()
tk.Button(tab_perm, text="Change Permissions", command=on_change_permissions).pack(pady=5)

tk.Label(tab_perm, text="Change Owner").pack(pady=(20, 0))
tk.Label(tab_perm, text="File/Directory Path").pack()
owner_path_entry = tk.Entry(tab_perm, width=50)
owner_path_entry.pack()
tk.Label(tab_perm, text="New Owner (username:group)").pack()
owner_owner_entry = tk.Entry(tab_perm)
owner_owner_entry.pack()
tk.Button(tab_perm, text="Change Owner", command=on_change_owner).pack(pady=5)

tab_control.pack(expand=1, fill="both")

root.mainloop()

