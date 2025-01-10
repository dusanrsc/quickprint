# USE QUICKPRINT TO REDUCE TIME OF TYPING FOR STANDARD PRINT() AND INPUT() FUNCTIONS.

# ESPECIALLY USEFULL FOR REDUCING TIME SPENT IN MASSIVE PROJECTS WITH A LOT OF DEBUGGING.

# USE IT AS STANDARD PYTHONS INPUT() AND PRINT() FUNCTIONS.

# How To Set-Up?
# Download QuickPrint Library From GitHub with:
    python -m pip install git+https://github.com/dusanrsc/quickprint.git

# OR Upgrade QuickPrint:
    python -m pip install --upgrade git+https://github.com/dusanrsc/quickprint.git

# How To Use?
    from quickprint.quickprint import *

    _input = i("Your Name: ")
    p(f"Hello, {_input}!")

# Output:
    Hello, Dušan!

# Uninstall QuickPrint:
    python -m pip uninstall quickprint
