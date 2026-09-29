def add_wellness_record(students, student_id, water, sleep, exercise, date, mood):
    for student in students:
        if student["id"] == student_id:

            if "wellness_records" not in student:
                student["wellness_records"] = []

            record = {
                "date": date,
                "water": water,
                "sleep": sleep,
                "exercise": exercise,
                "mood": mood
            }

            student["wellness_records"].append(record)
            return True

    return False

def get_wellness_records(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student.get("wellness_records", [])

    return []