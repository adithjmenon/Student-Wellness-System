def display_wellness_report(student_name, records):
    if len(records) == 0:
        print("No wellness records found.")
        return

    total_water = 0
    total_sleep = 0
    total_exercise = 0

    print("\n--- Wellness Report for", student_name, "---")

    for record in records:
        print(
            record["date"],
            "| Water:", record["water"], "L",
            "| Sleep:", record["sleep"], "hours",
            "| Exercise:", record["exercise"], "minutes",
            "| Mood:", record["mood"]
        )

        total_water = total_water + record["water"]
        total_sleep = total_sleep + record["sleep"]
        total_exercise = total_exercise + record["exercise"]

    number_of_records = len(records)

    print("\nAverage water intake:", round(total_water / number_of_records, 2), "L")
    print("Average sleep:", round(total_sleep / number_of_records, 2), "hours")
    print("Average exercise:", round(total_exercise / number_of_records, 2), "minutes")