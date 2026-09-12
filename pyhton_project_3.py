student ={}

while True:

    print("welcome to the student data organizer!")

    print("select an option:")
    print("1. add student")
    print("2. view student")
    print("3. ubdate student")
    print("4. delete student")
    print("5. display subject offered")
    print("6. exit")

    choice = int(input("enter your choice: "))

    match choice:
        case 1:
            studentid = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subject = input("Subjects (comma-separated): ").split(",")

            student[studentid] = {
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subject": subject
            }

            print("\nStudent added successfully!\n")

        case 2:
            student_id = int(input("enter student id: "))
            found = False
            for sid, info in student.items():
                if sid == student_id:
                    print(f"Student ID: {sid}")
                    for key, value in info.items():
                        print(f"  {key}: {value}")
                    print()
                    found = True

            if not found:
                print("Student not found!\n")
        case 3:
            student_id = int(input("Enter student ID: "))

            if student_id in student:
                student[student_id]["name"] = input("Enter new name: ")
                student[student_id]["age"] = int(input("Enter new age: "))
                student[student_id]["grade"] = input("Enter new grade: ")
                student[student_id]["dob"] = input("Enter new date of birth: ")
                student[student_id]["subject"] = input("Enter new subjects: ").split(",")

                print("Student updated successfully!")

            else:
                print("Student not found!")

        case 4:
            student_id = int(input("enter student id to delete: "))

            if student_id in student:
                del student[student_id]
                print("student deleted successfully!")
            else:
                print("student not found!")

        case 5:
            print("science")
            print("maths")
            print("english")
            print("hindi")
            print("social science")
            print("ML")
            print("gujarati")
            print("general knowledge")

        case 6:
            print("exit program. ")
            break

        case _:
            print("invalid choice")