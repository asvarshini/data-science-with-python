# Question 1: Calculate item totals, total bill, and apply 10% discount if total >= 2000

prices = [600, 450, 800, 400]
quantities = [1, 2, 1, 1]

# Method 1: for loop + append
new = []
for i in range(len(prices)):
    new.append(prices[i] * quantities[i])

total = sum(new)
bill = total - total * 0.10 if total >= 2000 else total

print("Item totals:", new)
print("Total:", total)
print("Bill:", bill)


# Method 2: list comprehension
new = [price * quantity for price, quantity in zip(prices, quantities)]
total = sum(new)
bill = total * 0.90 if total >= 2000 else total

print("Item totals:", new)
print("Total:", total)
print("Bill:", bill)


# Method 3: calculate total directly with zip
total = sum(price * quantity for price, quantity in zip(prices, quantities))
bill = total * 0.90 if total >= 2000 else total

print("Total:", total)
print("Bill:", bill)
