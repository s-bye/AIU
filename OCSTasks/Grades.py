def grade_statistics(grades):
    grade_counts = {}

    for grade in grades:
        if grade >= 90 and grade <= 100:
            grade_counts["A"] = grade_counts.get("A", 0) + 1
        elif grade >= 75 and grade <= 89:
            grade_counts["B"] = grade_counts.get("B", 0) + 1
        elif grade >= 60 and grade <= 74:
            grade_counts["C"] = grade_counts.get("C", 0) + 1
        elif grade >= 50 and grade <= 59:
            grade_counts["D"] = grade_counts.get("D", 0) + 1
        else:
            grade_counts["F"] = grade_counts.get("F", 0) + 1

        return grade_counts

def print_grade(grade_counts):
    total_grades = sum(grade_counts.values())

    for grade, count in grade_counts.items():
        percentage = count / total_grades * 100

        if count == 1:
            print(f"{grade}: {count} grade ({percentage:.2f}%)")
        else:
            print(f"{grade}: {count} grades ({percentage:.2f}%)")

num_grades = int(input("Enter the number of grades: "))
grades = []
for i in range(num_grades):
    grade = int(input(f"Enter grade {i + 1}: "))
    grades.append(grade)
grade_counts = grade_statistics(grades)
print_grade(grade_counts)