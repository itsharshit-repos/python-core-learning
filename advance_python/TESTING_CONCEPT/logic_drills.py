# CODING TASK:
# Create this file: logic_drills.py (Use this file only for practice.)
# Use: if __name__ == "__main__": main()

# Question 1: Extract Names
# Create a list of students. Each student should have: name, age, marks
# Write a function: get_student_names. It should return only the names.
# Expected result: ["Aman", "Riya", "Kabir"]

# Question 2: Filter Passed Students
# A student passes if marks are greater than or equal to 40.
# Write a function: get_passed_students. It should return only the names of students who passed.
# Expected result: ["Aman", "Kabir"]

# Question 3: Count Failed Students
# Write a function: count_failed_students. It should return how many students failed.
# Expected result: 1

# Question 4: Find Student by Name
# Write a function: find_student. It should take one student name as input. If the student exists, return that student.
# If not, return None.
# Test mentally with: find_student("Riya"), find_student("Unknown")

# Question 5: Get Topper
# Write a function: get_topper_name. It should return the name of the student with highest marks.
# Expected result: "Kabir"

# Use exactly this data:
# Aman, age 18, marks 72
# Riya, age 19, marks 35
# Kabir, age 18, marks 91

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    marks: int

def student_info() -> list[Student]:
    return [
        Student(name="Aman", age=18, marks=72),
        Student(name="Riya", age=19, marks=35),
        Student(name="Kabir", age=18, marks=91)
    ]

def get_student_names() -> list[str]:
    students = student_info()
    name_list = []
    for student in students:
        name_list.append(student.name)
    return name_list

def get_passed_students() -> list[str]:
    students = student_info()
    passed_student = []
    for student in students:
        if student.marks >= 40 and student.marks <= 100:
            passed_student.append(student.name)
    return passed_student

def count_failed_students() -> int:
    students = student_info()
    failed_student = []
    for student in students:
        if student.marks >= 0 and student.marks < 40:
            failed_student.append(student.name)
    return len(failed_student)

def find_student(name: str) -> Student | None:
    students = student_info()
    for student in students:
        if student.name == name:
            return student
    return None
    
def get_topper_name() -> str:
    students = student_info()
    topper = students[0]
    for student in students:
        if student.marks > topper.marks:
            topper = student
    return topper.name

def main() -> None:
    print(get_student_names())
    print(get_passed_students())
    print(count_failed_students())
    print(find_student("Riya"))
    print(find_student("Unknown"))
    print(get_topper_name())

if __name__ == "__main__":
    main()