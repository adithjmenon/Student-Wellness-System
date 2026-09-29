def student_id_exists(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return True

    return False

def add_student(students, student_id, name, age, height, weight):
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "height": height,
        "weight": weight,
        "wellness_records": []
    }

    students.append(student)

def display_students(students):
    if len(students) == 0:
        print("No students added yet.")

    else:
        for student in students:
            print("\nID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])

            if "height" in student:
                print("Height:", student["height"], "cm")
                print("Weight:", student["weight"], "kg")


def delete_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return True

    return False