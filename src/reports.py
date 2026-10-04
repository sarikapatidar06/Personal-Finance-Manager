from collections import defaultdict


def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense.amount

    return total


def calculate_average(expenses):
    if not expenses:
        return 0

    total = calculate_total(expenses)

    return total / len(expenses)


def category_wise_summary(expenses):
    summary = defaultdict(float)

    for expense in expenses:
        summary[expense.category] += expense.amount

    return dict(summary)


def display_report(expenses):
    if not expenses:
        print("\nNo expenses available.")
        return

    total = calculate_total(expenses)
    average = calculate_average(expenses)
    category_summary = category_wise_summary(expenses)

    print("\n" + "=" * 40)
    print("        EXPENSE REPORT")
    print("=" * 40)

    print(f"Total Expenses: ₹{total:.2f}")
    print(f"Average Expense: ₹{average:.2f}")

    print("\nCategory-wise Summary:")
    print("-" * 40)

    for category, amount in category_summary.items():
        print(f"{category}: ₹{amount:.2f}")

    print("=" * 40)