import os

from app.config import config


def setup():
    # Create a folder named "downloads" in the root directory if it does not exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    # Create a folder named "upload" in the root directory if it does not exist
    if not os.path.exists('upload'):
        os.makedirs('upload')

    # Load the configuration file
    config.load_config()