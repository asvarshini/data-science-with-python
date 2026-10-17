# REMOVE DUPLICATES FROM A LIST
# =============================

numbers = [4, 2, 4, 7, 2, 9, 7]


# METHOD 1: YOUR METHOD — FOR LOOP + LIST
# ---------------------------------------
new = []

for number in numbers:

    if number not in new:
        new.append(number)

print("Method 1:", new)


# METHOD 2: SET + LIST
# --------------------
new = list(set(numbers))

print("Method 2:", new)

# NOTE:
# This removes duplicates BUT does NOT guarantee
# the original order in general.


# METHOD 3: dict.fromkeys()
# -------------------------
new = list(dict.fromkeys(numbers))

print("Method 3:", new)

# This removes duplicates AND preserves order.


# METHOD 4: LIST COMPREHENSION
# ---------------------------
new = []

[new.append(number)
 for number in numbers
 if number not in new]

print("Method 4:", new)

# Works, but this is NOT recommended style.
# Normal for-loop is clearer.


# METHOD 5: FOR LOOP + SET
# ------------------------
new = []
seen = set()

for number in numbers:

    if number not in seen:
        new.append(number)
        seen.add(number)

print("Method 5:", new)

# Good when the list is large because checking
# membership in a set is generally faster.


# METHOD 6: FUNCTION
# ------------------
def remove_duplicates(numbers):

    new = []

    for number in numbers:

        if number not in new:
            new.append(number)

    return new


print("Method 6:", remove_duplicates(numbers))


# METHOD 7: FUNCTION + SET
# ------------------------
def remove_duplicates(numbers):

    new = []
    seen = set()

    for number in numbers:

        if number not in seen:
            new.append(number)
            seen.add(number)

    return new


print("Method 7:", remove_duplicates(numbers))


# METHOD 8: SET WITH SEEN VALUES
# ------------------------------
seen = set()

new = [
    number
    for number in numbers
    if not (number in seen or seen.add(number))
]

print("Method 8:", new)


# METHOD 9: PANDAS
# ----------------
import pandas as pd

new = pd.Series(numbers).drop_duplicates().tolist()
print("Method 9:", new)