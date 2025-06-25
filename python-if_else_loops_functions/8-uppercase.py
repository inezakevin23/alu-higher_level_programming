#!/usr/bin/python3

def uppercase(str):
    """
    Prints the input string in uppercase followed by a new line.
    Only lowercase letters are converted; other characters remain unchanged.
    """
    result = ""
    for char in str:
        code = ord(char)
        # if char is lowercase a-z, convert to uppercase
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += char
    # Print using string format
    print("{}".format(result))
