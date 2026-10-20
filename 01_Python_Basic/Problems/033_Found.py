# FIND A STUDENT IN A LIST
# ========================

students = ["Asha", "Ravi", "Meena", "Arun"]
target = "Meena"


# METHOD 1: YOUR METHOD — in + index()
# ------------------------------------
if target in students:
    print(f"Student found at position: {students.index(target) + 1}")
else:
    print("Not found")


# METHOD 2: FOR LOOP + ENUMERATE()
# --------------------------------
found = False

for i, student in enumerate(students):

    if student == target:
        print(f"Student found at position: {i + 1}")
        found = True
        break

if not found:
    print("Not found")


# METHOD 3: FOR LOOP + RANGE()
# ----------------------------
found = False

for i in range(len(students)):

    if students[i] == target:
        print(f"Student found at position: {i + 1}")
        found = True
        break

if not found:
    print("Not found")


# METHOD 4: WHILE LOOP
# --------------------
i = 0

while i < len(students):

    if students[i] == target:
        print(f"Student found at position: {i + 1}")
        break

    i += 1

else:
    print("Not found")


# METHOD 5: index() WITH try/except
# ---------------------------------
try:
    position = students.index(target)
    print(f"Student found at position: {position + 1}")

except ValueError:
    print("Not found")


# METHOD 6: FUNCTION
# ------------------
def find_student(students, target):

    if target in students:
        return students.index(target) + 1

    return None


position = find_student(students, target)

if position:
    print(f"Student found at position: {position}")
else:
    print("Not found")


# METHOD 7: FUNCTION + FOR LOOP
# -----------------------------
def find_student(students, target):

    for i, student in enumerate(students):

        if student == target:
            return i + 1

    return None


position = find_student(students, target)

if position:
    print(f"Student found at position: {position}")
else:
    print("Not found")


# METHOD 8: COUNT() + index()
# ---------------------------
if students.count(target) > 0:
    print(f"Student found at position: {students.index(target) + 1}")
else:
    print("Not found")


# METHOD 9: LIST COMPREHENSION
# ----------------------------
positions = [
    i + 1
    for i, student in enumerate(students)
    if student == target
]

if positions:
    print(f"Student found at position: {positions[0]}")
else:
    print("Not found")