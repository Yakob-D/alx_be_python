income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
projected_savings = savings * 12 + int((savings * 12 * 0.05))
print("Your monthly savings are $" + str(savings))
print("Projected savings after one year, with interest, is: $" + str(annual_savings))
