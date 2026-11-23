import math

MAX_AMOUNT = 1_000_000_000


def add_expense(expenses, amount, category):
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > MAX_AMOUNT:
        raise ValueError("Amount exceeds maximum")
    if math.isnan(amount):
        raise ValueError("Amount must be a number")
    if not category:
        raise ValueError("Category is required")

    expenses.append({
        "amount": amount,
        "category": category
    })
    return expenses


def total_by_category(expenses, category):
    return sum(
        expense["amount"]
        for expense in expenses
        if expense["category"] == category
    )


def total_all(expenses):
    return sum(expense["amount"] for expense in expenses)
