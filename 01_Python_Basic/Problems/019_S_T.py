# ============================================================
# Problem:
# Convert strings to integers and find their sum
# ============================================================

numbers = ["10", "25", "7", "18"]


# ============================================================
# METHOD 1: list comprehension + int() + sum()
# Your method
# Short and Pythonic
# ============================================================

print(sum([int(x) for x in numbers]))


# ============================================================
# METHOD 2: generator expression + sum()
# Better because we don't need to create a list
# ============================================================

print(sum(int(x) for x in numbers))


# ============================================================
# METHOD 3: for loop
# Best method for understanding the logic
# ============================================================

total = 0

for x in numbers:

    total += int(x)

print(total)


# ============================================================
# METHOD 4: map() + sum()
# Very common Python method
# ============================================================

numbers = ["10", "25", "7", "18"]

total = sum(map(int, numbers))

print(total)


# ============================================================
# METHOD 5: list() + map()
# See the converted numbers
# ============================================================

new = list(map(int, numbers))

print(new)
print(sum(new))


# ============================================================
# METHOD 6: while loop
# ============================================================

total = 0
i = 0

while i < len(numbers):

    total += int(numbers[i])

    i += 1

print(total)


# ============================================================
# METHOD 7: function + for loop
# ============================================================

def total_numbers(numbers):

    total = 0

    for x in numbers:
        total += int(x)

    return total


print(total_numbers(numbers))


# ============================================================
# METHOD 8: function + map()
# ============================================================

def total_numbers(numbers):

    return sum(map(int, numbers))


print(total_numbers(numbers))


# ============================================================
# METHOD 9: reduce()
# Possible, but unnecessary here
# ============================================================

from functools import reduce

total = reduce(
    lambda a, b: a + int(b),
    numbers,
    0
)

print(total)


# ============================================================
# METHOD 10: Convert the whole list first
# ============================================================

numbers = ["10", "25", "7", "18"]

numbers = [int(x) for x in numbers]

print(sum(numbers))


# ============================================================
# TRACE
# ============================================================

# numbers = ["10", "25", "7", "18"]

# int("10") -> 10
# int("25") -> 25
# int("7")  -> 7
# int("18") -> 18

# New list:
# [10, 25, 7, 18]

# sum:
# 10 + 25 + 7 + 18
# = 60


# ============================================================
# IMPORTANT PATTERNS
# ============================================================

# String list -> integer list

new = [int(x) for x in numbers]


# String list -> integer list using map()

new = list(map(int, numbers))


# Integer list -> sum

total = sum(new)


# Do conversion and sum together

total = sum(int(x) for x in numbers)


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

# Understand this first:

total = 0

for x in numbers:
    total += int(x)

print(total)


# Then learn this:

print(sum(int(x) for x in numbers))


# And this very common Python pattern:

print(sum(map(int, numbers)))