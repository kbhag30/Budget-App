Budget App
A Python budget management application that tracks deposits, withdrawals, transfers, account balances, and spending by category. This project was completed as part of a Python certification course and demonstrates object-oriented programming, data structures, functions, and formatted output.
Features
	•	Create budget categories such as Food, Clothing, and Entertainment
	•	Record deposits with descriptions
	•	Record withdrawals and prevent spending beyond the available balance
	•	Calculate the current category balance
	•	Transfer funds between categories
	•	Display a formatted ledger for each category
	•	Generate a spending chart showing the percentage of total spending by category
Technologies Used
	•	Python
	•	Object-Oriented Programming (OOP)
	•	Lists and Dictionaries
	•	Functions
	•	List Comprehensions
	•	String Formatting
How It Works
The application uses a Category class to represent each budget category.
Each category contains:
	•	A category name
	•	A ledger containing deposits and withdrawals
Example
food = Category('Food')

food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant')

clothing = Category('Clothing')

food.transfer(50, clothing)
The ledger stores each transaction as a dictionary:
{
    'amount': 1000,
    'description': 'initial deposit'
}
Withdrawals are stored as negative amounts, allowing the balance to be calculated by adding all transactions together.
Spending Chart
The create_spend_chart() function calculates the total amount spent in each category and converts the amounts into percentages of total spending.
Example:
print(create_spend_chart([food, clothing]))
The function produces a vertical chart similar to:
Percentage spent by category
100|         
 90|         
 80|         
 70|         
 60|         
 50|    o    
 40|    o    
 30| o  o    
 20| o  o    
 10| o  o    
  0| o  o    
    ----------
     F  C
     o  l
     o  o
     d  t
        h
        i
        n
        g
Main Methods
deposit(amount, description='')
Adds money to the category's ledger.
withdraw(amount, description='')
Withdraws money if the category has sufficient funds.
Returns:
	•	True if the withdrawal is successful
	•	False if there are insufficient funds
get_balance()
Calculates and returns the current balance.
transfer(amount, category)
Transfers money from one category to another.
check_funds(amount)
Checks whether the category has enough money for a withdrawal or transfer.
__str__()
Returns a formatted representation of the category's ledger and current balance.
create_spend_chart(categories)
Creates a chart showing the percentage of total spending for each category.
Running the Project
	1	Make sure Python is installed.
	2	Clone or download the project.
	3	Open the project directory in your terminal or code editor.
	4	Run the Python file:
python budget_app.py
What I Learned
Through this project, I practiced:
	•	Creating and using Python classes
	•	Working with object attributes and methods
	•	Managing data using lists and dictionaries
	•	Using loops and conditional statements
	•	Writing reusable functions
	•	Using list comprehensions
	•	Formatting strings and numerical values
	•	Working with multiple objects and transferring data between them
	•	Building a text-based data visualization
Project Context
This project was completed as part of a Python certification course and was designed to demonstrate practical Python programming and object-oriented programming concepts.
