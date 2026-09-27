# Question 4: Delivery charge based on weight

weight = int(input("Enter the weight: "))

# Method 1: if-else
if weight <= 5:
    charge = weight * 50
else:
    charge = weight * 50 + 100

print(f"Delivery charge: {charge}")


# Method 2: ternary operator
charge = weight * 50 if weight <= 5 else weight * 50 + 100
print(f"Delivery charge: {charge}")
