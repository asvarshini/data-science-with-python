# Question 7: Find the student with the highest marks

students = ["Asha", "Ravi", "Meena", "Arun"]
marks = [78, 91, 84, 88]


# ------------------------------------------------------------
# Method 1: max() + index()
# ------------------------------------------------------------

highest_marks = max(marks)
index = marks.index(highest_marks)

print(f"Name: {students[index]}")
print(f"Marks: {marks[index]}")


# ------------------------------------------------------------
# Method 2: for loop
# ------------------------------------------------------------

highest_marks = marks[0]
highest_student = students[0]

for i in range(len(marks)):
    if marks[i] > highest_marks:
        highest_marks = marks[i]
        highest_student = students[i]

print("Name:", highest_student)
print("Marks:", highest_marks)


# ------------------------------------------------------------
# Method 3: zip() + max()
# IMPORTANT: max(zip(students, marks)) sorts by student first.
# Use key=lambda x: x[1] to find the highest mark.
# ------------------------------------------------------------

student, highest_marks = max(zip(students, marks), key=lambda x: x[1])

print("Name:", student)
print("Marks:", highest_marks)


# ------------------------------------------------------------
# Method 4: enumerate() + max()
# ------------------------------------------------------------

index, highest_marks = max(enumerate(marks), key=lambda x: x[1])

print("Name:", students[index])
print("Marks:", highest_marks)
