from datetime import datetime
from database import load_students, save_students
from health_calculator import calculate_bmi, get_bmi_category
from student_manager import student_id_exists, add_student, display_students, delete_student
from wellness_tracker import add_wellness_record, get_wellness_records
from reports import display_wellness_report

students = load_students()

while True:
    print("\n--- Student Health System ---")
    print("1. Add student")
    print("2. View students")
    print("3. Calculate BMI")
    print("4. Add daily wellness record")
    print("5. View wellness report")
    print("6. Delete student")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter student ID: ")

        if student_id_exists(students, student_id):
            print("This student ID already exists. Please use a different ID.")
            continue

        name = input("Enter name: ")
        age = input("Enter age: ")

        try:
            height = float(input("Enter height in cm: "))
            weight = float(input("Enter weight in kg: "))
        except ValueError:
            print("Height and weight must be numbers.")
            continue

        add_student(students, student_id, name, age, height, weight)
        save_students(students)

        print("Student added and saved successfully.")

    elif choice == "2":
        display_students(students)

    elif choice == "3":
        student_id = input("Enter student ID: ")
        found = False

        for student in students:
            if student["id"] == student_id:
                found = True

                if "height" not in student or "weight" not in student:
                    print("This student does not have height and weight details.")
                    break

                bmi = calculate_bmi(student["weight"], student["height"])
                category = get_bmi_category(bmi)

                print("BMI is:", bmi)
                print("Category:", category)
                break

        if found == False:
            print("Student not found.")

    elif choice == "4":
        student_id = input("Enter student ID: ")

        try:
            water = float(input("Water intake in litres: "))
            sleep = float(input("Sleep hours: "))
            exercise = int(input("Exercise minutes: "))
        except ValueError:
            print("Please enter numbers for water, sleep, and exercise.")
            continue

        if water < 0 or sleep < 0 or sleep > 24 or exercise < 0:
            print("Please enter valid positive values.")
            continue

        date = input("Date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Incorrect date format. Use YYYY-MM-DD.")
            continue

        mood = input("Mood (low, okay, good, great): ").lower()

        if mood not in ["low", "okay", "good", "great"]:
            print("Please enter low, okay, good, or great.")
            continue

        if add_wellness_record(students, student_id, water, sleep, exercise, date, mood):
            save_students(students)
            print("Daily wellness record saved successfully.")
        else:
            print("Student not found.")

    elif choice == "5":
        student_id = input("Enter student ID: ")
        student_name = ""

        for student in students:
            if student["id"] == student_id:
                student_name = student["name"]
                break

        if student_name == "":
            print("Student not found.")
        else:
            records = get_wellness_records(students, student_id)
            display_wellness_report(student_name, records)

    elif choice == "6":
        student_id = input("Enter student ID to delete: ")

        if delete_student(students, student_id):
            save_students(students)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == "7":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")