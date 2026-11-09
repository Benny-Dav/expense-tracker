PERSONAL EXPENSE TRACKER
-add an expense
-view all expenses
-calc total expenditure
-vilter by category
-category summary(total by category)
-data persistence, save expenses to json 
-input validation

data structure for a single expense:
dictionary. category:food, description:groceries, amount:" 120
this structure is suitable for storing the key value pairs, where the three parameters can be stored for a single expense. lookup for any value with dictionary is also quite fast, constant time.

data structure for muliple expenses:
list. 
A python list would be suitable for storing multiple expenses recorded per user, where the single expenses can be accessed by index in averagely constant time complexity. 
Example
---------
user1=[
{
    "category": "Food",
    "description": "Groceries",
    "amount": 150
},
{
    "category": "Skincare",
    "description": "Vanilla scented lotion",
    "amount": 180
},
{
    "category": "Health",
    "description": "Becoactin and Dewormer",
    "amount": 100
},

]