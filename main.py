import pyodbc
from os import getenv
from dotenv import load_dotenv

# Import environmental variables from external file to hide credentials etc...
load_dotenv()
server = getenv('SERVER')
database = getenv('DATABASE')
username = getenv('DB_USER')
password = getenv('PASSWORD')
driver = getenv('DRIVER')

with pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=tcp:' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
