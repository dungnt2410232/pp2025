students = []
courses = []

def input_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        print(f"Student {i+1}:")
        sid = input(" - ID: ")
        name = input(" - Name: ")
        dob = input(" - DoB: ")
        students.append({'id': sid, 'name': name, 'dob': dob})

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        print(f"Course {i+1}:")
        cid = input(" - ID: ")
        name = input(" - Name: ")
        courses.append({'id': cid, 'name': name, 'marks': {}})

def input_marks():
    print("\nSelect a course ID from the list:")
    list_courses()
    selected_id = input("Enter Course ID: ")
    selected_course = None
    for c in courses:
        if c['id'] == selected_id:
            selected_course = c
            break
            
    if selected_course is not None:
        print(f"Inputting marks for course: {selected_course['name']}")
        for s in students:
            mark = float(input(f"Mark for {s['name']} (ID {s['id']}): "))
            selected_course['marks'][s['id']] = mark
    else:
        print("Course not found.")

def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def show_marks():
    print("\n--- Show Marks ---")
    cid = input("Enter Course ID to view: ")
    
    for c in courses:
        if c['id'] == cid:
            print(f"Marks for {c['name']}:")
            for student_id, score in c['marks'].items():
                print(f"Student ID: {student_id} - Mark: {score}")
            return 
            
    print("Course not found.")

if __name__ == "__main__":
    print("Input students")
    input_students()
    
    print("\nInput courses.")
    input_courses()
    
    print("\nSelect courses and marking")
    input_marks()
    
    print("\nListing")
    list_students()
    list_courses()
    
    print("\nShow marks")
    show_marks()