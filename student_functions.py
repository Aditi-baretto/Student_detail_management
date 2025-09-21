from db_connection import create_connection

# ---------------- ADD STUDENT ----------------
def add_student(name, email, contact, dob, gender, student_class, address):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO students (name, email, contact_number, dob, gender, student_class, address)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (name, email, contact, dob, gender, student_class, address)
        cursor.execute(query, values)
        conn.commit()
        return "✅ Student added successfully!"
    except Exception as e:
        return f"❌ Error inserting student: {e}"
    finally:
        cursor.close()
        conn.close()

# ---------------- VIEW STUDENTS ----------------
def view_students():
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        return result
    except Exception as e:
        return f"❌ Error fetching students: {e}"
    finally:
        cursor.close()
        conn.close()

# ---------------- UPDATE STUDENT ----------------
def update_student(student_id, name, email, contact, dob, gender, student_class, address):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = """
            UPDATE students 
            SET name=%s, email=%s, contact_number=%s, dob=%s, gender=%s, student_class=%s, address=%s
            WHERE student_id=%s
        """
        values = (name, email, contact, dob, gender, student_class, address, student_id)
        cursor.execute(query, values)
        conn.commit()
        return "✅ Student updated successfully!"
    except Exception as e:
        return f"❌ Error updating student: {e}"
    finally:
        cursor.close()
        conn.close()

# ---------------- DELETE STUDENT ----------------
def delete_student(student_id):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        query = "DELETE FROM students WHERE student_id=%s"
        cursor.execute(query, (student_id,))
        conn.commit()
        return "🗑️ Student deleted successfully!"
    except Exception as e:
        return f"❌ Error deleting student: {e}"
    finally:
        cursor.close()
        conn.close()
