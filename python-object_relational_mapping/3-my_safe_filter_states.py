#!/usr/bin/python3
"""Python Module"""
import MySQLdb
from sys import argv


"""SQL Query"""
if __name__ == "__main__":
    dataB = MySQLdb.connect(
        host="localhost"
        port=3306,
        user=argv[1],
        password=arg[2],
        database=argv[3]
    )

    cursor = dataB.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4], ))
    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
