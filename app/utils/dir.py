import os


def list_files(directory: str):
    """
    List all files in a directory.
    """
    print(f"\nFiler i mappen '{directory}':")
    for file in os.listdir(directory):
        print(f" - {file}")