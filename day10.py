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

def syntax_checker(txt):
    """return a non-zero syntax checker score for corrupted lines"""
    for char in txt:
        if char in ERRVAL:
            return ERRVAL[char]
    return 0

def p1(expect=399153, viz=None):
    """return the sum of all the syntax checker scores"""
    return sum([syntax_checker(trim(line)) for line in DATA])

######## Part 2 ##########
# line completer scores
COMPVAL = {")": 1, "]": 2, "}": 3, ">": 4}

def completer(txt):
    """return a non-zero completer score for incomplete lines"""
    # find and discard corrupted strings
    for char in txt:
        if char in ERRVAL:
            return 0
    # reverse the string and make opens into closes
    txt = txt[::-1].replace("{","}").replace("[","]").replace("<",">").replace("(",")")
    # calculate the score
    acc = 0
    for char in txt:
        acc *= 5
        acc += COMPVAL[char]
    return acc

def p2(expect=2995077699, viz=None):
    # calculate completer score for each line
    scores = [completer(trim(line)) for line in DATA]
    # remove corrupted lines and sort
    completed = [_ for _ in sorted(scores) if _]
    # return the middle score
    return completed[len(completed)//2]

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
