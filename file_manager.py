import csv
from src.expense import Expense


def save_expenses(expenses, filename="data/expenses.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Date", "Category", "Amount", "Description"])

        for expense in expenses:
            writer.writerow([
                expense.date,
                expense.category,
                expense.amount,
                expense.description
            ])


def load_expenses(filename="data/expenses.csv"):
    expenses = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expense = Expense(
                    row["Amount"],
                    row["Category"],
                    row["Date"],
                    row["Description"]
                )

                expenses.append(expense)

    except FileNotFoundError:
        print("No expense file found. Starting with empty data.")

    return expenses