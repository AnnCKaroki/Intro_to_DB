# MySQLServer.py
import mysql.connector
from mysql.connector import errorcode

try:
    # Connect
    cnx = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Muralala18"
    )
    cursor = cnx.cursor()

    # Define the database name
    DB_NAME = 'alx_book_store'


    create_db_query = "CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME)
    cursor.execute(create_db_query)

    print(f"Database '{DB_NAME}' created successfully!")

except mysql.connector.Error as err:
    # Handle connection errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(f"Error: {err}")
finally:
    # Always close the cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'cnx' in locals() and cnx is not None and cnx.is_connected():
        cnx.close()
