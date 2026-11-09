from unicodedata import category


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

#function to add expense
#--should accept a list of expenses,
#--create expense dict,
#--add dict to user expense list, 
#--return updated user expense list

def add_expense(expenses,category,description,amount):
    #create and populate dict
    expense={}
    expense["category"]=category
    expense["description"]=description
    expense["amount"]=amount

    #add dict to expenses list
    expenses.append(expense)

    #return updated expenses list
    return expenses

#test function on user1 list
add_expense(user1, "Food", "Bag of water", 12)


#function to view all expenses
#--should accept expenses list and display every expense with all data

def view_expenses(expenses):
    print("---YOUR EXPENSES---")
    if len(expenses) ==0:
        print("You have no expenses recorded yet.")
    for e in expenses:
        print("-> Category : ", e["category"])
        print("-> Description : ", e["description"])
        print("-> Amount : ", e["amount"],"\n")

#test function 
view_expenses(user1)


#function to calc total expenditure
#--should accept expenses list
#--calc sum of all amounts
#--return total, or 0 for empty list

def calc_total_expenditure(expenses):
    total=0

    for e in expenses:
        amount = e["amount"]
        total +=amount

    return total

#filter expenses by category
#--accept expenses list
#--return a new list containing 
#--only expenses of given category
#--do not modify expenses list
#--if no expenses found, return empty list


def filter_by_category(expenses, category):
    filtered_list =[]
    for e in expenses:
        if e["category"] == category:
            filtered_list.append(e)
    return filtered_list

#test function
filter_by_category(user1,"Clothing")


#function for summary of expenses per category
#--accepts expense list
#--calc total amount spent in each category
#--return dict containing each category and total
#--return empty dict if no expenses

def category_summary(expenses):
    #create empty dict
    summary={}

    for e in expenses:
        category = e["category"]
        amount = e["amount"]

        if category not in summary:
            summary[category] = amount
            
        else:
            summary[category] +=amount
    
    return summary