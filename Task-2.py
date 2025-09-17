Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> import csv
>>> def add_expenses(desc,amount):
...     with open("expenses.csv","a",newline="") as f:
...         writer = csv.writer(f)
...         writer.writerow([desc, amount])
... 
...         
>>> def view_expenses():
...     with open("expenses.csv","r") as f:
...         for row in csv.reader(f):
...             print(f"Item : {row[0]}, Amount : Rs. {row[1]}")
... 
...             
>>> def total_expenses():
...     total = 0
...     with open("expenses.csv","r") as f:
...         for row in csv.reader(f):
...             total = total + int(row[1])
...     print("Total Expenses : Rs.",total)
... 
...     
>>> add_expenses("Coffee",250)
>>> add_expenses("Snacks",150)
>>> view_expenses()
Item : Coffee, Amount : Rs. 250
Item : Snacks, Amount : Rs. 150
>>> total_expenses()
Total Expenses : Rs. 400
>>> 
>>> add_expenses("House Rent",15000)
>>> add_expense("Internet",700)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    add_expense("Internet",700)
NameError: name 'add_expense' is not defined. Did you mean: 'add_expenses'?
>>> add_expenses("Internet",700)
>>> view_expenses()
Item : Coffee, Amount : Rs. 250
Item : Snacks, Amount : Rs. 150
Item : House Rent, Amount : Rs. 15000
Item : Internet, Amount : Rs. 700
>>> total_expenses()
Total Expenses : Rs. 16100
