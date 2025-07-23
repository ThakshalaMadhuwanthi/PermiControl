
import subprocess
import logging
from utils.logger import setup_logging

setup_logging()

def add_user(username):
    try:
        subprocess.run(['sudo', 'useradd', username], check=True)
        logging.info(f"User '{username}' added successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to add user '{username}': {e}")

def delete_user(username):
    try:
        subprocess.run(['sudo', 'userdel', '-r', username], check=True)
        logging.info(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to delete user '{username}': {e}")

def modify_user(username, option, value):
    try:
        subprocess.run(['sudo', 'usermod', option, value, username], check=True)
        logging.info(f"User '{username}' modified with {option} = {value}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to modify user '{username}': {e}")
