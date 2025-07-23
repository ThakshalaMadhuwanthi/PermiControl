
import subprocess
import logging
import pwd
from utils.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def add_user(username):
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        logger.info(f"User '{username}' added successfully.")
        return f"User '{username}' added successfully."
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to add user '{username}': {e}")
        return f"Failed to add user '{username}': {e}"

def delete_user(username):
    try:
        pwd.getpwnam(username)  # Check if user exists
    except KeyError:
        return f"User '{username}' does not exist."
    
    try:
        subprocess.run(['sudo', 'userdel', '-r', username], check=True)
        logger.info(f"User '{username}' deleted successfully.")
        return f"User '{username}' deleted successfully."
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to delete user '{username}': {e}")
        return f"Failed to delete user '{username}': {e}"

VALID_OPTIONS = ['-l', '-d', '-s', '-c', '-u', '-g']  # Common usermod options

def modify_user(username, option, value):
    if option not in VALID_OPTIONS:
        return f"Error: Unsupported option '{option}'."

    try:
        subprocess.run(['sudo', 'usermod', option, value, username], check=True)
        logger.info(f"User '{username}' modified with {option} = {value}")
        return f"User '{username}' modified successfully."
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to modify user '{username}' with {option} {value}: {e}")
        return f"Error: Failed to modify user '{username}' with {option} {value}.\n{e}"



