import datetime

# Get the current date
current_date = datetime.date.today()

# Subtract five days
new_date = current_date - datetime.timedelta(days=5)

# Print the new date
print("Current date:", current_date)
print("New date (after subtracting five days):", new_date)
