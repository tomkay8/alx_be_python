monthly_income = input('Enter your monthly income: ')
total_monthly_expenses = input('Enter your total monthly expenses: ')

monthly_savings = int(monthly_income) - int(total_monthly_expenses)

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print('Your monthly savings are $' + str(monthly_savings))
print('Projected savings after one year, with interest, is: $' + str(projected_savings))
