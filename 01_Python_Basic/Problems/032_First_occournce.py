# FIND FIRST OCCURRENCE
# =====================

numbers = [4, 7, 2, 7, 9, 7]
target = 7


# METHOD 1: index() — YOUR METHOD
# -------------------------------
if target in numbers:
    print("First occurrence:", numbers.index(target) + 1)
else:
    print("Not found")


# METHOD 2: FOR LOOP + ENUMERATE()
# --------------------------------
found = False

for i, number in enumerate(numbers):

    if number == target:
        print("First occurrence:", i + 1)
        found = True
        break

if not found:
    print("Not found")


# METHOD 3: FOR LOOP + RANGE()
# ----------------------------
found = False

for i in range(len(numbers)):

    if numbers[i] == target:
        print("First occurrence:", i + 1)
        found = True
        break

if not found:
    print("Not found")


# METHOD 4: WHILE LOOP
# --------------------
i = 0

while i < len(numbers):

    if numbers[i] == target:
        print("First occurrence:", i + 1)
        break

    i += 1

else:
    print("Not found")


# METHOD 5: index() + try/except
# ------------------------------
try:
    position = numbers.index(target)
    print("First occurrence:", position + 1)

except ValueError:
    print("Not found")


# METHOD 6: FUNCTION
# ------------------
def first_occurrence(numbers, target):

    if target in numbers:
        return numbers.index(target) + 1

    return None


position = first_occurrence(numbers, target)

if position:
    print("First occurrence:", position)
else:
    print("Not found")


# METHOD 7: FUNCTION + ENUMERATE()
# --------------------------------
def first_occurrence(numbers, target):

    for i, number in enumerate(numbers):

        if number == target:
            return i + 1

    return None


position = first_occurrence(numbers, target)

if position:
    print("First occurrence:", position)
else:
    print("Not found")


# METHOD 8: LIST COMPREHENSION
# ----------------------------
positions = [
    i + 1
    for i, number in enumerate(numbers)
    if number == target
]

if positions:
    print("First occurrence:", positions[0])
else:
    print("Not found")