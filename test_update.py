from student_functions import update_student, view_students

# 1️⃣ Check current students
print("Before update:")
print(view_students())

# 2️⃣ Update one student (replace 1 with an actual student_id from Workbench)
result = update_student(
    1,                                  # student_id
    "Updated Name",                     # name
    "updated@email.com",                 # email
    "9876543210",                        # contact
    "2000-01-01",                        # dob
    "Female",                            # gender
    "10",                                # student_class
    "New Updated Address"                # address
)
print(result)

# 3️⃣ Check again
print("After update:")
print(view_students())
