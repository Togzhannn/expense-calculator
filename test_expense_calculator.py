import unittest
from expense_calculator import add_expense, total_by_category, total_all


class TestExpenseCalculator(unittest.TestCase):
    def test_add_expense(self):
        expenses = []
        result = add_expense(expenses, 100, "food")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["amount"], 100)

    def test_total_by_category(self):
        expenses = [
            {"amount": 100, "category": "food"},
            {"amount": 50, "category": "transport"},
            {"amount": 200, "category": "food"}
        ]
        self.assertEqual(total_by_category(expenses, "food"), 300)

    def test_total_all(self):
        expenses = [
            {"amount": 100, "category": "food"},
            {"amount": 50, "category": "transport"}
        ]
        self.assertEqual(total_all(expenses), 150)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            add_expense([], -10, "food")

    def test_boolean_amount_is_rejected(self):
        with self.assertRaises(ValueError):
            add_expense([], True, "food")


if __name__ == "__main__":
    unittest.main()