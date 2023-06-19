"""
 in this program we have to use two database(sqlite and postgreSQL).
 
 for that we use Factory Design Pattern 
    - there is interface of class Repository_Database
        - Sqlite_Repository and postgreSQL_Repository is their concrete classes
    - in Repository_Database we define our operations that we have to required 
        - INSERT,UPDATE and DELETE

"""
import click

# this is instance of database
def create_table():
    # click.echo("which database you want to use to store task:\n 1) Sqlite  \n 2) PostgreSQL")
    # user_input = int(input("enter your choice"))
    # if user_input == 1:
    #     s.Sqlite_Repository
    # elif user_input == 2:
    #     p.postgreSQL_Repository()
    create_table_sqlitetask = '''CREATE TABLE IF NOT EXISTS task (
                                    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    task TEXT NOT NULL,
                                    description TEXT NOT NULL,
                                    due_date DATE NOT NULL
                                    )'''
    create_table_if_not_exist('task',create_table_sqlitetask)

class Repository_Database:
    
    def execute_query(self):
        pass



# concreate class of database
class sqlite_Repository(Repository_Database):
    
    def execute_query(self):
        query = f"INSERT INTO task (task, description, due_date) VALUES ('{task}', '{description}', '{due_date}')"

        return



# concrete class of database
class postgreSQL_Repository(Repository_Database):
    
    def execute_query(self):
        pass
    
        return

if __name__ == '__main__':
    db = Repository_Database()
    z = Sqlite_Repository

    # Calling the execute_query() method on the objects
    db.execute_query()
    db.execute_query()