number = input("Enter a number: ")
numList = list()
while (number != "done"):
    numList.append(float(number))
    number = input("Enter a number: ")
print("Maximum:",max(numList))
print("Minimum:",min(numList))
