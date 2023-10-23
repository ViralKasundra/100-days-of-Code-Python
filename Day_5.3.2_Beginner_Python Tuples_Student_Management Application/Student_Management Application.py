# Student Management Application (Interactive) with Nested Tuples

# Initialize a list with some initial student records
students = [
    ("Alice", 18, 95),
    ("Bob", 19, 85),
    ("Charlie", 17, 92),
    ("David", 18, 88),
    ("Eve", 19, 90)
]

# Nested Tuple for Courses and Student Records
courses = [("Math", "Science", "History"), students]

# Function to add a student to the list
def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = int(input("Enter student's grade: "))
    student = (name, age, grade)
    students.append(student)
    print(f"Student '{name}' added successfully.")

# Function to access a student's name by index
def access_student_name(index):
    if 0 <= index < len(students):
        student = students[index]
        return student[0]
    else:
        return "Index out of range."

# Function to print all student records
def print_students():
    if not students:
        print("No student records available.")
    else:
        print("List of Students:")
        for index, student in enumerate(students):
            print(f"Index: {index}, Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")

# Function to sort students by grade
def sort_students_by_grade():
    sorted_students = sorted(students, key=lambda student: student[2], reverse=True)
    print("Students Sorted by Grade:")
    for index, student in enumerate(sorted_students):
        print(f"Index: {index}, Name: {student[0]}, Age: {student[1]}, Grade: {student[2]}")

# Function to display student statistics for a specific grade
def student_statistics(grade):
    count = sum(1 for student in students if student[2] == grade)
    print(f"Number of students with grade {grade}: {count}")

# Main application loop
while True:
    print("\nStudent Management Options:")
    print("1. Add a student")
    print("2. Access a student's name by index")
    print("3. Print all student records")
    print("4. Sort students by grade")
    print("5. Student statistics for a specific grade")
    print("6. View Courses")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        index = int(input("Enter the index of the student you want to access: "))
        student_name = access_student_name(index)
        print(f"Student's Name: {student_name}")
    elif choice == '3':
        print_students()
    elif choice == '4':
        sort_students_by_grade()
    elif choice == '5':
        grade = int(input("Enter the grade to view statistics: "))
        student_statistics(grade)
    elif choice == '6':
        print("Courses: ", courses[0])
        print("Students:")
        print_students()
    elif choice == '7':
        print("Exiting the Student Management Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7).")
