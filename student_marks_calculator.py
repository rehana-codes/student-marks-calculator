# Student Marks Calculator

name = input("Enter your name: ")

subjects = ["PPS", "Physics", "BEE", "Maths", "EG"]
marks = []

for subject in subjects:
    mark = int(input("Enter " + subject + " marks: "))
    marks.append(mark)

total = sum(marks)
percentage = (total / 500) * 100

print("\n--- STUDENT REPORT CARD ---")
print("Name:", name)

for i in range(len(subjects)):
    print(subjects[i] + ":", marks[i])

print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if all(mark >= 35 for mark in marks):
    print("Result: PASS")
else:
    print("Result: FAIL")
