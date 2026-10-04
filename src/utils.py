from datetime import datetime


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            return amount

        except ValueError:
            print("Invalid amount. Please enter a number.")


def get_valid_category():
    categories = [
        "Food",
        "Transport",
        "Entertainment",
        "Shopping",
        "Other"
    ]

    while True:
        category = input(
            "Enter category (Food/Transport/Entertainment/Shopping/Other): "
        ).strip()

        for valid_category in categories:
            if category.lower() == valid_category.lower():
                return valid_category

        print("Invalid category. Please choose from the given categories.")


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Please use YYYY-MM-DD format.")


def get_valid_description():
    while True:
        description = input("Enter description: ").strip()

        if description:
            return description

        print("Description cannot be empty.")