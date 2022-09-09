#!/usr/bin/python3
i = 0
while i != 100:
    if i == 99:
       print(f"{i}")
       break
    if i < 10:
        print(f"0{i}, ", end="")
    else:
        print(f"{i}, ", end="")
    i = i + 1