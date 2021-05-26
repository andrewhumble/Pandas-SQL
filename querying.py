import pyodbc
from pyodbc import Error
import pandas

# Framework to run queries on a SQL database in Python3


def create_server_connection(driver, server, database, uid, password):
    '''
    Creates a server connection to connect to a database.

    Parameters
        driver (string): the driver name of the database
        server (string): the server name
        database (string): the database name
        uid (string): the user id
        password (string): the password

    Returns
        
    '''
    connection = None
    try:
        connection = pyodbc.connect(
            DRIVER=driver,
            SERVER=server,
            DATABASE=database,
            UID=uid,
            PASSWORD=password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


def create_db_connection(driver, server, database, uid, password):
    connection = None
    try:
        connection = pyodbc.connect(
            DRIVER=driver,
            SERVER=server,
            DATABASE=database,
            UID=uid,
            PASSWORD=password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

