# Question 3: Compare previous month and current month

previous_month = 420
current_month = 465

if current_month > previous_month:
    unit_increased = current_month - previous_month
    print(f"Current unit has increased by: {unit_increased}")
elif current_month < previous_month:
    unit_decreased = previous_month - current_month
    print(f"Current unit has decreased by: {unit_decreased}")
else:
    print("Current unit is the same as previous month")


# Shorter version
difference = current_month - previous_month

if difference > 0:
    print(f"Increased by: {difference}")
elif difference < 0:
    print(f"Decreased by: {-difference}")
else:
    print("No change")
