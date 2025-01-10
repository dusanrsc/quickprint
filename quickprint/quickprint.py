# quickprint/quickprint.py

def p(*args, **kwargs):
    """
    Function p() that replaces print() with all its capabilities.

    *args: Arguments we want to print.
    **kwargs: All additional options used by print(), such as sep, end, file, etc.
    """
    print(*args, **kwargs)


def i(prompt="", /):
    """
    Function i() that replaces input() with all its capabilities.

    prompt: String displayed to the user before they enter data (optional).
    """
    return input(prompt)
