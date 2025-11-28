https://roadmap.sh/projects/expense-tracker
Expense Tracker CLI

A simple and powerful Command Line Expense Tracker that helps you manage your personal finances.
You can add, update, delete, list, and summarize expenses.
It also supports categories, monthly budgets, and CSV export.

📁 Features

✔ Add expenses with description, amount, and category
✔ Update existing expenses
✔ Delete expenses by ID
✔ View all expenses
✔ Total expense summary
✔ Monthly expense summary (current year)
✔ Filter expenses by category
✔ Set monthly budgets + automatic warnings
✔ Export expenses to CSV
✔ Data stored locally using JSON files

🛠️ Tech Stack

Python 3

argparse for command-line parsing

JSON for local storage

CSV for export

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/expense-tracker-cli.git


Enter the project directory:

cd expense-tracker-cli


Run the program:

python expense_tracker.py --help

📌 Usage

Below are all supported commands.

➕ Add Expense
python expense_tracker.py add --description "Lunch" --amount 20 --category Food

✏️ Update Expense
python expense_tracker.py update --id 1 --description "Lunch at KFC" --amount 25

❌ Delete Expense
python expense_tracker.py delete --id 2

📄 List All Expenses
python expense_tracker.py list

📊 Total Summary
python expense_tracker.py summary

📅 Monthly Summary
python expense_tracker.py summary --month 11

🏷️ Filter by Category
python expense_tracker.py filter-category --category Food

💰 Set Monthly Budget
python expense_tracker.py set-budget --month 11 --amount 100


Budget warnings will automatically appear when adding expenses.

📤 Export Expenses to CSV
python expense_tracker.py export --file expenses.csv

📦 Project Structure
expense-tracker-cli/
│── expense_tracker.py
│── expenses.json
│── budgets.json
│── README.md

📝 Data Storage

Expenses are stored in expenses.json like:

{
  "id": 1,
  "date": "2024-11-26",
  "description": "Lunch",
  "amount": 20,
  "category": "Food"
}


Budgets are stored in budgets.json like:

{
  "11": 100
}

🤝 Contributing

Contributions are welcome!
You can:

Open issues

Suggest new features

Submit pull requests

⭐ Support

If you found this helpful, please star the repo ⭐ on GitHub to support the project!
