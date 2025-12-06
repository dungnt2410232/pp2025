class Student:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__dob = ""

    def input(self):
        self.__id = input(" - ID: ")
        self.__name = input(" - Name: ")
        self.__dob = input(" - DoB: ")

    def list(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DoB: {self.__dob}")

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name

class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__marks = {}

    def input(self):
        self.__id = input(" - ID: ")
        self.__name = input(" - Name: ")

    def list(self):
        print(f"ID: {self.__id}, Name: {self.__name}")

    def input_marks(self, students):
        print(f"Inputting marks for course: {self.__name}")
        for s in students:
            mark = float(input(f"Mark for {s.get_name()} (ID {s.get_id()}): "))
            self.__marks[s.get_id()] = mark

    def show_marks(self):
        print(f"Marks for {self.__name}:")
        for sid, score in self.__marks.items():
            print(f"Student ID: {sid} - Mark: {score}")

    def get_id(self):
        return self.__id

students = []
courses = []

print("Input students")
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    print(f"Student {i+1}:")
    s = Student()
    s.input()
    students.append(s)

print("\nInput courses.")
num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
    print(f"Course {i+1}:")
    c = Course()
    c.input()
    courses.append(c)

print("\nSelect courses and marking")
print("\n--- Course List ---")
for c in courses:
    c.list()

selected_id = input("Enter Course ID: ")
found_course = None

for c in courses:
    if c.get_id() == selected_id:
        found_course = c
        break
        
if found_course:
    found_course.input_marks(students)
else:
    print("Course not found.")

print("\nListing")
print("--- Student List ---")
for s in students:
    s.list()

print("--- Course List ---")
for c in courses:
    c.list()

print("\nShow marks")
cid = input("Enter Course ID to view: ")
for c in courses:
    if c.get_id() == cid:
        c.show_marks()