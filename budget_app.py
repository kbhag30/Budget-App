class Category:
    # Create a new Category object with a name and an empty ledger
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Add a deposit to the ledger
    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    # Withdraw money if there are enough funds
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        return False
    
    # Calculate the current balance by adding all ledger amounts
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    # Transfer money from this category to another category
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    # Check whether the category has enough money for a withdrawal
    def check_funds(self, amount):
        return amount <= self.get_balance()

    # Create a formatted string showing the category and its ledger
    def __str__(self):
        output = f"{self.name:*^30}\n"

        for item in self.ledger:
            desc = item['description'][:23]
            amt = f"{item['amount']:.2f}"
            output += f"{desc:<23}{amt:>7}\n"
        output += f"Total: {self.get_balance():.2f}"
        return output


# Create a Food category
food = Category('Food')
# Add $1,000 to the Food category
food.deposit(1000, 'initial deposit')
# Withdraw money for groceries
food.withdraw(10.15, 'groceries')
# Withdraw money for a restaurant purchase
food.withdraw(15.89, 'restaurant and more food for dessert')
# Create a Clothing category
clothing = Category('Clothing')
# Transfer $50 from Food to Clothing
food.transfer(50, clothing)
# Print the Food category's ledger
print(food)


# Create a spending chart showing how much was spent in each category
def create_spend_chart(categories):
    # Keep track of the total amount spent across all categories
    total_spent = 0
    # Store the amount spent for each category
    spent = []

    # Go through each category
    for category in categories:
        # Add up only the negative ledger amounts (withdrawals)
        amount_spent = sum(
            item['amount']
            for item in category.ledger
            if item['amount'] < 0
        )
        # Convert the negative spending amount into a positive number
        amount_spent = abs(amount_spent)
        # Save the spending amount for this category
        spent.append(amount_spent)
        # Add the category's spending to the overall spending
        total_spent += amount_spent

    # Convert each category's spending into a percentage
    # Then round the percentage down to the nearest multiple of 10
    percentages = [
        int((amount / total_spent) * 100) // 10 * 10
        for amount in spent
    ]

    # Start the spending chart
    output = "Percentage spent by category\n"

    # Create chart rows from 100% down to 0%
    for percent in range(100, -1, -10):
        # Add the percentage number and vertical line
        output += f"{percent:>3}|"
        # Check each category's percentage
        for category_percent in percentages:
            # Add an 'o' if the category reaches this percentage level
            if category_percent >= percent:
                output += " o "
            # Otherwise leave the space blank
            else:
                output += "   "
        # Move to the next line
        output += " \n"
    # Add the horizontal line underneath the chart
    output += "    " + "---" * len(categories) + "-\n"

    # Find the length of the longest category name
    max_length = max(len(category.name) for category in categories)

    # Print category names vertically
    for i in range(max_length):
        # Add spacing before the category names
        output += "     "
        # Go through each category
        for category in categories:
            # Check whether this category has a character at this position
            if i < len(category.name):
                # Add the current character followed by spacing
                output += category.name[i] + "  "
            # Add spaces if the category name is shorter
            else:
                output += "   "
        # Move to the next line
        output += "\n"
    # Remove the final newline and return the completed chart
    return output.rstrip("\n")

print(create_spend_chart([food, clothing]))