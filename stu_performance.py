def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "Fail"

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = int(input("Enter subject mark: "))
    marks.append(mark)

total = sum(marks)
average = calculate_average(marks)
grade = calculate_grade(average)

print("\nSTUDENT PERFORMANCE REPORT")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Grade:", grade)
