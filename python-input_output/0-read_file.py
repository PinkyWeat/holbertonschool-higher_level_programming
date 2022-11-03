#!/usr/bin/python3
"""Module"""


def read_file(filename=""):
    """reads a text file (UT8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    print(f"{read_data}", end="")
