# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
def computeGrade(score):
    try:
        score = float(score)
    except:
        return "Bad Score"
    if(score >= 0.0 and score <= 1.0):
            if(score >= .9):
                return ("A")
            elif(score >= 0.8):
                return ("B")
            elif(score >= 0.7):
                return ("C")
            elif(score >= 0.6):
                return ("D")
            else:
                return ("F")
    else:
        return ("Bad Score")

score = input("Enter Score: ")
print(computeGrade(score))
