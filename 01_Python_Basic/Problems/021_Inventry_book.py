# ============================================================
# Problem:
# Check whether a target product is available in inventory
# ============================================================

inventory = {"pen": 40, "book": 12, "bag": 0}
target = "book"


# ============================================================
# METHOD 1: if + dictionary lookup
# Best and simplest method
# ============================================================

if target in inventory:
    if inventory[target] > 0:
        print(f"{target} is available")
        print(f"Quantity : {inventory[target]}")
    else:
        print(f"{target} is out of stock")
else:
    print("Product not found")


# ============================================================
# METHOD 2: get()
# Safe dictionary lookup
# ============================================================

quantity = inventory.get(target)

if quantity is not None:
    if quantity > 0:
        print(f"{target} is available")
        print(f"Quantity : {quantity}")
    else:
        print(f"{target} is out of stock")
else:
    print("Product not found")


# ============================================================
# METHOD 3: get() with default value
# Shorter method
# ============================================================

quantity = inventory.get(target, 0)

if target in inventory:
    if quantity > 0:
        print(f"{target} is available")
        print(f"Quantity : {quantity}")
    else:
        print(f"{target} is out of stock")
else:
    print("Product not found")


# ============================================================
# METHOD 4: Nested if
# Separate the two conditions clearly
# ============================================================

if target in inventory:

    if inventory[target] == 0:
        print(f"{target} is out of stock")
    else:
        print(f"{target} is available")
        print(f"Quantity : {inventory[target]}")

else:
    print("Product not found")


# ============================================================
# METHOD 5: for loop + items()
# Your approach, corrected
# ============================================================

found = False

for i, j in inventory.items():

    if i == target:

        found = True

        if j > 0:
            print(f"{target} is available")
            print(f"Quantity : {j}")
        else:
            print(f"{target} is out of stock")

        break

if not found:
    print("Product not found")


# ============================================================
# METHOD 6: for-else
# Good practice for understanding for-else
# ============================================================

for i, j in inventory.items():

    if i == target:

        if j > 0:
            print(f"{target} is available")
            print(f"Quantity : {j}")
        else:
            print(f"{target} is out of stock")

        break

else:
    print("Product not found")


# ============================================================
# METHOD 7: Function
# Useful when checking many products
# ============================================================

def check_inventory(inventory, target):

    if target not in inventory:
        return "Product not found"

    if inventory[target] == 0:
        return f"{target} is out of stock"

    return f"{target} is available, Quantity : {inventory[target]}"


print(check_inventory(inventory, target))


# ============================================================
# METHOD 8: Function + get()
# ============================================================

def check_inventory(inventory, target):

    quantity = inventory.get(target)

    if quantity is None:
        return "Product not found"

    if quantity == 0:
        return f"{target} is out of stock"

    return f"{target} is available, Quantity : {quantity}"


print(check_inventory(inventory, target))


# ============================================================
# METHOD 9: Ternary operator
# Only suitable when product definitely exists
# ============================================================

quantity = inventory[target]

print(
    f"{target} is available"
    if quantity > 0
    else f"{target} is out of stock"
)


# ============================================================
# METHOD 10: Check all available products
# Different version of the problem
# ============================================================

for i, j in inventory.items():

    if j > 0:
        print(f"{i} is available - Quantity : {j}")


# ============================================================
# TRACE
# ============================================================

# inventory = {
#     "pen": 40,
#     "book": 12,
#     "bag": 0
# }

# target = "book"

# First find:
#
# inventory["book"]
#
# 12
#
# Then:
#
# 12 > 0
#
# True
#
# Therefore:
#
# book is available
# Quantity : 12


# ============================================================
# TEST DIFFERENT CASES
# ============================================================

# Case 1: Available
target = "book"
# Quantity = 12


# Case 2: Out of stock
target = "bag"
# Quantity = 0


# Case 3: Product doesn't exist
target = "laptop"
# Product not found


# ============================================================
# IMPORTANT PATTERN
# ============================================================

# Step 1: Check whether key exists

if target in inventory:

    # Step 2: Get its value

    quantity = inventory[target]

    # Step 3: Check the value

    if quantity > 0:
        print("Available")
    else:
        print("Out of stock")

else:
    print("Product not found")


# ============================================================
# RECOMMENDED FOR DSA
# ============================================================

inventory = {"pen": 40, "book": 12, "bag": 0}
target = "book"

if target in inventory:
    if inventory[target] > 0:
        print(f"{target} is available")
        print(f"Quantity : {inventory[target]}")
    else:
        print(f"{target} is out of stock")
else:
    print("Product not found")