def calculate_grades (grades):
    total_grade = 0
    for value in grades.values():
        total_grade += value
    
    final_grade = total_grade / len(grades)
    return round(final_grade, 2)