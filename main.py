from src.expense import Expense
from src.file_manager import save_expenses, load_expenses
from src.reports import display_report
from src.utils import (
    get_valid_amount,
    get_valid_category,
    get_valid_date,
    get_valid_description
)

import os
import shutil


def show_menu():
    print("\n" + "=" * 45)
    print("        PERSONAL FINANCE MANAGER")
    print("=" * 45)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Expense Report")
    print("4. Search Expense")
    print("5. Monthly Report")
    print("6. Backup Expenses")
    print("7. Exit")
    print("=" * 45)


def search_expenses(expenses):
    keyword = input("Enter category or description: ").strip().lower()

    found = [
        expense for expense in expenses
        if keyword in expense.category.lower()
        or keyword in expense.description.lower()
    ]

    print("\nSEARCH RESULTS")
    print("-" * 40)

    if not found:
        print("No matching expenses found.")
    else:
        for expense in found:
            print(expense)


def monthly_report(expenses):
    month = input("Enter month (YYYY-MM): ").strip()

    found = [
        expense for expense in expenses
        if expense.date.startswith(month)
    ]

    print("\nMONTHLY REPORT")
    print("-" * 40)

    if not found:
        print("No expenses found for this month.")
        return

    total = sum(expense.amount for expense in found)

    print(f"Month: {month}")
    print(f"Total: ₹{total:.2f}")
    print(f"Number of expenses: {len(found)}")


def backup_expenses():
    source = "data/expenses.csv"
    backup = "data/expenses_backup.csv"

    if not os.path.exists(source):
        print("\nNo expense file found.")
        return

    try:
        shutil.copy2(source, backup)
        print("\nBackup created successfully!")
        print(f"Backup file: {backup}")

    except Exception as e:
        print("\nBackup failed.")
        print(f"Error: {e}")


def main():
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\nADD NEW EXPENSE")
            print("-" * 30)

            amount = get_valid_amount()
            category = get_valid_category()
            date = get_valid_date()
            description = get_valid_description()

            expense = Expense(
                amount,
                category,
                date,
                description
            )

            expenses.append(expense)
            save_expenses(expenses)

            print("\nExpense added successfully!")

        elif choice == "2":
            print("\nALL EXPENSES")
            print("-" * 40)

            if not expenses:
                print("No expenses found.")
            else:
                for expense in expenses:
                    print(expense)

        elif choice == "3":
            display_report(expenses)

        elif choice == "4":
            search_expenses(expenses)

        elif choice == "5":
            monthly_report(expenses)

        elif choice == "6":
            backup_expenses()

        elif choice == "7":
            print("\nThank you for using Personal Finance Manager!")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 7.")


if __name__ == "__main__":
    main()