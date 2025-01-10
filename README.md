# USE QUICKPRINT TO REDUCE TIME OF TYPING FOR STANDARD PRINT() AND INPUT() FUNCTIONS.
# ESPECIALLY USEFULL FOR REDUCING TIME SPENT IN MASSIVE PROJECTS WITH A LOT OF DEBUGGING.
# USE IT AS STANDARD PYTHONS INPUT() AND PRINT() FUNCTIONS.

# How To Set-Up?
# Download QuickPrint Library From GitHub with:
    python -m pip install git+https://github.com/dusanrsc/quickprint.git

# or Upgrade QuickPrint:
    python -m pip install --upgrade git+https://github.com/dusanrsc/quickprint.git

# How To Use Example?
    # Importing modules.
    from quickprint.quickprint import *

    # Code example.
    _input = i("Your Name: ")
    p(f"Hello, {_input}!")

# Output Example:
    Hello, Dušan!

# Uninstall QuickPrint:
    python -m pip uninstall quickprint
