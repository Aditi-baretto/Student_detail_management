from db_connection import create_connection

def add_student(name, email, contact, dob, gender, student_class, address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, contact_number, dob, gender, class, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (name, email, contact, dob, gender, student_class, address)
    )
    conn.commit()
    cursor.close()
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
