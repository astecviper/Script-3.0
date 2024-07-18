# logger.py
import logging
import os
import json
from datetime import datetime

# Create Logs directory if it doesn't exist
log_dir = 'Logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging
log_file = os.path.join(log_dir, 'app.log')
print(f"Creating log file: {log_file}")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create file handler
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Color coding for log levels
class CustomFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': '\033[92m',  # Green
        'INFO': '\033[94m',   # Blue
        'WARNING': '\033[93m',# Yellow
        'ERROR': '\033[91m',  # Red
        'CRITICAL': '\033[95m'# Magenta
    }
    RESET = '\033[0m'

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, self.RESET)
        record.msg = f"{log_color}{record.msg}{self.RESET}"
        return super().format(record)

# Apply custom formatter to the console handler
console_handler.setFormatter(CustomFormatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def close_log_handlers():
    for handler in logger.handlers[:]:
        handler.close()
        logger.removeHandler(handler)

def finalize_logging():
    settings_file = 'ettings.json'
    save_logs = False  # Default to disabled

    # Check if settings.json exists
    if os.path.exists(settings_file):
        with open(settings_file, 'r') as f:
            settings = json.load(f)
            save_logs = settings.get('save_logs', False)

    # Close all logging handlers
    close_log_handlers()

    # Check if saving logs is enabled
    if save_logs:
        timestamp = datetime.now().strftime("%m-%d-%Y - %H-%M-%S")
        new_log_file = os.path.join(log_dir, f"Aztec's Speed-Up & Clean-Up [{timestamp}].log")
        print(f"Renaming log file to: {new_log_file}")
        os.rename(log_file, new_log_file)
    else:
        print(f"Deleting log file: {log_file}")
        if os.path.exists(log_file):
            os.remove(log_file)

# Test the logger
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")