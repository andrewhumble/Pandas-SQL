import sqlalchemy as db
from sqlalchemy.sql.schema import MetaData
import urllib


def create_db_connection(server_name, database_name):
    """Creates a database connection.

    Args:
        server_name (string): the name of the server
        database_name (stirng): the name of the database

    Returns:
        engine: engine object
        connection: connection object
    """
    params = urllib.parse.quote_plus(
        "Driver={SQL Server};"
        "SERVER=" + server_name + ";"
        "DATABASE=" + database_name + ";"
        "Trusted_Connection=yes;"
    )
    engine = db.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    conn = engine.connect()
    return engine, conn


def main():
    engine, conn = create_db_connection("ms01afossd01", "AdventureWorks2016")
    meta = MetaData()
    meta.reflect(engine, schema='dbo')
    students = meta.tables['dbo.students']
    query = students.update().where(students.c.id == 1).values(grade_level = "Test2")
    conn.execute(query)


if __name__ == "__main__":
    main()


"""
UPDATE Example
--------------
meta.reflect(engine, schema='dbo')
students = meta.tables['dbo.students']
query = students.update().where(students.c.id == 1).values(grade_level = "Junior")
conn.execute(query)
"""

"""
INSERT Example
--------------
meta.reflect(engine, schema='dbo')
students = meta.tables['dbo.students']
ins = students.insert().values(id = 1, name = 'Andrew', lastname = 'Humble')
results = conn.execute(ins)
"""

"""
SELECT Example
--------------
meta.reflect(engine, schema='Person')
person = meta.tables['Person.Person']
email_address = meta.tables['Person.EmailAddress']
query = db.select(
                [person.columns.FirstName, person.columns.LastName, email_address.columns.EmailAddress]
            ).where(
                db.and_(person.columns.BusinessEntityID == email_address.columns.BusinessEntityID,
                     person.columns.FirstName == 'Andrew')
            )

results = conn.execute(query)

for result in results:
    print(result)
"""
