import streamlit as st
import pandas as pd
from student_functions import add_student, view_students, update_student, delete_student

# ------------------- STYLES -------------------
st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🎓 College Student Management System</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid #1E3A8A'>", unsafe_allow_html=True)
st.sidebar.markdown("<h2 style='color:#1E3A8A;'>📚 Menu</h2>", unsafe_allow_html=True)

# Sidebar menu
menu = ["Add Student", "View Students", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("", menu)

# ---------------- ADD STUDENT ----------------
if choice == "Add Student":
    st.subheader("➕ Add a New Student")
    name = st.text_input("Name", key="add_name")
    email = st.text_input("Email", key="add_email")
    contact = st.text_input("Contact Number", key="add_contact")
    dob = st.date_input("Date of Birth", key="add_dob")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="add_gender")
    student_class = st.text_input("Class", key="add_class")
    address = st.text_area("Address", key="add_address")

    if st.button("Add Student", key="add_button"):
        message = add_student(name, email, contact, str(dob), gender, student_class, address)
        st.success(message)

# ---------------- VIEW STUDENTS ----------------
elif choice == "View Students":
    st.subheader("📋 Student Records 🏫")
    students = view_students()
    if students:
        df = pd.DataFrame(students)
        df = df[['student_id','name','email','contact_number','dob','gender','student_class','address']]
        st.dataframe(df, use_container_width=True)
    else:
        st.warning("⚠️ No student records found!")

# ---------------- UPDATE STUDENT ----------------
elif choice == "Update Student":
    st.subheader("✏️ Update Student Details")
    students = view_students()
    if students:
        student_ids = [s['student_id'] for s in students]
        selected_id = st.selectbox("Select Student ID to Update", student_ids, key="update_select")
        selected_student = next(s for s in students if s['student_id'] == selected_id)

        name = st.text_input("Name", selected_student['name'], key="update_name")
        email = st.text_input("Email", selected_student['email'], key="update_email")
        contact = st.text_input("Contact Number", selected_student['contact_number'], key="update_contact")
        dob = st.date_input("Date of Birth", selected_student['dob'], key="update_dob")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], 
                              index=["Male","Female","Other"].index(selected_student['gender']), key="update_gender")
        student_class = st.text_input("Class", selected_student['student_class'], key="update_class")
        address = st.text_area("Address", selected_student['address'], key="update_address")

        if st.button("Update Student", key="update_button"):
            message = update_student(selected_student['student_id'], name, email, contact, str(dob), gender, student_class, address)
            st.success(message)
    else:
        st.warning("⚠️ No student records found!")

# ---------------- DELETE STUDENT ----------------
elif choice == "Delete Student":
    st.subheader("🗑️ Delete Student Record")
    students = view_students()
    if students:
        student_ids = [s['student_id'] for s in students]
        selected_id = st.selectbox("Select Student ID to Delete", student_ids, key="delete_select")
        selected_student = next(s for s in students if s['student_id'] == selected_id)

        st.write(f"Are you sure you want to delete **{selected_student['name']}**?")
        if st.button("Delete Student", key="delete_button"):
            message = delete_student(selected_id)
            st.success(message)
    else:
        st.warning("⚠️ No student records found!")
