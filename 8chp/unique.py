# Write a program to open the file romeo.txt and read it line by line. For each
# line, split the line into a list of words using the split function. For
# each word, check to see if the word is already in the list of unique
# words. If the word is not in the list of unique words, add it to the list.
# When the program completes, sort and print the list of unique words
# in alphabetical order.

fhand = open("romeo.txt")
unique = list()
for line in fhand:
    x = line.split()
    for word in x:
        if(not word in unique):
            unique.append(word)
unique.sort()
print(unique)
