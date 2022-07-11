# Sometimes when programmers get bored or want to have a
# bit of fun, they add a harmless Easter Egg to their program. Modify
# the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo
# boo”. The program should behave normally for all other files which
# exist and don’t exist.
filename = input("Enter the file name: ")
if(filename == "na na boo boo"):
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    exit()
try:
    fhand = open(filename)
    count = 0
    for line in fhand:
        count+=1
    print("There were",count,"subject lines in",filename)
except:
    print("File cannot be opened:",filename)
