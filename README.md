# Personal Finance Manager

A simple Python-based Personal Finance Manager that helps users record, manage, search, and analyze their daily expenses.

## Features

- Add new expenses
- View all expenses
- Search expenses by category or description
- Generate total expense report
- Calculate average expense
- Category-wise expense summary
- Monthly expense report
- Backup expense data
- CSV file-based data storage
- Input validation
- Error handling
- Unit testing

## Technologies Used

- Python
- CSV
- Object-Oriented Programming (OOP)
- Unittest

## Project Structure

```text
Personal-Finance-Manager/
│
├── data/
│   ├── expenses.csv
│   └── expenses_backup.csv
│
├── docs/
│   └── user_guide.md
│
├── screenshots/
│
├── src/
│   ├── expense.py
│   ├── file_manager.py
│   ├── menu.py
│   ├── reports.py
│   └── utils.py
│
├── tests/
│   └── test_finance_manager.py
│
├── main.py
├── README.md
└── requirements.txt
## How to Run

Open the project folder in terminal and run:

python main.py

## Main Menu

1. Add New Expense
2. View All Expenses
3. View Expense Report
4. Search Expense
5. Monthly Report
6. Backup Expenses
7. Exit

## Expense Details

Each expense contains:

- Amount
- Category
- Date
- Description

## Data Storage

Expenses are stored in data/expenses.csv

Backup file:
data/expenses_backup.csv

## Reports

The application provides:

- Total expenses
- Average expense
- Category-wise summary
- Monthly expense report

## Testing

Unit tests are available in:

tests/test_finance_manager.py

Run tests using:

python -m unittest discover tests

All 4 tests currently pass successfully.

## Validation

The application validates:

- Expense amount
- Expense category
- Date format
- Description

Invalid input is rejected and the user is asked to enter valid information.

## Author

Sarika Patidar
