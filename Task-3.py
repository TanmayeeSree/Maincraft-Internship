import csv
from datetime import datetime

# Add expense with category
def add_expense(desc, amount, category):
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount, category, datetime.now().strftime("%Y-%m-%d")])

# Display expenses
def display_expenses():
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            print(row)

# Search expenses by category
def search_category(category):
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if row[2] == category:
                print(row)

# Monthly total
def monthly_total(month):
    total = 0
    with open("expenses.csv", "r") as f:
        for row in csv.reader(f):
            if row[3].startswith(month):
                total += int(row[1])
    print(f"Monthly Total ({month}): ", total)

# Example usage
add_expense("Lunch", 20, "Food")
add_expense("Hotel",1200,"Food")
add_expense("Bus Ticket",60,"Travel")
search_category("Food")
monthly_total("2025-09")


