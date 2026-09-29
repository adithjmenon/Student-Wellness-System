def calculate_bmi(weight, height):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters * height_in_meters)
    return round(bmi, 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Healthy range"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity range"