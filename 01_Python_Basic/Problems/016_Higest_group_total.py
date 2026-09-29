# ============================================================
# Problem:
# Find the group with the highest total marks
# ============================================================

marks = [[12, 15, 18], [10, 20, 25], [14, 17, 19]]


# ============================================================
# METHOD 1: for loop + sum() + max()
# Your approach corrected
# Best method to understand the logic
# ============================================================

new = []

for i in marks:
    new.append(sum(i))

highest = max(new)
index = new.index(highest)

print("Group", index + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# METHOD 2: Track highest total directly
# Best DSA method
# ============================================================

highest = 0
group = 0

for i in range(len(marks)):

    total = sum(marks[i])

    if total > highest:
        highest = total
        group = i

print("Group", group + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# METHOD 3: enumerate()
# Cleaner when we need the index
# ============================================================

highest = 0
group = 0

for i, row in enumerate(marks):

    total = sum(row)

    if total > highest:
        highest = total
        group = i

print("Group", group + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# METHOD 4: list comprehension + max()
# Short Python method
# ============================================================

new = [sum(i) for i in marks]

highest = max(new)
group = new.index(highest)

print("Group", group + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# METHOD 5: max() with key
# Find the group directly
# ============================================================

group = max(marks, key=sum)

print("Group", marks.index(group) + 1, "has the highest total.")
print("Total:", sum(group))


# ============================================================
# METHOD 6: max() with enumerate()
# Find index and total together
# ============================================================

group, highest = max(
    enumerate(marks),
    key=lambda x: sum(x[1])
)

print("Group", group + 1, "has the highest total.")
print("Total:", highest if False else sum(marks[group]))


# ============================================================
# METHOD 7: sorted()
# Sort groups according to their total
# ============================================================

new = sorted(
    enumerate(marks),
    key=lambda x: sum(x[1]),
    reverse=True
)

group = new[0][0]

print("Group", group + 1, "has the highest total.")
print("Total:", sum(marks[group]))


# ============================================================
# METHOD 8: while loop
# ============================================================

highest = 0
group = 0
i = 0

while i < len(marks):

    total = sum(marks[i])

    if total > highest:
        highest = total
        group = i

    i += 1

print("Group", group + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# METHOD 9: Function
# Useful when we want to reuse the logic
# ============================================================

def highest_group(marks):

    highest = 0
    group = 0

    for i, row in enumerate(marks):

        total = sum(row)

        if total > highest:
            highest = total
            group = i

    return group, highest


group, highest = highest_group(marks)

print("Group", group + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# METHOD 10: Function + max()
# ============================================================

def highest_group(marks):

    group = max(marks, key=sum)

    return marks.index(group) + 1, sum(group)


group, highest = highest_group(marks)

print("Group", group, "has the highest total.")
print("Total:", highest)


# ============================================================
# TRACE
# ============================================================

# Group 1:
# [12, 15, 18]
# 12 + 15 + 18 = 45

# Group 2:
# [10, 20, 25]
# 10 + 20 + 25 = 55

# Group 3:
# [14, 17, 19]
# 14 + 17 + 19 = 50

# Totals:
# [45, 55, 50]

# Maximum:
# 55

# Index:
# 1

# Group number:
# 1 + 1 = 2


# ============================================================
# IMPORTANT PATTERN
# ============================================================

# Nested list:
#
# marks = [
#     [12, 15, 18],
#     [10, 20, 25],
#     [14, 17, 19]
# ]

# Each inner list is one group.

# sum(i)
# gives the total of one group.


# ============================================================
# YOUR CODE CORRECTED
# ============================================================

marks = [[12, 15, 18], [10, 20, 25], [14, 17, 19]]

new = []

for i in marks:
    new.append(sum(i))

highest = max(new)
group = new.index(highest)

print("Group", group + 1, "has the highest total.")
print("Total:", highest)


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

highest = 0
group = 0

for i, row in enumerate(marks):

    total = sum(row)

    if total > highest:
        highest = total
        group = i

print("Group", group + 1, "has the highest total.")
print("Total:", highest)