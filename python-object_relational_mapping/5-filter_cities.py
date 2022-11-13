#!/usr/bin/python3
"""Python Module"""
import MySQLdb
from sys import argv


"""SQL Query"""
if __name__ == "__main__":
    """Will connect to htbn_0e_0_usa and
    list all cities in state"""

    try:
        dataB = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            password=argv[2],
            dataB=argv[3]
        )
    except Exception:
        print("Error")

    cursor = dataB.cursor()
    cursor.execute("""SELECT cities.name FROM cities \
                    JOIN states ON  cities.state_id = states.id WHERE \
                    BINARY states.name = %s""", (argv[4],))
    result = cursor.fetchall()

    for st in result:
        for cit in st:
            if st == result[0]:
                print(cit, end="")
            else:
                print(f", {cit}", end="")
    print()
    cursor.close()
    dataB.close()