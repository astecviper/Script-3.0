# main.py
# IMPORTS
import subprocess
from utils.logger import setup_logging, finalize_logging, logger

# MAIN
def main():
    setup_logging()
    logger.debug("Logging setup complete")
    subprocess.call(["python", "utils/dependency.py"])
    finalize_logging()
    subprocess.call(["python", "main_gui.py"])

if __name__ == "__main__":
    main()
