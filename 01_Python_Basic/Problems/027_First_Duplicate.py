# FIND FIRST DUPLICATE
# ====================

ids = [104, 205, 301, 205, 410]


# METHOD 1: YOUR METHOD — SET
# ---------------------------
new = set()

for i in ids:

    if i in new:
        print("Method 1:", i)
        break

    new.add(i)


# METHOD 2: FOR LOOP + LIST
# -------------------------
new = []

for i in ids:

    if i in new:
        print("Method 2:", i)
        break

    new.append(i)


# METHOD 3: ENUMERATE() + SET
# ---------------------------
seen = set()

for index, value in enumerate(ids):

    if value in seen:
        print("Method 3:", value)
        break

    seen.add(value)


# METHOD 4: FUNCTION + SET
# ------------------------
def find_first_duplicate(ids):

    seen = set()

    for value in ids:

        if value in seen:
            return value

        seen.add(value)

    return None


print("Method 4:", find_first_duplicate(ids))


# METHOD 5: FUNCTION + ENUMERATE()
# --------------------------------
def find_first_duplicate(ids):

    seen = set()

    for index, value in enumerate(ids):

        if value in seen:
            return value

        seen.add(value)

    return None


print("Method 5:", find_first_duplicate(ids))


# METHOD 6: COUNT()
# -----------------
duplicate = None

for value in ids:

    if ids.count(value) > 1:
        duplicate = value
        break

print("Method 6:", duplicate)


# METHOD 7: LIST COMPREHENSION
# ----------------------------
seen = set()

duplicates = [
    value
    for value in ids
    if value in seen or seen.add(value)
]

print("Method 7:", duplicates[0] if duplicates else None)


# METHOD 8: DICTIONARY COUNTING
# -----------------------------
counts = {}

first_duplicate = None

for value in ids:

    counts[value] = counts.get(value, 0) + 1

    if counts[value] == 2:
        first_duplicate = value
        break

print("Method 8:", first_duplicate)


# METHOD 9: PANDAS
# ----------------
import pandas as pd

s = pd.Series(ids)
duplicates = s[s.duplicated()]

if not duplicates.empty:
     print("Method 9:", duplicates.iloc[0])
else:
     print("Method 9:", None)