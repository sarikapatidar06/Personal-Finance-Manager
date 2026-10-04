import unittest

from src.expense import Expense
from src.reports import (
    calculate_total,
    calculate_average,
    category_wise_summary
)


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense(100, "Food", "2026-10-01", "Lunch"),
            Expense(200, "Transport", "2026-10-02", "Auto"),
            Expense(300, "Food", "2026-10-03", "Dinner")
        ]

    def test_expense_creation(self):
        expense = Expense(
            500,
            "Shopping",
            "2026-10-04",
            "Clothes"
        )

        self.assertEqual(expense.amount, 500)
        self.assertEqual(expense.category, "Shopping")
        self.assertEqual(expense.date, "2026-10-04")
        self.assertEqual(expense.description, "Clothes")

    def test_calculate_total(self):
        total = calculate_total(self.expenses)
        self.assertEqual(total, 600)

    def test_calculate_average(self):
        average = calculate_average(self.expenses)
        self.assertEqual(average, 200)

    def test_category_wise_summary(self):
        summary = category_wise_summary(self.expenses)

        self.assertEqual(summary["Food"], 400)
        self.assertEqual(summary["Transport"], 200)


if __name__ == "__main__":
    unittest.main()