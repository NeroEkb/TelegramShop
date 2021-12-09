import sqlite3
from item import Item


def get(name):
    try:
        sqlite_connection = sqlite3.connect(name)
        cursor = sqlite_connection.cursor()
        result = cursor.execute('SELECT * FROM `items`').fetchall()
        return [Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in result]
    except sqlite3.Error as error:
        print(error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()


#TODO: change rerturn func