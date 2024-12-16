import mysql.connector
from mysql.connector import Error

def connect_database():
    """ Connect to the MySQL database and return the connection object"""
    # DB connection parameters
    db_name = "library_management_db"
    user = "root"
    password = "Mp261Vk823!"
    host = "localhost"

    try:
        # Attempting to establish a connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        # Check if the connection is successful
        print("Connected to MySQL database successfully!")
        return conn
    
    except Error as e:
        # Handling any connection errors
        print(f"Error: {e}")
        return None