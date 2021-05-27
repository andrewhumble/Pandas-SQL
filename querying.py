import pyodbc
from pyodbc import Error
import pandas

# Framework to run queries on a SQL database in Python3

def create_database(connection, query):
    '''
    Creates a database on the given connection.

    Parameters:
        connection (string): connection object connected to the server
        query (string): the query to execute via the connection

    Returns:
        void - database is created

    '''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(server_name, database_name):
    '''
    Creates a server connection to connect to a database.

    Parameters:
        driver (string): the driver name of the database
        server (string): the server name
        database (string): the database name
        uid (string): the user id
        password (string): the password

    Returns:
        pyodc.Conneciton object referring to the requested server
        
    '''
    connection = None
    try:
        connection = pyodbc.connect(
                      'Driver={SQL Server};'
                      'Server=' + server_name + ';'
                      'Database=' + database_name + ';'
                      'Trusted_Connection=yes;')
        print("MS SQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    '''
    Executes a query on the given server

    Parameters:
        connection (string): connection object connected to the server
        query (string): the query to execute via the connection

    Returns:
        void - query is ran on the server

    '''
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    '''
    Executes a read query on the given server

    Parameters:
        connection (string): connection object connected to the server
        query (string): the query to execute via the connection

    Returns:
        void - query is ran on the server

    '''
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    '''
    Executes a list of values on the given server

    Parameters:
        connection (string): connection object connected to the server
        sql (string): the query to execute via the connection
        val (list of tuples): the list of values to send to the server 

    Returns:
        void - the list of queries is ran on the server

    '''
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

query = '''
    Enter query here.
    '''

connection = create_db_connection('server_name', 'database_name')
results = read_query(connection, query)

for result in results:
    print(result)