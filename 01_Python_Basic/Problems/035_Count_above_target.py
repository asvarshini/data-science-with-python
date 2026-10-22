# COUNT MARKS >= TARGET
# =====================

marks = [72, 45, 88, 39, 67, 91]
target = 60


# METHOD 1: FOR LOOP + COUNTER
count = 0

for mark in marks:
    if mark >= target:
        count += 1

print("Method 1:", count)


# METHOD 2: WHILE LOOP + COUNTER
count = 0
i = 0

while i < len(marks):
    if marks[i] >= target:
        count += 1
    i += 1

print("Method 2:", count)


# METHOD 3: FOR LOOP + RANGE
count = 0

for i in range(len(marks)):
    if marks[i] >= target:
        count += 1

print("Method 3:", count)


# METHOD 4: ENUMERATE()
count = 0

for i, mark in enumerate(marks):
    if mark >= target:
        count += 1

print("Method 4:", count)


# METHOD 5: LIST COMPREHENSION + LEN()
passed = [mark for mark in marks if mark >= target]

print("Method 5:", len(passed))


# METHOD 6: SUM() + GENERATOR
count = sum(mark >= target for mark in marks)

print("Method 6:", count)


# METHOD 7: SUM() + IF/ELSE
count = sum(1 if mark >= target else 0 for mark in marks)

print("Method 7:", count)


# METHOD 8: FILTER()
passed = list(filter(lambda mark: mark >= target, marks))

print("Method 8:", len(passed))


# METHOD 9: FILTER() + LEN()
count = len(list(filter(lambda mark: mark >= target, marks)))

print("Method 9:", count)


# METHOD 10: FUNCTION + FOR LOOP
def count_marks(marks, target):
    count = 0

    for mark in marks:
        if mark >= target:
            count += 1

    return count


print("Method 10:", count_marks(marks, target))


# METHOD 11: FUNCTION + SUM()
def count_marks(marks, target):
    return sum(mark >= target for mark in marks)


print("Method 11:", count_marks(marks, target))


# METHOD 12: RECURSION
def count_marks(marks, target, i=0):
    if i == len(marks):
        return 0

    if marks[i] >= target:
        return 1 + count_marks(marks, target, i + 1)

    return count_marks(marks, target, i + 1)


print("Method 12:", count_marks(marks, target))


# METHOD 13: NUMPY
import numpy as np
count = np.sum(np.array(marks) >= target)
print("Method 13:", count)


# METHOD 14: PANDAS
import pandas as pd
count = (pd.Series(marks) >= target).sum()
print("Method 14:", count)