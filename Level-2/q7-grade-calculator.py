# Level 2 Question 7:
# Calculate percentage and grade from 5 subject marks
marks = []
for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)
percentage = sum(marks) / 5
print(f"Percentage: {percentage:.1f}%")
if percentage >= 90:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
else:
    print("Grade: D")