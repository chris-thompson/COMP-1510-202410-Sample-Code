"""
Your employer pays time-and-a-half for any hours works above 40 in a single
week. This program accepts input for the number of hours worked, and calculates
the total wages for the week.

The program works like this:
    >> Enter the hourly rate: 12.50
    >> Enter the number of hours worked: 44
    >>
    >> Total wages: $575.00
"""


hourly_rate = float(input("Enter the hourly rate: "))
hours_worked = float(input("Enter the number of hours worked: "))

if hours_worked > 40:
    base_wages = 40.0 * hourly_rate
    overtime = (hours_worked - 40.0) * (1.5 * hourly_rate)
    wages = base_wages + overtime
else:
    wages = hours_worked * hourly_rate

print("\nTotal wages: $%.2f\n" % wages)
