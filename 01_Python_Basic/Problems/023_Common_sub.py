# ============================================================
# Problem:
# Find common subjects between two students
# ============================================================

student1 = ["Math", "Python", "DBMS", "OS"]
student2 = ["Python", "OS", "Networks", "Math"]


# ============================================================
# METHOD 1: for loop + if
# Your method
# Best method to understand the logic
# ============================================================

new = []

for i in student1:
    if i in student2:
        new.append(i)

print(new)


# ============================================================
# METHOD 2: list comprehension
# Short Python version
# ============================================================

new = [i for i in student1 if i in student2]

print(new)


# ============================================================
# METHOD 3: set intersection
# Very useful for finding common elements
# ============================================================

new = list(set(student1) & set(student2))

print(new)


# ============================================================
# METHOD 4: set.intersection()
# Same as above, but using the method
# ============================================================

new = list(set(student1).intersection(set(student2)))

print(new)


# ============================================================
# METHOD 5: while loop
# Same logic using while
# ============================================================

new = []

i = 0

while i < len(student1):
    if student1[i] in student2:
        new.append(student1[i])
    i += 1

print(new)


# ============================================================
# METHOD 6: filter()
# Filters elements that are present in both lists
# ============================================================

new = list(filter(lambda x: x in student2, student1))

print(new)


# ============================================================
# METHOD 7: for loop + set
# Avoid checking repeatedly in student2
# Useful when lists are large
# ============================================================

new = []

student2_set = set(student2)

for i in student1:
    if i in student2_set:
        new.append(i)

print(new)


# ============================================================
# METHOD 8: Function
# Useful when we want to reuse the logic
# ============================================================

def common_subjects(student1, student2):

    new = []

    for i in student1:
        if i in student2:
            new.append(i)

    return new


print(common_subjects(student1, student2))


# ============================================================
# METHOD 9: Function + list comprehension
# Short reusable version
# ============================================================

def common_subjects(student1, student2):
    return [i for i in student1 if i in student2]


print(common_subjects(student1, student2))


# ============================================================
# METHOD 10: Set + function
# ============================================================

def common_subjects(student1, student2):
    return list(set(student1) & set(student2))


print(common_subjects(student1, student2))


# ============================================================
# TRACE
# ============================================================

# student1:
# Math
# Python
# DBMS
# OS

# Check each subject:

# Math   -> present in student2 -> add
# Python -> present in student2 -> add
# DBMS   -> not present         -> skip
# OS     -> present in student2 -> add

# Output:
# ['Math', 'Python', 'OS']


# ============================================================
# IMPORTANT PATTERNS
# ============================================================

# Common elements using loop

new = []

for i in student1:
    if i in student2:
        new.append(i)


# Common elements using list comprehension

new = [i for i in student1 if i in student2]


# Common elements using sets

new = list(set(student1) & set(student2))


# ============================================================
# IMPORTANT DIFFERENCE
# ============================================================

# List method:

new = [i for i in student1 if i in student2]

# Keeps the order of student1.

# Output:
# ['Math', 'Python', 'OS']


# Set method:

new = list(set(student1) & set(student2))

# Finds the common elements,
# but set does NOT guarantee the original list order.


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

# First learn:

new = []

for i in student1:
    if i in student2:
        new.append(i)


# Then learn:

new = [i for i in student1 if i in student2]


# Then learn:

new = list(set(student1) & set(student2))