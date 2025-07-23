import subprocess
import logging
import grp
from utils.logger import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def create_group(groupname):
    try:
        subprocess.run(['sudo', 'groupadd', groupname], check=True)
        logger.info(f"Group '{groupname}' created successfully.")
        return f"Group '{groupname}' created successfully."
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to create group '{groupname}': {e}")
        return f"Failed to create group '{groupname}': {e}"

def delete_group(groupname):
    try:
        grp.getgrnam(groupname)  # Check if group exists
    except KeyError:
        return f"Group '{groupname}' does not exist."

    try:
        subprocess.run(['sudo', 'groupdel', groupname], check=True)
        logger.info(f"Group '{groupname}' deleted successfully.")
        return f"Group '{groupname}' deleted successfully."
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to delete group '{groupname}': {e}")
        return f"Failed to delete group '{groupname}': {e}"

def add_user_to_group(username, groupname):
    try:
        subprocess.run(['sudo', 'usermod', '-aG', groupname, username], check=True)
        logger.info(f"User '{username}' added to group '{groupname}' successfully.")
        return f"User '{username}' added to group '{groupname}' successfully."
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to add user '{username}' to group '{groupname}': {e}")
        return f"Failed to add user '{username}' to group '{groupname}': {e}"

