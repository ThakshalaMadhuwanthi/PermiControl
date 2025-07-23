
# utils/logger.py

import logging
import os

def setup_logging():
    os.makedirs("logs", exist_ok=True)  # Ensure logs/ directory exists
    logging.basicConfig(
        filename='logs/permicontrol.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

