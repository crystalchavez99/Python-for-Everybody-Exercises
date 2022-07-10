# Write a program which repeatedly reads numbers until the
# user enters “done”. Once “done” is entered, print out the total, count,
# and average of the numbers. If the user enters anything other than a
# number, detect their mistake using try and except and print an error
# message and skip to the next number.
ask = input("Enter a number: ")
total = 0
count = 0
while(ask != "done"):
    try:
        ask = int(ask)
        count+=1
        total+=ask
    except:
        print("Invalid input")
    ask = input("Enter a number: ")
print(total,count,(total/count))
