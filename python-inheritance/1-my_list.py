#!/usr/bin/python3
"""Python Interpreter"""

class MyList(list):
    """new class inherits from list"""

    def print_sorted(self):
        """prints"""
        print(sorted(self))
