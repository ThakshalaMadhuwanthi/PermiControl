
import subprocess
import logging
from utils.logger import setup_logging

setup_logging()

def create_group(groupname):
    try:
        subprocess.run(['sudo', 'groupadd', groupname], check=True)
        logging.info(f"Group '{groupname}' created successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to create group '{groupname}': {e}")

def delete_group(groupname):
    try:
        grp.getgrnam(groupname)  # Will raise KeyError if group doesn't exist
    except KeyError:
        return f"Group '{groupname}' does not exist."

    try:
        subprocess.run(['sudo', 'groupdel', groupname], check=True)
        return f"Group '{groupname}' deleted successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to delete group '{groupname}': {e}"
def add_user_to_group(username, groupname):
    try:
        subprocess.run(['sudo', 'usermod', '-aG', groupname, username], check=True)
        logging.info(f"User '{username}' added to group '{groupname}' successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to add user '{username}' to group '{groupname}': {e}")
