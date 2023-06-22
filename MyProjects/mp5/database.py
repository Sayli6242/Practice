"""
 in this program we have to use two database(sqlite and postgreSQL).
 
 for that we use Factory Design Pattern 
    - there is interface of class Repository_Database
        - Sqlite_Repository and postgreSQL_Repository is their concrete classes
    - in Repository_Database we define our operations that we have to required 
        - INSERT,UPDATE and DELETE

"""
import click
from mp4helpers.sqliteHelper import create_table_if_not_exist
from mp4helpers.sqliteHelper import execute_query
# this is instance of database
                             


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
    
    def create_table():
        create_table_task = "CREATE TABLE IF NOT EXISTS task(task_id INTEGER PRIMARY KEY AUTOINCREMENT,task_title TEXT,task_description TEXT,task_due_date integer)"
        create_table_if_not_exist("task", create_table_task)
        return 

    def insert_query(self, task_title,task_description,task_due_date):
        query = "INSERT INTO task (task_title, task_description, task_due_date) VALUES (?, ?, ?)"
        parameters = (task_title, task_description,task_due_date)
        result , task_id = execute_query(query, parameters)
        print(f'task add successfully with id {task_id}')        
        return  

    def update_query(self,task_id,task_title,task_description,task_due_date):
        query = "UPDATE task SET task_title = ?, task_discription = ?, due_date = ? WHERE task_id = ?"
        parameters = (task_id,task_title, task_description,task_due_date)
        result = execute_query(query,parameters)
        print('task updated successfully')
        return

    def delete_query(self,task_id):
        query = "DELETE FROM task WHERE task_id = ?"  # Update the column name to task_id
        parameters = (task_id,)
        result = execute_query(query, parameters)
        print('Delete task successfully')
        return
        

# concrete class of database
class postgreSQL_Repository(Repository_Database):

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
  
