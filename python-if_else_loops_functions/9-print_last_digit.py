#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        print(f"{abs(number) % 10}", end="")
        return abs(number) % 10
    elif number > 0:
        print(f"{number % 10}", end="")
        return number % 10
    else:
        print(f"{number}", end="")
        return number
