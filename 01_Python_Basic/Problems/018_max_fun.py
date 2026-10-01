# ============================================================
# Problem:
# Find the maximum number in a list
# ============================================================


# ============================================================
# METHOD 1: Function + for loop
# Your method
# Best method for understanding the logic
# ============================================================

def m(li):

    l = li[0]

    for i in li:
        if i > l:
            l = i

    return l


li = [10, 25, 7, 40, 18]

print(m(li))


# ============================================================
# METHOD 2: Function + max()
# Shortest built-in method
# ============================================================

def m(li):
    return max(li)


li = [10, 25, 7, 40, 18]

print(m(li))


# ============================================================
# METHOD 3: while loop
# ============================================================

def m(li):

    l = li[0]
    i = 0

    while i < len(li):

        if li[i] > l:
            l = li[i]

        i += 1

    return l


li = [10, 25, 7, 40, 18]

print(m(li))


# ============================================================
# METHOD 4: sorted()
# Sort the list and take the last element
# ============================================================

def m(li):
    return sorted(li)[-1]


li = [10, 25, 7, 40, 18]

print(m(li))


# ============================================================
# METHOD 5: sort()
# Changes the original list
# ============================================================

def m(li):

    li.sort()

    return li[-1]


li = [10, 25, 7, 40, 18]

print(m(li))


# ============================================================
# METHOD 6: reduce()
# Possible, but not necessary for this problem
# ============================================================

from functools import reduce

def m(li):

    return reduce(
        lambda a, b: a if a > b else b,
        li
    )


li = [10, 25, 7, 40, 18]

print(m(li))


# ============================================================
# METHOD 7: input() with space-separated numbers
# Correct way to take a list of integers from the user
# ============================================================

li = list(map(int, input("Enter numbers: ").split()))

print(max(li))


# Example input:
# 10 25 7 40 18
#
# Output:
# 40


# ============================================================
# METHOD 8: User input + your own function
# ============================================================

def m(li):

    l = li[0]

    for i in li:
        if i > l:
            l = i

    return l


li = list(map(int, input("Enter numbers: ").split()))

print(m(li))


# ============================================================
# METHOD 9: Input one number at a time
# ============================================================

li = []

n = int(input("How many numbers: "))

for i in range(n):

    value = int(input("Enter number: "))

    li.append(value)

print(max(li))


# ============================================================
# METHOD 10: enumerate()
# Useful when we also need the index
# ============================================================

li = [10, 25, 7, 40, 18]

l = li[0]
index = 0

for i, value in enumerate(li):

    if value > l:
        l = value
        index = i

print("Maximum :", l)
print("Index :", index)


# ============================================================
# METHOD 11: Find maximum without max()
# Simple direct solution
# ============================================================

li = [10, 25, 7, 40, 18]

l = li[0]

for i in li:

    if i > l:
        l = i

print(l)


# ============================================================
# TRACE
# ============================================================

# li = [10, 25, 7, 40, 18]

# Start:
# l = 10

# i = 10
# 10 > 10 -> False
# l = 10

# i = 25
# 25 > 10 -> True
# l = 25

# i = 7
# 7 > 25 -> False
# l = 25

# i = 40
# 40 > 25 -> True
# l = 40

# i = 18
# 18 > 40 -> False
# l = 40

# Final answer:
# 40


# ============================================================
# IMPORTANT INPUT CONCEPT
# ============================================================

# WRONG for numbers:

i = list(input("Enter the list"))

# If input is:
# 10 20 30
#
# Result:
# ['1', '0', ' ', '2', '0', ' ', '3', '0']


# Correct:

i = list(map(int, input("Enter numbers: ").split()))

# If input is:
# 10 20 30
#
# Result:
# [10, 20, 30]


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

# Understand this first:

def m(li):

    l = li[0]

    for i in li:
        if i > l:
            l = i

    return l


# Then know the Python shortcut:

print(max(li))