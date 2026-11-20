import json

FILENAME = "expenses.json"

#load json upon application initialization
def load_expenses(filename):
    try:
        #--load expenses list as json 
        with open(filename,"r") as file:
            expenses = json.load(file)

            if isinstance(expenses, list):
                return expenses
            else:
                raise ValueError("The file content should be a list")

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

#display menu and take user input
def display_menu():
    valid = False

    while not valid:
        #display menu options
        print (
        "========== PERSONAL EXPENSE TRACKER ========\n"
        "1. Add an expense\n"
        "2. View all expenses\n"
        "3. Calculate total expenditure\n"
        "4. Filter expenses by category\n"
        "5. View category summary\n"
        "6. Exit\n"
    )
        #capture user's choice
        choice = input("Choose an option :")
        #validate no empty space and no number less than 1 or above 6
        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Enter an option from the menu")
        else:
            valid = True

    #return user's choice
    return choice

    
# menu_choice = display_menu()
# print("You selected : ", menu_choice)

#input validation
#--amount input validation
def get_amount():
    valid = False
    while not valid:
        try:
            amount = float(input("Enter expense amount : "))
            if amount <=0:
                print("Enter a valid number greater than 0")
            else:
                valid = True
        except ValueError:
            print("Enter a valid number")
    
    return amount

#--category input validation
def get_category():
    valid = False
    while not valid:
        category = input("Enter an expense category : ")

        if not category.strip():
            print("Enter a valid category")
        else:
            valid = True
    return category.strip()

#--description input validation
def get_description():
    #loop to keep asking until valid value
    valid = False
    while not valid:
        description = input("Enter an expense description : ")
        if not description.strip():
            print("Enter a valid description")
        else:
            valid = True
    return description.strip()


#run application loop
def run_application():
    #keep application running
    menu_choice = ""

    while menu_choice != "6":
        menu_choice = display_menu()
        #if user selects 1
        if menu_choice == "1":
            category = get_category()
            description = get_description()
            amount = get_amount()
            add_expense(expenses,category,description,amount)
            #save new expense
            save_expenses(expenses, FILENAME)
        #if user selects 2
        elif menu_choice == "2":
            view_expenses(expenses)

        #if user selects 3
        elif menu_choice == "3":
            total_expenditure = calc_total_expenditure(expenses)
            print("Your total expenditure is : GHS ", total_expenditure)

        #if user selects 4
        elif menu_choice == "4":
            category = input("Enter category to filter : ")
            filtered_list = filter_by_category(expenses, category)
            if len(filtered_list) == 0:
                print("There are no expenses in this category")
            else :
                view_expenses(filtered_list)

        #if user selects 5
        elif menu_choice == "5":
            summary = category_summary(expenses)
            if len(summary) == 0:
                print("No expenses recorded yet")
            else:
                print("=====CATEGORY SPENDING SUMMARY=====")
                for category,total in summary.items():
                    print(f"{category} : {total}")

        #check if user selected 6
        elif menu_choice == "6":
            print("Goodbye")

run_application()

