# import our helpers
from utils import load, show, day, TRACE
from collections import Counter

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# Parse input
TEMPLATE = DATA[0]
RULES = dict([tuple(_.split(" -> ")) for _ in DATA[2:] if _])

######## Part 1 ##########
def p1(expect=5656, viz=None):
    text = TEMPLATE
    for _ in range(10):
        _text = ""
        for i in range(len(text)-1):
            _text += text[i] + RULES[text[i:i+2]]
        _text += text[-1]
        text = _text
    counter = Counter(text)
    return max(counter.values()) - min(counter.values())

######## Part 2 ##########
MAXDEPTH = 40 # ~0.08 seconds, works up to ~980 (1.5 seconds)
COUNTERCACHE = [{} for _ in range(MAXDEPTH)]

def rfunc(pair, depth):
    c2 = RULES[pair]
    counter = Counter(c2) # initially just the new letter
    if depth < MAXDEPTH-1: # not at maximum iteration depth yet
        for txt in (pair[0]+c2, c2+pair[1]): # process the two new substrings
            # if this calculation has not been done before then calculate it and cache the result
            if txt not in COUNTERCACHE[depth]:
                COUNTERCACHE[depth][txt] = rfunc(txt, depth+1)
            # update our counter with cached result
            counter += COUNTERCACHE[depth][txt]
    return counter

def p2(expect=12271437788530, viz=None):
    counter = Counter(TEMPLATE) # store all the template characters
    for i in range(len(TEMPLATE)-1):
        # update the counter for each letter pair
        counter += rfunc(TEMPLATE[i:i+2], 0)
    return max(counter.values()) - min(counter.values())

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
