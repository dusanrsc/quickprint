# USE QUICKPRINT TO REDUCE TIME OF TYPING FOR STANDARD PRINT() AND INPUT() FUNCTIONS.
# ESPECIALLY USEFULL FOR REDUCING TIME SPENT IN MASSIVE PROJECTS WITH A LOT OF DEBUGGING.
# USE IT AS STANDARD PYTHONS INPUT() AND PRINT() FUNCTIONS.

# "Primarily developed for self-use and for fun."
# "It opens the door for the development of future scalabile Python libraries."

# How To Set-Up?
# Download QuickPrint Library From GitHub with:
    python -m pip install git+https://github.com/dusanrsc/quickprint.git

# or Upgrade QuickPrint:
    python -m pip install --upgrade git+https://github.com/dusanrsc/quickprint.git

# How To Use? With Example.
```python
# Importing sub-modules.
from quickprint.quickprint import *

# Code example.
_input = i("Your Name: ")

p(f"Hello, {_input}!")
p("Hello, world!")
```
# Output Example:
    Hi, Dušan!
    Hello, world!

# Uninstall QuickPrint:
    python -m pip uninstall quickprint
