"""
 in this program we have to use two database(sqlite and postgreSQL).
 
 for that we use Factory Design Pattern 
    - there is interface of class Repository_Database
        - Sqlite_Repository and postgreSQL_Repository is their concrete classes
    - in Repository_Database we define our operations that we have to required 
        - INSERT,UPDATE and DELETE

"""
import click
import sqlite3
from  psycopg2 import connect
# this is instance of database
# make this implementation generic to use
# make all query dynamic to use for multiple table and multiple values
# take table name as input form above layer
# all those things required is input to function

class Repository_Database:
    
    def create_table():
        pass
    
    def insert_query():
        pass

    def update_query():
        pass

    def delete_query():
        pass

# concreate class of database
class sqlite_Repository(Repository_Database):
    def __init__(self):
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()
        
    def create_table(self,table_name,columns,status):
        column_definitions = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions}, status TEXT DEFAULT '{status}')"
        self.cur.execute(create_table_query)
        self.con.commit()
        print(f'table {table_name} created successfully')

    def insert_query(self, table_name,columns,values):
        column_names = ', '.join(columns)
        placeholders = ', '.join(['?' for _ in values])
        query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
        self.cur.execute(query, values)
        task_id = self.cur.lastrowid
        self.con.commit()
        print(f'task add successfully with id {task_id}')        
        return  

    def update_query(self, table_name, set_values, condition_column, condition_value):
        set_clause = ', '.join([f"{column} = ?" for column in set_values])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_column} = ?"
        values = list(set_values.values()) + [condition_value]
        self.cur.execute(query,values)
        self.cur.lastrowid
        self.cur.fetchall()
        self.con.commit()
        print('task updated successfully')
        return

    def delete_query(self,table_name,id_column,id_value):
        query = f"DELETE FROM {table_name} WHERE {id_column} = ?"
        values = (id_value,)
        self.cur.execute(query,values)
        self.con.commit()
        print("Task deleted successfully")
        return

    def retrieve_pending_tasks(self,status):
        query = "SELECT * FROM tasks WHERE status = ?"
        self.cur.execute(query, (status,))
        tasks = self.cur.fetchall()
        return tasks

    def retrieve_inprogress_tasks(self,status):
        query = "SELECT * FROM tasks WHERE status = ?"
        self.cur.execute(query, (status,))
        tasks = self.cur.fetchall()
        return tasks

    def retrieve_completed_tasks(self, status):
        query = "SELECT * FROM tasks WHERE status = ?"
        self.cur.execute(query, (status,))
        tasks = self.cur.fetchall()
        return tasks

# concrete class of database
class postgreSQL_Repository(Repository_Database):

    def __init__(self):
        self.con = connect(
            host = "localhost",
            port = "5432",
            database ="postgres",
            user = "postgres",
            password = "mysecretpassword",
        )
    
        self.cur = self.con.cursor()

    def create_table(self, table_name, columns, status):
        column_definitions = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions}, status TEXT DEFAULT '{status}')"
        self.cur.execute(create_table_query)
        self.con.commit()
        print(f"Table {table_name} created successfully")

    def insert_query(self, table_name, columns, values):
        column_names = ', '.join(columns)
        placeholders = ', '.join(['%s' for _ in values])
        query = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"
        self.execute(query, values)
        task_id = self.get_last_inserted_id(table_name)
        print(f"Task added successfully with id {task_id}")
        return

    def get_last_inserted_id(self, table_name):
        query = f"SELECT lastval() FROM {table_name}"
        con = psycopg2.connect(
            host="localhost",
            port = "5432",
            database="postgres",
            user="postgres",
            password="mysecretpassword"
        )
        self.cur.execute(query)
        task_id = cursor.fetchone()[0]
        return task_id
    
    def update_query(self, table_name, set_values, condition_column, condition_value):
        set_clause = ', '.join([f"{column} = %s" for column in set_values])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_column} = %s"
        values = list(set_values.values()) + [condition_value]
        self.cur.execute(query, values)
        print("Task updated successfully")
        return

    
    def delete_query(self, table_name, id_column, id_value):
        query = f"DELETE FROM {table_name} WHERE {id_column} = %s"
        values = (id_value,)
        self.cur.execute(query, values)
        print("Task deleted successfully")
        return
    
    def retrieve_pending_tasks(self, status):
        query = "SELECT * FROM tasks WHERE status = %s"
        self.cur.execute(query, (status,))
        tasks = self.cur.fetchall()
        return tasks

    def retrieve_inprogress_tasks(self, status):
        query = "SELECT * FROM tasks WHERE status = %s"
        self.cur.execute(query, (status,))
        tasks = self.cur.fetchall()
        return tasks

    def retrieve_completed_tasks(self, status):
        query = "SELECT * FROM tasks WHERE status = %s"
        self.cur.execute(query, (status,))
        tasks = self.cur.fetchall()
        return tasks

if __name__ == '__main__':

    db = Repository_Database()
  
