import argparse
import json
import os
from datetime import datetime
import csv


DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(description, amount, category):
    data = load_data()
    expense_id = len(data) + 1
    expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount,
        "category": category
    }
    data.append(expense)
    save_data(data)
    print(f"Expense added successfully (ID: {expense_id})")

    # Check budget warning for current month
    current_month = datetime.now().month
    check_budget(current_month)


def list_expenses():
    data = load_data()
    if not data:
        print("No expenses found.")
        return
    
    print("ID  Date        Description       Amount   Category")
    for item in data:
        # print(f"{item['id']}   {item['date']}   {item['description']}   ${item['amount']}   {item['category']}")
        print(f"{item['id']}   {item['date']}   {item['description']}   ${item['amount']}   {item.get('category', 'N/A')}")


def delete_expense(expense_id):
    data = load_data()
    updated = [item for item in data if item["id"] != expense_id]

    if len(updated) == len(data):
        print("Error: Expense ID not found.")
        return
    
    save_data(updated)
    print("Expense deleted successfully")

def summary(month=None):
    data = load_data()

    # Total summary (no month provided)
    if month is None:
        total = sum(item["amount"] for item in data)
        print(f"Total expenses: ${total}")
        return

    # Validate month number
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
        return

    current_year = datetime.now().year

    filtered = [
        item for item in data
        if int(item["date"].split("-")[1]) == month
        and int(item["date"].split("-")[0]) == current_year
    ]

    total = sum(item["amount"] for item in filtered)

    # Convert month number to name (e.g., 8 → August)
    month_name = datetime(current_year, month, 1).strftime("%B")

    print(f"Total expenses for {month_name}: ${total}")


def update_expense(expense_id, description=None, amount=None):
    data = load_data()

    # Find the expense
    for item in data:
        if item["id"] == expense_id:
            if description:
                item["description"] = description
            if amount:
                item["amount"] = amount

            save_data(data)
            print("Expense updated successfully")
            return

    print("Error: Expense ID not found.")


def filter_by_category(category):
    data = load_data()
    filtered = [item for item in data if item.get("category") == category]

    if not filtered:
        print("No expenses found in this category.")
        return

    print("ID  Date        Description       Amount   Category")
    for item in filtered:
        print(f"{item['id']}   {item['date']}   {item['description']}   ${item['amount']}   {item['category']}")

def export_to_csv(filename="expenses.csv"):
    data = load_data()
    if not data:
        print("No expenses to export.")
        return

    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["id", "date", "description", "amount", "category"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow({
                "id": item["id"],
                "date": item["date"],
                "description": item["description"],
                "amount": item["amount"],
                "category": item.get("category", "N/A")
            })

    print(f"Expenses exported to {filename} successfully.")
       


BUDGET_FILE = "budgets.json"

def load_budgets():
    if not os.path.exists(BUDGET_FILE):
        return {}
    with open(BUDGET_FILE, "r") as f:
        return json.load(f)

def save_budgets(budgets):
    with open(BUDGET_FILE, "w") as f:
        json.dump(budgets, f, indent=4)

def set_budget(month, amount):
    if month < 1 or month > 12:
        print("Error: Month must be between 1 and 12.")
        return
    budgets = load_budgets()
    budgets[str(month)] = amount
    save_budgets(budgets)
    print(f"Budget set: {amount} for month {month}")

def check_budget(month):
    budgets = load_budgets()
    budget = budgets.get(str(month))
    if not budget:
        return  # No budget set for this month

    # Calculate total expenses for the month
    data = load_data()
    current_year = datetime.now().year
    total = sum(item["amount"] for item in data
                if int(item["date"].split("-")[0]) == current_year and int(item["date"].split("-")[1]) == month)

    if total > budget:
        print(f"⚠ Warning: You have exceeded your budget of ${budget} for this month! Total spent: ${total}")
     



def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")

    subcommands = parser.add_subparsers(dest="command")

    # add
    add_cmd = subcommands.add_parser("add")
    add_cmd.add_argument("--description", required=True)
    add_cmd.add_argument("--amount", type=float, required=True)
    add_cmd.add_argument("--category", required=True)

    # list
    subcommands.add_parser("list")
    category_cmd = subcommands.add_parser("filter-category")
    category_cmd.add_argument("--category", required=True)


    # delete
    delete_cmd = subcommands.add_parser("delete")
    delete_cmd.add_argument("--id", type=int, required=True)

    # summary
    summary_cmd = subcommands.add_parser("summary")
    summary_cmd.add_argument("--month", type=int)

    # update
    update_cmd = subcommands.add_parser("update")
    update_cmd.add_argument("--id", type=int, required=True)
    update_cmd.add_argument("--description")
    update_cmd.add_argument("--amount", type=float)


    # set-budget
    budget_cmd = subcommands.add_parser("set-budget")
    budget_cmd.add_argument("--month", type=int, required=True)
    budget_cmd.add_argument("--amount", type=float, required=True)


    export_cmd = subcommands.add_parser("export")
    export_cmd.add_argument("--file", default="expenses.csv")




    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount, args.category)


    elif args.command == "list":
        list_expenses()

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "summary":
        summary(args.month)

    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)

    elif args.command == "filter-category":
        filter_by_category(args.category)

    elif args.command == "set-budget":
        set_budget(args.month, args.amount)

    elif args.command == "export":
       export_to_csv(args.file)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
