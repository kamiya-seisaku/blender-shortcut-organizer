# Existing code in __init__.py
# ...

# Add this code to check for Tkinter availability
import subprocess
import sys

def check_tkinter_availability():
    try:
        import tkinter
        print('Tkinter is available.')
    except ImportError:
        print('Tkinter is not available. Installing...')
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tk'])
            print('Tkinter installed successfully.')
        except subprocess.CalledProcessError as e:
            print(f'An error occurred while installing Tkinter: {e}')

# Call the function to check for Tkinter
check_tkinter_availability()

# Continue with your existing code
# ...
