SUBJECT_COUNT = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def total_marks(student):
    """Return the sum of one student's subject marks."""
    total = 0
    for index in range(1, len(student)):
        total = total + student[index]
    return total


def average(student):
    """Return one student's average marks across all subjects."""
    return total_marks(student) / SUBJECT_COUNT


def count_students_above_class_average(student_list):
    """Return how many students have an average above the class average."""
    average_sum = 0
    for student in student_list:
        average_sum = average_sum + average(student)
    class_average_value = average_sum / len(student_list)

    above_average_count = 0
    for student in student_list:
        if average(student) > class_average_value:
            above_average_count = above_average_count + 1
    return above_average_count


print("REPORT")

for student in students:
    marks_total = total_marks(student)
    student_average = average(student)
    if student_average >= 90:
        grade = "A"
    elif student_average >= 80:
        grade = "B"
    elif student_average >= 70:
        grade = "C"
    elif student_average >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{student[0]} {marks_total} {student_average}{grade}")

average_sum = 0
for student in students:
    student_average = average(student)
    average_sum = average_sum + student_average

print(f"Classaverage:{average_sum / len(students)}")

highest_average = 0
topper_name = ""
for student in students:
    student_average = average(student)
    if student_average > highest_average:
        highest_average = student_average
        topper_name = student[0]
print(f"Topper: {topper_name}{highest_average}")

above_average_count = count_students_above_class_average(students)
print(f"Students above class average: {above_average_count}")
