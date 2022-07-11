filename = input("Enter the file name: ")
fhand = open(filename)
spam = 0
count = 0
for line in fhand:
    phrase = line.startswith("X-DSPAM-Confidence:")
    if(phrase):
        index = line.find(":")
        numString = line[index + 1:]
        number = float(numString)
        spam+=number
        count+=1
print("Average spam confidence:",spam/count)
