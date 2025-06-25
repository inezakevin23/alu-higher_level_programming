#!/usr/bin/python3

def uppercase(text):
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

