# ===========================================
# Title: wolff_hobbies.py
# Author: Patrick Wolff
# Date: 11 September 2022
# Description: Python program using conditionals, lists and loops
# ===========================================

# List of hobbies
hobbies = ["reading", "running", "gaming", "watching sports", "woodworking"]

# For loop to iterate over list
for item in hobbies:
    print(item)

print()

# List of days
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Loop to print days with message
for day in days:
    if day == "Sunday" or day == "Saturday":
        print(day + ": " + "It's your day off, enjoy one of your hobbies")
    else:
        print(day + ": " + "Work day")

