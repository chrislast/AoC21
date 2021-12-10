# import our helpers
from utils import load, show, day

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()
# syntax checker scores
ERRVAL = {")": 3, "]": 57, "}": 1197, ">": 25137}
# line completer scores
COMPVAL = {")": 1, "]": 2, "}": 3, ">": 4}

def trim(txt):
    """remove empty braces until done"""
    while True:
        edited = txt.replace(
            "{}","").replace(
            "[]","").replace(
            "<>","").replace(
            "()","")
        if edited == txt:
            return txt
        txt = edited

######## Part 1 ##########
def p1(expect=399153, viz=None):
    scores = []

    for line in DATA:
        trimmed = trim(line)
        for char in trimmed:
            if char in ERRVAL:
                scores.append(ERRVAL[char])
                break # get next line

    return sum(scores)

######## Part 2 ##########
def p2(expect=2995077699, viz=None):
    # calculate completer score for each incomplete line
    scores = []

    for line in DATA:
        txt = trim(line)

        # skip corrupted strings - anything containing bad closures
        if set(txt).intersection(ERRVAL):
            continue

        # reverse the string and replace openers with closures
        txt = txt[::-1].replace(
               "{","}").replace(
               "[","]").replace(
               "<",">").replace(
               "(",")")

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
