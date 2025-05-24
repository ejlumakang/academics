# A company SEES is in need of a payroll system that computes for the net pay of their employees.
# Where:
# - Gross pay = No. of days work per week times the rate per day of each employee.
# - 10% of the Gross pay is being deducted as their tax.
# - Rate per day is Php 347.00
# Display the employees Gross Pay, Deduction, and Net pay.

rate = 347.00

days = int(input("Days worked: "))

gross_pay = days * rate
tax_deduction = 0.1 * gross_pay

net_pay = gross_pay - tax_deduction

print(f"{gross_pay:.2f}")
print(f"{tax_deduction:.2f}")
print(f"{net_pay:.2f}")
