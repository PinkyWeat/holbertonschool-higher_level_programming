#!/usr/bin/python3
"""prints My name is <first name> <last name>"""


import string


def say_my_name(first_name, last_name=""):
    """say's the name"""

    if type(first_name) or type(last_name) is not string:
        raise TypeError("first_name must be a string")
    print(f"My name is {first_name} {last_name}")
