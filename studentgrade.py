subject1 = float(input("Enter marks for Data Mining: "))
subject2 = float(input("Enter marks for Oops: "))
subject3 = float(input("Enter marks for Software Engineering: "))
subject4 = float(input("Enter marks for Devops: "))
subject5 = float(input("Enter marks for SSW: "))

avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5


if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "Fail"

print(f"The grade is: {grade}")
