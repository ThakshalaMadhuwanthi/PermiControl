
import logging
import os
import sys

def setup_logging():
    os.makedirs("logs", exist_ok=True)

    # Prevent duplicate handlers if setup_logging() is called multiple times
    if len(logging.getLogger().handlers) > 0:
        return

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/permicontrol.log"),
            logging.StreamHandler(sys.stdout)  # Also logs to terminal/GUI console
        ]
    )

