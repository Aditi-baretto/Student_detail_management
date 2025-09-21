import mysql.connector

def create_connection():
    """
    Create and return a connection to the MySQL database
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin1234",   # Your MySQL root password
        database="student_management"
    )
    return conn
