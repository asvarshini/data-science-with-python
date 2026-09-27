# Question 5: Calculate fare
# First 5 km = 20
# Every km after 5 km = 5


# ------------------------------------------------------------
# Method 1: if-else
# ------------------------------------------------------------

distance = int(input("Enter the distance travelled: "))

fare = 20

if distance > 5:
    fare = fare + (distance - 5) * 5

print("Fare to be paid:", fare)


# ------------------------------------------------------------
# Method 2: for loop
# ------------------------------------------------------------

distance = int(input("Enter the distance travelled: "))

fare = 20

for km in range(6, distance + 1):
    fare += 5

print("Fare to be paid:", fare)


# ------------------------------------------------------------
# Method 3: while loop
# ------------------------------------------------------------

distance = int(input("Enter the distance travelled: "))

fare = 20
km = 6

while km <= distance:
    fare += 5
    km += 1

print("Fare to be paid:", fare)


# ------------------------------------------------------------
# Method 4: ternary operator
# ------------------------------------------------------------

distance = int(input("Enter the distance travelled: "))

fare = 20 if distance <= 5 else 20 + (distance - 5) * 5

print("Fare to be paid:", fare)


# ------------------------------------------------------------
# Method 5: function
# ------------------------------------------------------------

def calculate_fare(distance):
    if distance <= 5:
        return 20
    return 20 + (distance - 5) * 5


distance = int(input("Enter the distance travelled: "))
print("Fare to be paid:", calculate_fare(distance))
