#IMPORTS
import subprocess
from utils import logger

#MAIN
def main():
    subprocess.call(["python", "utils/dependency.py"])
    logger.finalize_logging()
    subprocess.call(["python", "main_gui.py"])
    
if __name__ == "__main__":
    main()