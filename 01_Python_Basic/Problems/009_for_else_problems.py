# Question 2: for-else practice

# ------------------------------------------------------------
# Problem 1: Pass/Fail
# ------------------------------------------------------------

marks = [55, 48, 62]
total = sum(marks)

for mark in marks:
    if mark < 40:
        print("FAIL")
        break
else:
    if total > 150:
        print("PASS")
    else:
        print("FAIL")


# ------------------------------------------------------------
# Problem 2: Find first number greater than 20
# ------------------------------------------------------------

numbers = [12, 7, 25, 18, 30]

for number in numbers:
    if number > 20:
        print("Found:", number)
        break
else:
    print("Not found")


# ------------------------------------------------------------
# Problem 3: Find Kiran
# ------------------------------------------------------------

names = ["Rahul", "Anu", "Kiran", "Priya"]

print("Kiran" in names)

for i in range(len(names)):
    if names[i] == "Kiran":
        print(f"Name found at index {i}: {names[i]}")
        break
else:
    print("Not found")


# Simpler method using index()
if "Kiran" in names:
    print("Kiran index:", names.index("Kiran"))
else:
    print("Not found")
