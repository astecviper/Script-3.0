import json
import os

try:
    from utils.logger import setup_logging, logger
except ModuleNotFoundError as e:
    print(f"Error importing logger: {e}")
    setup_logging = None
    logger = None

# Path to settings.json
settings_file = os.path.join(os.path.dirname(__file__), 'settings.json')

# Default settings structure
default_settings = {
    "enabled_tests": [],
    "custom_presets": [],
    "scheduled_presets": [],
    "settings": {
        "logging_level": "DEBUG",
        "save_logs": False,
        "save_summaries": False  # Added save_summaries setting
    }
}

def create_default_settings():
    """Create the settings file with default settings."""
    try:
        with open(settings_file, 'w') as f:
            json.dump(default_settings, f, indent=4)
        if logger:
            logger.info("Default settings file created.")
        else:
            print("Default settings file created.")
    except Exception as e:
        if logger:
            logger.error(f"Error creating default settings file: {e}")
        else:
            print(f"Error creating default settings file: {e}")

def load_settings():
    """Load settings from the settings file, creating the file if it doesn't exist."""
    try:
        if not os.path.exists(settings_file):
            if logger:
                logger.info("Settings file not found. Creating a new one with default settings.")
            else:
                print("Settings file not found. Creating a new one with default settings.")
            create_default_settings()
        
        with open(settings_file, 'r') as f:
            if logger:
                logger.info("Loading settings from file.")
            else:
                print("Loading settings from file.")
            return json.load(f)
    except Exception as e:
        if logger:
            logger.error(f"Error loading settings: {e}")
        else:
            print(f"Error loading settings: {e}")
        return default_settings

def save_settings(settings):
    """Save settings to the settings file."""
    try:
        with open(settings_file, 'w') as f:
            json.dump(settings, f, indent=4)
        if logger:
            logger.info("Settings saved to file.")
        else:
            print("Settings saved to file.")
    except Exception as e:
        if logger:
            logger.error(f"Error saving settings: {e}")
        else:
            print(f"Error saving settings: {e}")

def update_settings(key, value):
    """Update a specific setting in the settings file."""
    try:
        settings = load_settings()
        keys = key.split('.')
        d = settings
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value
        save_settings(settings)
    except Exception as e:
        if logger:
            logger.error(f"Error updating settings: {e}")
        else:
            print(f"Error updating settings: {e}")

if __name__ == "__main__":
    if setup_logging:
        setup_logging()
    if logger:
        logger.debug("Initializing settings script")
    else:
        print("Initializing settings script")
    
    settings = load_settings()  # Ensure settings are loaded or created
    
    if logger:
        logger.debug("Settings script completed")
    else:
        print("Settings script completed")
