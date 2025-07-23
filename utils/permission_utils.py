
import subprocess
import logging
from utils.logger import setup_logging

setup_logging()

def change_permissions(path, mode):
    try:
        subprocess.run(['chmod', mode, path], check=True)
        logging.info(f"Permissions for '{path}' changed to '{mode}'.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to change permissions for '{path}': {e}")

def change_owner(path, owner):
    try:
        subprocess.run(['chown', owner, path], check=True)
        logging.info(f"Owner of '{path}' changed to '{owner}'.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to change owner of '{path}': {e}")
