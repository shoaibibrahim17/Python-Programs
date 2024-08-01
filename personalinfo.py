def display_personal_info():
    # Personal Information
    name = "Sk Ibrahim"
    full_address = "Brindavan Colony, Adilabad 504001"
    mobile_number = "8919574465"
    college_name = "Osmania University"
    course_subjects = ["Programming in Python", "Computer Networks", "DAA", "Automata Theory"]

    # Displaying the information
    print(f"Name: {name}")
    print(f"Full Address: {full_address}")
    print(f"Mobile Number: {mobile_number}")
    print(f"College Name: {college_name}")
    print("Course Subjects:")
    for subject in course_subjects:
        print(f"  - {subject}")

if __name__ == "__main__":
    display_personal_info()
