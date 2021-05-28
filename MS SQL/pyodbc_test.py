import pyodbc
import pandas

# Framework to run queries on a SQL database in Python3


def create_database(connection, query):
    """Creates a database on the given connection.

    Args:
        connection (string): connection object connected to the server
        query (string): the query to execute via the connection
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except pyodbc.Error as err:
        print(f"Error: '{err}'")


def create_db_connection(server_name, database_name):
    """Creates a server connection to connect to a database.

    Returns:
        pyodbc.Connection: connection to the requested server
    """
    connection = None
    try:
        connection = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=" + server_name + ";"
            "Database=" + database_name + ";"
            "Trusted_Connection=yes;"
        )
        print("MS SQL Database connection successful")
    except pyodbc.Error as err:
        print(f"Error: '{err}'")

    return connection


def execute_query(connection, query):
    """Executes a query on the given server

    Args:
        connection (pyodbc.Connection): connection object connected to the server
        query (string): the query to execute via the connection
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except pyodbc.Error as err:
        print(f"Error: '{err}'")


def read_query(connection, query):
    """Executes a read query on the given server

    Args:
        connection (pyodbc.Connection): connection object connected to the server
        query (string): the query to execute via the connection

    Returns:
        list of tuples: the output of the query formatted as a list of tuples
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pyodbc.Error as err:
        print(f"Error: '{err}'")


def execute_list_query(connection, sql, val):
    """Executes a list of values on the given server

    Args:
        connection (string): connection object connected to the server
        sql (string): the query to execute via the connection
        val (list of tuples): the list of values to send to the server
    """
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except pyodbc.Error as err:
        print(f"Error: '{err}'")


def main():
    query = """
        UPDATE students 
        SET grade_level = 'Junior'
        WHERE BusinessEntityID = 1
        """

    connection = create_db_connection("ms01afossd01", "AdventureWorks2016")
    execute_query(connection, query)
    """
    For read_query:
    results = read_query(conneciton, query)
    for result in results:
        print(result)
    """


if __name__ == "__main__":
    main()
