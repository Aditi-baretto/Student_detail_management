import streamlit as st
from student_functions import add_student, view_students

st.title("🎓 Student Management System")

menu = ["Add Student", "View Students"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add a New Student")
    name = st.text_input("Name")
    email = st.text_input("Email")
    contact = st.text_input("Contact Number")
    dob = st.date_input("Date of Birth")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    student_class = st.text_input("Class")
    address = st.text_area("Address")

    if st.button("Add Student"):
        add_student(name, email, contact, str(dob), gender, student_class, address)
        st.success(f"Student {name} added successfully!")

elif choice == "View Students":
    st.subheader("Student Records")
    students = view_students()
    st.dataframe(students)

