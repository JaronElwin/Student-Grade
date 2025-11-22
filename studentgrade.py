import sys

if len(sys.argv) != 6:
    print("Usage: python studentgrade.py <mark1> <mark2> <mark3> <mark4> <mark5>")
    sys.exit(1)

try:
    subject1 = float(sys.argv[1])
    subject2 = float(sys.argv[2])
    subject3 = float(sys.argv[3])
    subject4 = float(sys.argv[4])
    subject5 = float(sys.argv[5])
except ValueError:
    print("Error: All inputs must be numbers.")
    sys.exit(1)

avg = (subject1 + subject2 + subject3 + subject4 + subject5) / 5

print(f"\nCalculated Average Marks: {avg:.2f}")

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

print(f"The final grade is: {grade}")
