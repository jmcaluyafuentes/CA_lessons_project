print('How many hours you worked this week?')
hours_worked = int(input())
print('What is your base rate salary?')
base_rate_salary = int(input())

if hours_worked <= 40:
    gross_pay = hours_worked * base_rate_salary
else:
    hours_exceeds_40 = hours_worked - 40
    regular_pay = 40 * base_rate_salary
    overtime_pay = hours_exceeds_40 * base_rate_salary * 1.5
    gross_pay = regular_pay + overtime_pay
    
print(gross_pay)

print('good job')