Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import csv
... import os
... from datetime import datetime
... 
... CSV_FILE = "expenses.csv"
... HEADERS = ["id", "date", "description", "amount", "category"]
... 
... def ensure_csv():
...     """Create expenses.csv with header row if missing"""
...     if not os.path.exists(CSV_FILE):
...         with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
...             csv_writer = csv.writer(f)
...             csv_writer.writerow(HEADERS)
... 
... def add_expense(desc, amount, category):
...     """Add a new expense row to CSV"""
...     try:
...         amt = float(amount)
...     except ValueError:
...         print("❌ Amount must be a number.")
...         return
...     
...     row = [
...         str(int(datetime.now().timestamp()) * 1000),  # unique id
...         datetime.now().strftime("%Y-%m-%d"),          # date
...         desc.strip(),
...         f"{amt:.2f}",
...         category.strip().title()
...     ]
...     
...     with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
...         csv_writer = csv.writer(f)
...         csv_writer.writerow(row)
...     print("✅ Expense added successfully.")
... 
... def view_all():
...     """Read and display all expenses"""
...     ensure_csv()
...     with open(CSV_FILE, "r", encoding="utf-8") as f:
...         rows = list(csv.reader(f))
...     
...     if len(rows) <= 1:
...         print("⚠️ No expenses found.")
...         return
...     
...     total = 0
...     for r in rows[1:]:
...         print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
...         total += float(r[3])
...     print(f"💰 Total spent: ${total:.2f}")
... 
... def search_category(cat):
...     """Filter expenses by category"""
...     ensure_csv()
...     with open(CSV_FILE, "r", encoding="utf-8") as f:
...         rows = list(csv.reader(f))[1:]
...     
...     results = [r for r in rows if r[4].lower() == cat.lower()]
...     if not results:
...         print(f"⚠️ No records found for category: '{cat}'")
...         return
...     
...     for r in results:
...         print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
... 
... def monthly_total(month):
...     """Calculate total spending for a given month (YYYY-MM)"""
...     ensure_csv()
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))[1:]
    
    filt = [r for r in rows if r[1].startswith(month)]
    if not filt:
        print(f"⚠️ No records for month: '{month}'")
        return
    
    total = sum(float(r[3]) for r in filt)
    print(f"💰 Monthly total for {month}: ${total:.2f}")

def delete_by_id(exp_id):
    """Remove expense by ID"""
    ensure_csv()
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if len(rows) <= 1:
        print("⚠️ No expenses to remove.")
        return
    
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(HEADERS)
        for r in rows[1:]:
            if r[0] != exp_id:
                csv_writer.writerow(r)
    print("✅ Expense deleted successfully.")

def run():
    """Main menu loop"""
    ensure_csv()
    while True:
        print("\n1) Add Expense\n2) View All\n3) Search by Category\n4) Monthly Total\n5) Delete by ID\n6) Exit")
        choice = input("Choose: ").strip()
        
        if choice == "1":
            add_expense(input("Description: "), input("Amount: "), input("Category: "))
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_category(input("Category: "))
        elif choice == "4":
            monthly_total(input("Month (YYYY-MM): "))
        elif choice == "5":
            delete_by_id(input("Expense ID: "))
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
