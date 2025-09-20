import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Admin1234",   # your new root password
        database="student_management"
    )
    return conn
