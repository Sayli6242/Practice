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
        
    def create_table(self,table_name,columns):
        column_definitions = ', '.join(columns)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions}, status TEXT DEFAULT 'pending')"

        self.cur.execute(create_table_query)
        self.con.commit()
        print(f'table {table_name} created successfully')

    def insert_query(self, task_title,task_description,due_date, status):
        query = "INSERT INTO task (task_title, task_description, due_date, status) VALUES (?, ?, ?, 'pending')"
        self.cur.execute(query,(task_title, task_description, due_date, status))
        self.con.commit()
        print(f'task add successfully with id {task_id}')        
        return  

    def update_query(self,task_id,task_title,task_description,task_due_date):
        query = "UPDATE task SET task_title = ?, task_discription = ?, due_date = ? WHERE task_id = ?"
        self.cur.execute(query)
        self.con.commit()
        print('task updated successfully')
        return

    def delete_query(self,task_id):
        query = "DELETE FROM task WHERE task_id = ?"  # Update the column name to task_id
        self.cur.execute(query)
        self.con.commit()
        print('Delete task successfully')
        return

    
        

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

    def create_table():
        pass

    def insert_query():
        pass
    
    def update_query():
        pass

    
    def delete_query():
        pass
    


if __name__ == '__main__':

    db = Repository_Database()
  
