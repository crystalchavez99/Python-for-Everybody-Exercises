# Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
extra = 0
if(int(hours)>40):
    overtime = float(rate) * 1.5
    extra = (int(hours) - 40) * overtime
gross = (40 * float(rate)) + extra
print("Pay:", gross)
