# FIND THE NUMBER CLOSEST TO TARGET
# =================================

numbers = [12, 27, 35, 41, 50]
target = 38


# METHOD 1: YOUR METHOD
# ---------------------
x = []

for i in numbers:
    x.append(abs(i - target))

u = x.index(min(x))

print("Method 1:", x, u, numbers[u])


# METHOD 2: LIST COMPREHENSION
# ----------------------------
x = [abs(i - target) for i in numbers]

u = x.index(min(x))

print("Method 2:", x, u, numbers[u])


# METHOD 3: min() + key
# ---------------------
answer = min(numbers, key=lambda x: abs(x - target))

print("Method 3:", answer)


# METHOD 4: FOR LOOP + MINIMUM DIFFERENCE
# ---------------------------------------
closest = numbers[0]
minimum_difference = abs(numbers[0] - target)

for number in numbers:
    difference = abs(number - target)

    if difference < minimum_difference:
        minimum_difference = difference
        closest = number

print("Method 4:", closest)


# METHOD 5: FOR LOOP + INDEX
# --------------------------
closest = numbers[0]
closest_index = 0

for i in range(len(numbers)):
    if abs(numbers[i] - target) < abs(closest - target):
        closest = numbers[i]
        closest_index = i

print("Method 5:", closest_index, closest)


# METHOD 6: WHILE LOOP
# --------------------
closest = numbers[0]
i = 1

while i < len(numbers):

    if abs(numbers[i] - target) < abs(closest - target):
        closest = numbers[i]

    i += 1

print("Method 6:", closest)


# METHOD 7: ENUMERATE()
# ---------------------
closest = numbers[0]
closest_index = 0

for i, number in enumerate(numbers):

    if abs(number - target) < abs(closest - target):
        closest = number
        closest_index = i

print("Method 7:", closest_index, closest)


# METHOD 8: SORTING
# -----------------
sorted_numbers = sorted(
    numbers,
    key=lambda x: abs(x - target)
)

closest = sorted_numbers[0]

print("Method 8:", closest)


# METHOD 9: FUNCTION
# ------------------
def find_closest(numbers, target):

    closest = numbers[0]

    for number in numbers:

        if abs(number - target) < abs(closest - target):
            closest = number

    return closest


print("Method 9:", find_closest(numbers, target))


# METHOD 10: FUNCTION + min()
# --------------------------
def find_closest(numbers, target):
    return min(numbers, key=lambda x: abs(x - target))


print("Method 10:", find_closest(numbers, target))


# METHOD 11: ZIP() + LIST COMPREHENSION
# ------------------------------------
differences = [abs(x - target) for x in numbers]

closest = numbers[differences.index(min(differences))]

print("Method 11:", closest)


# METHOD 12: NUMPY
# ----------------
import numpy as np

numbers_array = np.array(numbers)
closest = numbers_array[np.argmin(abs(numbers_array - target))]
print("Method 12:", closest)


# METHOD 13: PANDAS
# -----------------
import pandas as pd
s = pd.Series(numbers)
closest = s.loc[(s - target).abs().idxmin()]
print("Method 13:", closest)