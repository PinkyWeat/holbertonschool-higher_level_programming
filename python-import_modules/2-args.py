#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    elif len(sys.argv) > 2:
        print(f"{len(sys.argv) - 1} arguments:")
    e = 1
    for arg in sys.argv[1:]:
        print(f"{e}: {arg}")
        e += 1
