# Question 8: Temperature and Sales problems


# ============================================================
# PART A: Number of days warmer than average
# ============================================================

temperatures = [30, 32, 29, 35, 31, 34, 33]

average = sum(temperatures) / len(temperatures)

# Method 1: for loop
count = 0

for temp in temperatures:
    if temp > average:
        count += 1

print("Average temperature:", average)
print("Number of warmer days:", count)


# Method 2: list comprehension + len()
warmer_days = [temp for temp in temperatures if temp > average]

print("Average temperature:", average)
print("Number of warmer days:", len(warmer_days))


# Method 3: sum() with condition
count = sum(temp > average for temp in temperatures)

print("Average temperature:", average)
print("Number of warmer days:", count)


# Method 4: filter() + len()
warmer = list(filter(lambda temp: temp > average, temperatures))

print("Average temperature:", average)
print("Number of warmer days:", len(warmer))


# ============================================================
# PART B: Total sales, average, highest sale and day
# ============================================================

sales = [1200, 850, 2300, 1750, 900, 3100, 2800]


# Method 1: built-in functions
total_sales = sum(sales)
average = total_sales / len(sales)

highest_sale = max(sales)
index = sales.index(highest_sale)

print("Total sales:", total_sales)
print("Average:", average)
print("Highest sale:", highest_sale)
print("Highest sales day:", index + 1)


# Method 2: while loop without max()
m = sales[0]
i = 1

while i < len(sales):
    if sales[i] > m:
        m = sales[i]
    i += 1

print("Highest sale:", m)
print("Highest sales day:", sales.index(m) + 1)


# Method 3: for loop without max()
highest = sales[0]
highest_day = 0

for i in range(len(sales)):
    if sales[i] > highest:
        highest = sales[i]
        highest_day = i

print("Highest sale:", highest)
print("Highest sales day:", highest_day + 1)


# Method 4: enumerate()
highest = sales[0]
highest_day = 0

for day, sale in enumerate(sales):
    if sale > highest:
        highest = sale
        highest_day = day

print("Highest sale:", highest)
print("Highest sales day:", highest_day + 1)


# Method 5: max() with enumerate()
day, highest = max(enumerate(sales), key=lambda x: x[1])

print("Highest sale:", highest)
print("Highest sales day:", day + 1)
