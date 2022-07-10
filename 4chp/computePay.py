# Rewrite your pay computation with time-and-a-half for over-
# time and create a function called computepay which takes two parameters
def computePay(hours,rate):
    extra = 0
    if(int(hours)>40):
        overtime = float(rate) * 1.5
        extra = (int(hours) - 40) * overtime
    gross = (40 * float(rate)) + extra
    print("Pay:", gross)

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
computePay(hours,rate)
