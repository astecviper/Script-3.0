# main.py
# IMPORTS
import subprocess
from utils.logger import setup_logging, logger

# MAIN
def main():
    setup_logging()
    logger.debug("Logging setup complete")
    subprocess.call(["python", "utils/dependency.py"])
    logger.debug("Dependency check complete")
    subprocess.call(["python", "utils/settings.py"])
    logger.debug("Settings initialization complete")
    logger.debug("Initializing GUI")
    subprocess.call(["python", "main_gui.py"])
    logger.debug("GUI initialization complete")

if __name__ == "__main__":
    main()
