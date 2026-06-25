class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        result = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            result += f"{desc}{amt}\n"
        result += f"Total: {self.get_balance():.2f}"
        return result


def create_spend_chart(categories):
    withdrawals = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = []
    for amount in withdrawals:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((amount / total_spent) * 100) // 10 * 10)

    chart = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for pct in percentages:
            if pct >= level:
                line += "o  "
            else:
                line += "   "
        chart.append(line)

    chart.append("    " + "-" * (len(categories) * 3 + 1))

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            if i < len(category.name):
                line += category.name[i] + "  "
            else:
                line += "   "
        chart.append(line)

    return "\n".join(chart)