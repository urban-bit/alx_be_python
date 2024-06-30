# finance_calculator.py

# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a fixed interest rate of 5%
annual_savings = monthly_savings * 12
projected_savings_with_interest = annual_savings + (annual_savings * 0.05)

# Display the user's monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.")

# Display the projected annual savings after including interest
print(f"Projected savings after one year, with interest, is: ${projected_savings_with_interest:.2f}.")
