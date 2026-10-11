# ============================================================
# Problem:
# Student Lookup
# Find the marks of a student using their name
# Handle a name that is not present
# ============================================================

marks = {"Asha": 82, "Ravi": 91, "Meena": 76}
target = "Ravi"


# ============================================================
# METHOD 1: Direct dictionary lookup
# Best when we know the key exists
# ============================================================

print(marks[target])


# ============================================================
# METHOD 2: if-else
# Handle name not present
# ============================================================

if target in marks:
    print(f"{target}'s marks: {marks[target]}")
else:
    print("Student not found")


# ============================================================
# METHOD 3: get()
# Simple and safe dictionary lookup
# ============================================================

result = marks.get(target)

if result is not None:
    print(f"{target}'s marks: {result}")
else:
    print("Student not found")


# ============================================================
# METHOD 4: get() with default value
# Short method
# ============================================================

result = marks.get(target, "Student not found")

print(result)


# ============================================================
# METHOD 5: try-except
# Handle KeyError if key does not exist
# ============================================================

try:
    print(f"{target}'s marks: {marks[target]}")
except KeyError:
    print("Student not found")


# ============================================================
# METHOD 6: Function
# Useful when we want to reuse the lookup
# ============================================================

def find_marks(marks, target):

    if target in marks:
        return marks[target]
    else:
        return "Student not found"


print(f"{target}'s marks: {find_marks(marks, target)}")


# ============================================================
# METHOD 7: Function + get()
# Short reusable version
# ============================================================

def find_marks(marks, target):
    return marks.get(target, "Student not found")


print(f"{target}'s marks: {find_marks(marks, target)}")


# ============================================================
# METHOD 8: for loop
# Possible, but unnecessary for a dictionary lookup
# ============================================================

result = None

for i in marks:
    if i == target:
        result = marks[i]
        break

if result is not None:
    print(f"{target}'s marks: {result}")
else:
    print("Student not found")


# ============================================================
# METHOD 9: for loop + items()
# Also works, but dictionary lookup is better
# ============================================================

for name, mark in marks.items():
    if name == target:
        print(f"{target}'s marks: {mark}")
        break
else:
    print("Student not found")


# ============================================================
# METHOD 10: Change target to test missing student
# ============================================================

target = "Kiran"

if target in marks:
    print(f"{target}'s marks: {marks[target]}")
else:
    print("Student not found")


# ============================================================
# TRACE
# ============================================================

# marks = {
#     "Asha": 82,
#     "Ravi": 91,
#     "Meena": 76
# }

# target = "Ravi"

# marks[target]
#
# marks["Ravi"]
#
# 91


# ============================================================
# IMPORTANT DICTIONARY PATTERNS
# ============================================================

# Direct lookup

mark = marks[target]


# Safe lookup

mark = marks.get(target)


# Safe lookup with message

mark = marks.get(target, "Student not found")


# Check whether key exists

if target in marks:
    print(marks[target])


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

# If the key definitely exists:

print(marks[target])


# If the key may not exist:

if target in marks:
    print(f"{target}'s marks: {marks[target]}")
else:
    print("Student not found")


# Or simply:

print(marks.get(target, "Student not found"))