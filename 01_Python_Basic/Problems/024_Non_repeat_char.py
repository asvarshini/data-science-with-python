# ============================================================
# Problem:
# Find the first non-repeating character
# ============================================================

text = "swiss"


# ============================================================
# METHOD 1: Dictionary + for loop
# Best method to understand the logic
# ============================================================

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

for i in text:
    if new[i] == 1:
        print("First non recurring element is :", i)
        break


# ============================================================
# METHOD 2: Dictionary + get()
# Same logic in a simple way
# ============================================================

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

for i in text:
    if new.get(i) == 1:
        print("First non recurring element is :", i)
        break


# ============================================================
# METHOD 3: Counter
# Python built-in frequency counting
# ============================================================

from collections import Counter

new = Counter(text)

for i in text:
    if new[i] == 1:
        print("First non recurring element is :", i)
        break


# ============================================================
# METHOD 4: set() + count()
# Easy to understand
# ============================================================

for i in text:
    if text.count(i) == 1:
        print("First non recurring element is :", i)
        break


# ============================================================
# METHOD 5: List comprehension
# Find all non-repeating characters
# ============================================================

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

answer = [i for i in text if new[i] == 1]

print("First non recurring element is :", answer[0])


# ============================================================
# METHOD 6: max / sorted approach
# Your approach - useful for finding lowest frequency,
# but we must preserve original order for "first"
# ============================================================

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

v = sorted(new.items(), key=lambda x: x[1])

for i in text:
    if new[i] == v[0][1]:
        print("First non recurring element is :", i)
        break


# ============================================================
# METHOD 7: while loop
# Same logic using while
# ============================================================

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

i = 0

while i < len(text):
    if new[text[i]] == 1:
        print("First non recurring element is :", text[i])
        break
    i += 1


# ============================================================
# METHOD 8: Using index()
# Check each character and its frequency
# ============================================================

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

answer = None

for i in new:
    if new[i] == 1:
        if answer is None or text.index(i) < text.index(answer):
            answer = i

print("First non recurring element is :", answer)


# ============================================================
# METHOD 9: Function
# Useful when we want to reuse the logic
# ============================================================

def first_non_repeating(text):

    new = {}

    for i in text:
        new[i] = new.get(i, 0) + 1

    for i in text:
        if new[i] == 1:
            return i

    return None


print("First non recurring element is :", first_non_repeating(text))


# ============================================================
# METHOD 10: Counter + function
# Short and clean
# ============================================================

from collections import Counter

def first_non_repeating(text):

    new = Counter(text)

    for i in text:
        if new[i] == 1:
            return i

    return None


print("First non recurring element is :", first_non_repeating(text))


# ============================================================
# TRACE
# ============================================================

# text = "swiss"

# s -> 2
# w -> 1
# i -> 1

# Frequency:
# s = 2
# w = 1
# i = 1

# Now check the original string:

# s -> frequency 2 -> skip
# w -> frequency 1 -> answer

# Output:
# First non recurring element is : w


# ============================================================
# IMPORTANT PATTERN
# ============================================================

# Step 1: Count frequency

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1


# Step 2: Go through ORIGINAL string

for i in text:
    if new[i] == 1:
        print(i)
        break


# ============================================================
# IMPORTANT DIFFERENCE
# ============================================================

# This:

v = sorted(new.items(), key=lambda x: x[1])

# sorts according to frequency.

# But "first non-repeating" means:
# We must respect the ORIGINAL ORDER of the string.

# Therefore this is safer:

for i in text:
    if new[i] == 1:
        print(i)
        break


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

# Learn this pattern very well:

new = {}

for i in text:
    new[i] = new.get(i, 0) + 1

for i in text:
    if new[i] == 1:
        print(i)
        break