# Rewrite your pay program using try and except so that your
# program handles non-numeric input gracefully by printing a message
# and exiting the program. The following shows two executions of the
# program:
try:
    hours = input("Enter Hours: ")
    hours = int(hours)
    rate = input("Enter Rate: ")
    rate = float(rate)
    gross = hours * rate
    print("Pay:", gross)
except:
    print("Error, please enter numeric input")
