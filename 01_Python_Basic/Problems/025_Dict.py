# ============================================================
# Problem:
# Find the product(s) with the highest frequency
# ============================================================

products = ["pen", "book", "pen", "bag", "book", "pen", "pencil"]


# ============================================================
# METHOD 1: for loop + if-else
# Best method for learning
# ============================================================

new = {}

for i in products:
    if i not in new:
        new[i] = 1
    else:
        new[i] += 1

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# METHOD 2: dictionary get()
# Shorter and very useful
# ============================================================

new = {}

for i in products:
    new[i] = new.get(i, 0) + 1

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# METHOD 3: Counter
# Python's built-in frequency counting method
# ============================================================

from collections import Counter

new = Counter(products)

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# METHOD 4: Counter + most_common()
# Easiest when we only want ONE most frequent product
# ============================================================

from collections import Counter

new = Counter(products)

i, j = new.most_common(1)[0]

print("The key is :", i)
print("Then value is :", j)


# ============================================================
# METHOD 5: max() with dictionary
# Find the key having the maximum value
# ============================================================

new = {}

for i in products:
    new[i] = new.get(i, 0) + 1

i = max(new, key=new.get)

print("The key is :", i)
print("Then value is :", new[i])


# ============================================================
# METHOD 6: max() with items()
# ============================================================

new = {}

for i in products:
    new[i] = new.get(i, 0) + 1

i, j = max(new.items(), key=lambda x: x[1])

print("The key is :", i)
print("Then value is :", j)


# ============================================================
# METHOD 7: set() + count()
# Easy to understand, but slower for large data
# ============================================================

new = {}

for i in set(products):
    new[i] = products.count(i)

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# METHOD 8: dictionary comprehension
# Short, but not the best method for beginners
# ============================================================

new = {i: products.count(i) for i in set(products)}

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# METHOD 9: for loop + max() directly
# First find frequency, then find the product
# ============================================================

new = {}

for i in products:
    new[i] = new.get(i, 0) + 1

f = max(new.values())

answer = []

for i in new:
    if new[i] == f:
        answer.append(i)

print("The key is :", answer)
print("Then value is :", f)


# ============================================================
# METHOD 10: sorted()
# Sort products according to their frequency
# ============================================================

new = {}

for i in products:
    new[i] = new.get(i, 0) + 1

answer = sorted(new.items(), key=lambda x: x[1], reverse=True)

print("The key is :", answer[0][0])
print("Then value is :", answer[0][1])


# ============================================================
# METHOD 11: while loop
# Same logic using while
# ============================================================

new = {}

i = 0

while i < len(products):
    if products[i] not in new:
        new[products[i]] = 1
    else:
        new[products[i]] += 1
    i += 1

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# METHOD 12: reduce()
# Possible, but NOT recommended for this problem
# ============================================================

from functools import reduce

def count_product(new, product):
    new[product] = new.get(product, 0) + 1
    return new

new = reduce(count_product, products, {})

f = max(new.values())

for i, j in new.items():
    if j == f:
        print("The key is :", i)

print("Then value is :", f)


# ============================================================
# IMPORTANT PATTERNS TO REMEMBER
# ============================================================

# 1. Frequency counting

count = {}

for i in products:
    count[i] = count.get(i, 0) + 1


# 2. Find maximum frequency

f = max(count.values())


# 3. Find product with maximum frequency

i = max(count, key=count.get)


# 4. Find product AND frequency

i = max(count, key=count.get)
j = count[i]


# 5. Find ALL products having maximum frequency

f = max(count.values())

for i, j in count.items():
    if j == f:
        print(i, j)


# 6. Using Counter

from collections import Counter

count = Counter(products)


# 7. Most common product

i, j = count.most_common(1)[0]


# ============================================================
# OUTPUT
# ============================================================

# pen = 3
# book = 2
# bag = 1
# pencil = 1

# Highest frequency = 3
# Highest-frequency product = pen