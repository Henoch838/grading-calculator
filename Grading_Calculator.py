def get_grades(prompt=""):
    grades = []
    while True:
        grade = int(input(prompt))
        if grade < 0:
            break
        grades.append(grade)
    return grades

def compute_avg_points(grades, removed_lowest_n=0):
    if not grades:
        return 0.0
    grades.sort()
    if removed_lowest_n >= len(grades):
        return float(max(grades))
    else:
        for _ in range(removed_lowest_n):
            grades.pop(0)
        return sum(grades) / len(grades)

def get_normalized_points(grade_percent, allocation, capped=True):
    points = (grade_percent / 100) * allocation
    if capped:
        return min(points, allocation)
    else:
        return points

def get_grade_letter(grade_number):
    if grade_number >= 94:
        return 'A'
    elif 90 <= grade_number < 94:
        return 'A-'
    elif 87 <= grade_number < 90:
        return 'B+'
    elif 84 <= grade_number < 87:
        return 'B'
    elif 80 <= grade_number < 84:
        return 'B-'
    elif 77 <= grade_number < 80:
        return 'C+'
    elif 74 <= grade_number < 77:
        return 'C'
    elif 70 <= grade_number < 74:
        return 'C-'
    elif 67 <= grade_number < 70:
        return 'D+'
    elif 64 <= grade_number < 67:
        return 'D-'
    else:
        return 'F'

def cap_exam_grades(grades):
    return [min(grade, 100) for grade in grades]

if __name__ == '__main__':
    assignments = get_grades("Enter your assignment grades: ")
    labs = get_grades("Enter your lab grades: ")
    project = get_grades("Enter your project grades: ")
    exams = get_grades("Enter your exam grades: ")

    exams = cap_exam_grades(exams)

    assignment_points = compute_avg_points(assignments)
    lab_points = compute_avg_points(labs)
    project_points = compute_avg_points(project)
    exam_points = compute_avg_points(exams, removed_lowest_n=1)

    assignment_points = get_normalized_points(assignment_points, 5)
    lab_points = get_normalized_points(lab_points, 15)
    project_points = get_normalized_points(project_points, 10, capped=False)
    exam_points = get_normalized_points(exam_points, 75, capped=False)

    total_grade = assignment_points + lab_points + project_points + exam_points
    grade_letter = get_grade_letter(total_grade)

    print(f"Assignment points: {assignment_points:.2f} (Average: {assignment_points/5*100:.2f}%)")
    print(f"Lab points: {lab_points:.2f} (Average: {lab_points/15*100:.2f}%)")
    print(f"Project points: {project_points:.2f} (Average: {project_points/10*100:.2f}%)")
    print(f"Exam points: {exam_points:.2f} (Average: {exam_points/75*100:.2f}%)")
    print(f"Total Grade: {total_grade:.2f} Letter: {grade_letter}")
