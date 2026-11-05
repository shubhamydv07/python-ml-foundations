expenses = []

while True:
    print('''===== Expense Tracker =====
1. Add Expense
2. View All Expenses
3. Total Spending
4. View by Category
5. Delete Expense
6. Exit''')
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 6:
        print("Thank you for using Expense Tracker!")
        break
    
    elif choice == 1:
        print("\n--- Add Expense ---")
        category = input("Enter category (Food/Travel/Shopping/Other): ")

        while True:
            try:
                amount = float(input("Enter amount: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        note  = input("Enter note (optional): ")
        expense = {
            "category" : category,
            "amount": amount,
            "note": note
        }

        expenses.append(expense)
        print(("Expense added successfully!"))

    elif choice == 2:
        if len(expenses) ==0:
            print("No expenses found.")
        else:
            print("\n--- All Expenses ---")

            for i in range (len(expenses)):
                print(f'{i+1}. Category : {expenses[i]["category"]}\nAmount : {expenses[i]["amount"]}\nnote : {expenses[i]["note"]}\n')

    elif choice == 3:
        if (len(expenses) == 0):
            print("No expenses found.")

        else:
            print("\n--- Total Spending ---")

            total_spendings = 0
            i=0
            while i < len(expenses):
                total_spendings +=expenses[i]['amount']
                i+=1
            print(f"Total Spending: ₹{total_spendings}")

    elif choice == 4:
        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\n--- View by Category ---")

            search_category = input("Enter category to search (food/Travel/Shopping/Other): ")
            found = False

            i = 0
            while i < len(expenses):
                if expenses[i]['category'].lower() == search_category.lower():
                    print(expenses[i])
                    found = True
                i+=1

            if found == False:
                print("No expenses found in this category!")

    elif choice == 5:
        if (len(expenses)==0):
            print("No expenses found.")

        else:
            print("\n--- Delete Expense ---")
            for i in range (len(expenses)):
                print(f'{i+1}. Category : {expenses[i]["category"]}\nAmount : {expenses[i]["amount"]}\nnote : {expenses[i]["note"]}\n')

            while True:
                 try:
                    number = int(input("Enter the number of the expense to delete: "))
                    break
                 except ValueError:
                     print("Invalid input! Please enter a number.")
                
            if number < 1 or number >len(expenses):
                    print("Invalid number !")
            else:
                    expenses.pop(number - 1)
                    print("Expense deleted successfully!")

    else:
        print("Invalid choice! Enter 1 to 6.")
