import sqlite3
# this function take query and parameters and execute different queries
def execute_query(query, parameters=None):
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    if parameters:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    return result, cursor.lastrowid

def create_table_if_not_exist(table_name, create_query):
    with sqlite3.connect("database.db") as con:
        cursor = con.cursor()
        
        # Check if the table exists
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone()
        
        if result is None:
            # Create the table
            cursor.execute(create_query)
            con.commit()
            print(f"Table '{table_name}' created successfully.")
        else:
            print(f"Table '{table_name}' already exists.")


