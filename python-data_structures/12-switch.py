#!/usr/bin/python3
from dataclasses import replace


a = 89
b = 10
c = a
a = b
b = c
print("a={:d} - b={:d}".format(a, b))
