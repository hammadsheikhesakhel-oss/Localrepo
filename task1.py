name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)