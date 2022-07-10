# Encapsulate this code in a function named count, and gen-
# eralize it so that it accepts the string and the letter as arguments.
def count(string,letter):
    count = 0
    for value in string:
        if value == letter:
            count +=1
    print(count)

count("banana","a")
