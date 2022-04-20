#Rewrite the grade program from the prev. chapter using a function called computegrade that takes a
#score as its parameter and returns a grade as a string
score = input('Enter score: ')

def computegrade(score):
    try: 
        score = float(score)
    except:
        return ('Bad score')
        quit()
    if score > 1.0:
        return ('Bad score')
        quit()
    if score >= 0.9:
        return ('A')
    elif score >= 0.8:
        return ('B')
    elif score >= 0.7:
        return ('C')
    elif score >= 0.6:
        return ('D')
    elif score < 0.6:
        return ('F')
        
print(computegrade(score))