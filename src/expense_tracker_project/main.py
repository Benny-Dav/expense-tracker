import json

FILENAME = "expenses.json"

#load json upon application initialization
def load_expenses(filename):
    try:
        #--load expenses list as json 
        with open(filename,"r") as file:
            expenses = json.load(file)
            return expenses

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: The expenses file contains invalid JSON")
        raise


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



#saving functionality to persist expenses
#--accept expenses list and filename
#--open file in write mode
#--save expenses as json

def save_expenses(expenses_list, filename):
    #--open file in write/ save list to json
    with open(filename,"w") as file:
        json.dump(expenses_list,file,indent=4)



#function to view all expenses
#--should accept expenses list and display every expense with all data

def view_expenses(expenses):
    print("---YOUR EXPENSES---")
    if len(expenses) == 0:
        print("You have no expenses recorded yet.")
    else:
        for e in expenses:
            print("-> Category : ", e["category"])
            print("-> Description : ", e["description"])
            print("-> Amount : ", e["amount"],"\n")



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

#----------------------------------------------------------------
#Application Initialization
#----------------------------------------------------------------

expenses = load_expenses(FILENAME)
view_expenses(expenses)

#test
# expenses = add_expense(expenses,"Food","Groceries",150)
# save_expenses(expenses,FILENAME)
# view_expenses(expenses)