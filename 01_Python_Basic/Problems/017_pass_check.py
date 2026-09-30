# ============================================================
# Problem:
# Check whether a password contains:
# - At least 8 characters
# - At least 1 number
# ============================================================

pas = input("Enter the password")


# ============================================================
# METHOD 1: for loop + isalpha() + isdigit()
# Best method for understanding the logic
# ============================================================

def check(pas):

    cha_count = 0
    num_count = 0

    for i in pas:

        if i.isalpha():
            cha_count += 1

        elif i.isdigit():
            num_count += 1

    if len(pas) >= 8 and num_count >= 1:
        print("Password is Valid ✌️")
    else:
        print("Password must contain at least 8 characters and 1 number")


check(pas)


# ============================================================
# METHOD 2: Count characters using sum()
# Shorter Python method
# ============================================================

def check(pas):

    num_count = sum(i.isdigit() for i in pas)

    if len(pas) >= 8 and num_count >= 1:
        print("Password is Valid ✌️")
    else:
        print("Password must contain at least 8 characters and 1 number")


check(pas)


# ============================================================
# METHOD 3: any()
# We only need to know whether at least one number exists
# ============================================================

def check(pas):

    if len(pas) >= 8 and any(i.isdigit() for i in pas):
        print("Password is Valid ✌️")
    else:
        print("Password must contain at least 8 characters and 1 number")


check(pas)


# ============================================================
# METHOD 4: all() + any()
# Check length and number
# ============================================================

def check(pas):

    if all([len(pas) >= 8, any(i.isdigit() for i in pas)]):
        print("Password is Valid ✌️")
    else:
        print("Password must contain at least 8 characters and 1 number")


check(pas)


# ============================================================
# METHOD 5: Regular Expression
# Useful when password rules become more complicated
# ============================================================

import re

def check(pas):

    if len(pas) >= 8 and re.search(r"\d", pas):
        print("Password is Valid ✌️")
    else:
        print("Password must contain at least 8 characters and 1 number")


check(pas)


# ============================================================
# METHOD 6: Function returning True / False
# Better design when validation is reused
# ============================================================

def check(pas):

    if len(pas) >= 8 and any(i.isdigit() for i in pas):
        return True

    return False


if check(pas):
    print("Password is Valid ✌️")
else:
    print("Password must contain at least 8 characters and 1 number")


# ============================================================
# METHOD 7: Check letters and numbers separately
# More complete password validation
# ============================================================

def check(pas):

    cha_count = 0
    num_count = 0

    for i in pas:

        if i.isalpha():
            cha_count += 1

        elif i.isdigit():
            num_count += 1

    if len(pas) >= 8 and cha_count >= 1 and num_count >= 1:
        print("Password is Valid ✌️")
    else:
        print("Password is Invalid")


check(pas)


# ============================================================
# METHOD 8: List comprehension
# ============================================================

def check(pas):

    numbers = [i for i in pas if i.isdigit()]

    if len(pas) >= 8 and len(numbers) >= 1:
        print("Password is Valid ✌️")
    else:
        print("Password is Invalid")


check(pas)


# ============================================================
# METHOD 9: while loop
# Same logic using while
# ============================================================

def check(pas):

    num_count = 0
    i = 0

    while i < len(pas):

        if pas[i].isdigit():
            num_count += 1

        i += 1

    if len(pas) >= 8 and num_count >= 1:
        print("Password is Valid ✌️")
    else:
        print("Password is Invalid")


check(pas)


# ============================================================
# TRACE
# ============================================================

# Suppose:

# pas = "python123"

# Length:
# 9

# Characters:

# p -> letter
# y -> letter
# t -> letter
# h -> letter
# o -> letter
# n -> letter
# 1 -> number
# 2 -> number
# 3 -> number

# len(pas) >= 8
# True

# number exists
# True

# Therefore:
# Password is Valid


