# ============================================================
# Problem:
# Count the number of students who passed
# Passing mark = 40
# ============================================================

marks = [35, 72, 41, 29, 88, 56]


# ============================================================
# METHOD 1: sum() + generator expression
# Your method
# Short and Pythonic
# ============================================================

def pa(li):

    count = sum(1 for i in li if i >= 40)

    print("Total passed students :", count)


pa(marks)


# ============================================================
# METHOD 2: for loop + counter
# Best method for understanding the logic
# ============================================================

def pa(li):

    count = 0

    for i in li:

        if i >= 40:
            count += 1

    print("Total passed students :", count)


pa(marks)


# ============================================================
# METHOD 3: list comprehension + len()
# ============================================================

def pa(li):

    passed = [i for i in li if i >= 40]

    print("Total passed students :", len(passed))


pa(marks)


# ============================================================
# METHOD 4: filter() + len()
# ============================================================

def pa(li):

    passed = list(filter(lambda i: i >= 40, li))

    print("Total passed students :", len(passed))


pa(marks)


# ============================================================
# METHOD 5: filter() without converting to list
# Count using sum()
# ============================================================

def pa(li):

    count = sum(1 for i in filter(lambda x: x >= 40, li))

    print("Total passed students :", count)


pa(marks)


# ============================================================
# METHOD 6: while loop
# ============================================================

def pa(li):

    count = 0
    i = 0

    while i < len(li):

        if li[i] >= 40:
            count += 1

        i += 1

    print("Total passed students :", count)


pa(marks)


# ============================================================
# METHOD 7: Function returning the count
# Better when the result is needed elsewhere
# ============================================================

def pa(li):

    count = 0

    for i in li:

        if i >= 40:
            count += 1

    return count


result = pa(marks)

print("Total passed students :", result)


# ============================================================
# METHOD 8: Function + sum()
# ============================================================

def pa(li):

    return sum(i >= 40 for i in li)


print("Total passed students :", pa(marks))


# ============================================================
# METHOD 9: Count passed and failed students
# ============================================================

def pa(li):

    passed = 0
    failed = 0

    for i in li:

        if i >= 40:
            passed += 1
        else:
            failed += 1

    print("Total passed students :", passed)
    print("Total failed students :", failed)


pa(marks)


# ============================================================
# METHOD 10: Find the actual passed marks
# ============================================================

def pa(li):

    passed = []

    for i in li:

        if i >= 40:
            passed.append(i)

    print("Passed marks :", passed)
    print("Total passed students :", len(passed))


pa(marks)


# ============================================================
# METHOD 11: Find passed and failed marks
# ============================================================

def pa(li):

    passed = []
    failed = []

    for i in li:

        if i >= 40:
            passed.append(i)
        else:
            failed.append(i)

    print("Passed :", passed)
    print("Failed :", failed)


pa(marks)


# ============================================================
# METHOD 12: enumerate()
# Useful if we also want student number
# ============================================================

def pa(li):

    for i, mark in enumerate(li, start=1):

        if mark >= 40:
            print("Student", i, "passed with", mark)


pa(marks)


# ============================================================
# TRACE
# ============================================================

# marks = [35, 72, 41, 29, 88, 56]

# count = 0

# 35 >= 40 -> False
# count = 0

# 72 >= 40 -> True
# count = 1

# 41 >= 40 -> True
# count = 2

# 29 >= 40 -> False
# count = 2

# 88 >= 40 -> True
# count = 3

# 56 >= 40 -> True
# count = 4

# Final answer:
# 4


# ============================================================
# IMPORTANT PATTERNS
# ============================================================

# Count items satisfying a condition

count = 0

for i in li:

    if condition:
        count += 1


# Same idea using sum()

count = sum(1 for i in li if condition)


# Same idea using list comprehension

count = len([i for i in li if condition])


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

# First understand:

def pa(li):

    count = 0

    for i in li:

        if i >= 40:
            count += 1

    return count


# Then learn the shorter version:

def pa(li):

    return sum(1 for i in li if i >= 40)


marks = [35, 72, 41, 29, 88, 56]

print("Total passed students :", pa(marks))