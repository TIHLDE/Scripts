import os


def setup():
    # Create a folder named "downloads" in the root directory if it does not exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')