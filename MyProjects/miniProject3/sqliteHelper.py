import sqlite3

def execute_query(query, parameters=None):
    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        con.commit()
        return result, cursor
