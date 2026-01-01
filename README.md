Expense Tracker CLI

A simple yet powerful command-line expense tracker designed to help you manage your personal finances efficiently.
With this tool, you can track expenses, organize them by category, set monthly budgets, and generate summaries—all from your terminal.

✨ Features


➕ Add expenses with a description, amount, and category


✏️ Update existing expenses


❌ Delete expenses using a unique ID


📄 View a list of all recorded expenses


📊 View total expense summaries


📅 Generate monthly expense summaries for the current year


🏷️ Filter expenses by category


💰 Set monthly budgets with automatic budget warnings


📤 Export expenses to a CSV file


💾 Store all data locally using JSON files



🛠️ Tech Stack


Python 3


argparse – for command-line argument parsing


JSON – for local data storage


CSV – for exporting expense data



🚀 Installation


Clone the repository:


git clone https://github.com/YOUR_USERNAME/expense-tracker-cli.git



Navigate into the project directory:


cd expense-tracker-cli



View available commands:


python expense_tracker.py --help


📌 Usage
Below are the supported commands and examples.
➕ Add an Expense
python expense_tracker.py add --description "Lunch" --amount 20 --category Food

✏️ Update an Expense
python expense_tracker.py update --id 1 --description "Lunch at KFC" --amount 25

❌ Delete an Expense
python expense_tracker.py delete --id 2

📄 List All Expenses
python expense_tracker.py list

📊 Total Expense Summary
python expense_tracker.py summary

📅 Monthly Expense Summary
python expense_tracker.py summary --month 11

🏷️ Filter Expenses by Category
python expense_tracker.py filter-category --category Food

💰 Set a Monthly Budget
python expense_tracker.py set-budget --month 11 --amount 100


⚠️ Budget warnings will automatically appear when new expenses exceed the set monthly budget.

📤 Export Expenses to CSV
python expense_tracker.py export --file expenses.csv


📦 Project Structure
expense-tracker-cli/
│── expense_tracker.py
│── expenses.json
│── budgets.json
│── README.md


📝 Data Storage
Expenses (expenses.json)
{
  "id": 1,
  "date": "2024-11-26",
  "description": "Lunch",
  "amount": 20,
  "category": "Food"
}

Budgets (budgets.json)
{
  "11": 100
}


🤝 Contributing
Contributions are welcome! You can help by:


Opening issues


Suggesting new features


Submitting pull requests



⭐ Support
If you find this project useful, please consider giving it a ⭐ on GitHub.
Your support helps keep the project growing!
