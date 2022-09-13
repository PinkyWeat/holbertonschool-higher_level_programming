#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addMe = 0
    for adding in sys.argv[1:]:
        addMe += int(adding)
    print(addMe)
