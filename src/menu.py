def display_menu():
    print("\n" + "=" * 45)
    print("        PERSONAL FINANCE MANAGER")
    print("=" * 45)

    print("\nMAIN MENU:")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Expense Report")
    print("4. Search Expense")
    print("5. Monthly Report")
    print("6. Backup Expenses")
    print("7. Exit")

    print("=" * 45)


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1-7): ").strip()

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return choice

        print("Invalid choice. Please enter 1 to 7.")