import os
import shutil
import sys

def copy_file(source: str, destination: str) -> None:
  
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")
    if os.path.isdir(source):
        raise IsADirectoryError(f"Source '{source}' is a directory, not a file.")

    
    if os.path.isdir(destination):
        dest_path = os.path.join(destination, os.path.basename(source))
    else:
        dest_path = destination

    
    if os.path.abspath(source) == os.path.abspath(dest_path):
        raise ValueError("Source and destination are the same file.")

    
    shutil.copy2(source, dest_path)
    print(f"Copied '{source}' -> '{dest_path}'")

def delete_path(path: str) -> None:

    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist.")

    if os.path.isfile(path):
        os.remove(path)
        print(f"Deleted file '{path}'")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print(f"Deleted directory '{path}'")
    else:
        raise TypeError(f"'{path}' is neither file nor directory.")
    
    



