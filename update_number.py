#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Ensure script works from its directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def read_number():
    """
    Reads the number from 'number.txt'.
    Ensures the file content is valid and returns an integer.
    """
    with open('number.txt', 'r') as f:
        content = f.read().strip()
        if not content.isdigit():
            raise ValueError("Content of 'number.txt' is not a valid number")
        return int(content)

def write_number(num):
    """
    Writes the given number to 'number.txt'.
    """
    with open('number.txt', 'w') as f:
        f.write(str(num))

def git_commit():
    """
    Stages and commits the 'number.txt' file with a message containing the current date.
    """
    try:
        # Stage the changes
        subprocess.run(['git', 'add', 'number.txt'], check=True)
        
        # Create commit with the current date
        date = datetime.now().strftime('%Y-%m-%d')
        commit_message = f"Update number: {date}"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Git command failed: {e}")

def main():
    """
    Main function to increment the number, update the file, and commit the change.
    """
    try:
        # Read, increment, and write the number
        current_number = read_number()
        new_number = current_number + 1
        write_number(new_number)
        
        # Commit the change
        git_commit()
        
    except FileNotFoundError as e:
        print(f"File error: {str(e)}")
    except ValueError as e:
        print(f"Value error: {str(e)}")
    except RuntimeError as e:
        print(f"Runtime error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
