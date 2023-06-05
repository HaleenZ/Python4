import datetime

# Current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Current year
current_year = current_datetime.year
print("Current year:", current_year)

# Month of year
month_of_year = current_datetime.strftime("%B")
print("Month of year:", month_of_year)

# Week number of the year
week_number = current_datetime.strftime("%W")
print("Week number of the year:", week_number)

# Weekday of the week
weekday = current_datetime.strftime("%A")
print("Weekday of the week:", weekday)

# Day of year
day_of_year = current_datetime.strftime("%j")
print("Day of year:", day_of_year)

# Day of the month
day_of_month = current_datetime.strftime("%d")
print("Day of the month:", day_of_month)

# Day of the week
day_of_week = current_datetime.strftime("%w")
print("Day of the week:", day_of_week)
