# Write the program to store the
# numbers the user enters in a list and use the max() and min() functions to
# compute the maximum and minimum numbers after the loop completes. end when the user enters “done”
number = input("Enter a number: ")
numList = list()
while (number != "done"):
    numList.append(float(number))
    number = input("Enter a number: ")
print("Maximum:",max(numList))
print("Minimum:",min(numList))
