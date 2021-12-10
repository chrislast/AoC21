# import our helpers
from utils import load, show, day, TRACE, Map, Path

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input

######## Part 1 ##########
# syntax checker scores
ERRVAL = {")": 3, "]": 57, "}": 1197, ">": 25137}

def trim(txt):
    """
    eliminate empty matching braces until they're all gone.
    - used for both parts
    """
    while True:
        edited = txt.replace("{}","").replace("[]","").replace("<>","").replace("()","")
        if edited == txt:
            return txt
        txt = edited

def p1(expect=399153, viz=None):
    scores = []
    for line in DATA:
        trimmed = trim(line)
        for char in trimmed:
            if char in ERRVAL:
                scores.append(ERRVAL[char])
                break
    return sum(scores)

######## Part 2 ##########
# line completer scores
COMPVAL = {")": 1, "]": 2, "}": 3, ">": 4}

def p2(expect=2995077699, viz=None):
    # calculate completer score for each incomplete line
    scores = []
    for line in DATA:
        txt = trim(line)
        # find and discard corrupted strings
        if any([char in txt for char in ERRVAL]):
            continue
        # reverse the string and make opens into closes
        txt = txt[::-1].replace("{","}").replace("[","]").replace("<",">").replace("(",")")
        # calculate the score
        acc = 0
        for char in txt:
            acc *= 5
            acc += COMPVAL[char]
        scores.append(acc)

    # return the middle score
    scores = sorted(scores)
    return scores[len(scores)//2]

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
