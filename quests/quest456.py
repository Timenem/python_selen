from __future__ import annotations


class User:
    """User system for bank accounts"""

    def __init__(self, name: str, balance: int, checking_account: bool) -> None:
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def __str__(self) -> str:
        return f"{self.name} has {self.balance}"

    def withdraw(self, amount: int) -> str:
        """withdraw an amount of money"""
        if amount > self.balance:
            raise ValueError("not enough balance")
        self.balance -= amount
        return f"{self}."

    def check(self, other: User, amount: int) -> str:
        """recieve money from another user"""
        if not other.checking_account:
            raise ValueError("can't write checks")
        other.withdraw(amount)
        self.add_cash(amount)
        return f"{self} and {other}."

    def add_cash(self, amount: int) -> str:
        """deposit an amount of money"""
        self.balance += amount
        return f"{self}."
