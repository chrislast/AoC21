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

COUNTERCACHE = [{} for _ in range(40)]

def rfunc(pair, depth):
    c2 = RULES[pair]
    counter = Counter(c2)
    if depth < 39:
        for txt in (pair[0]+c2, c2+pair[1]): # get the two substrings to check
            if txt not in COUNTERCACHE[depth]: #
                COUNTERCACHE[depth][txt] = rfunc(txt, depth+1)
            counter += COUNTERCACHE[depth][txt]
    return counter

def p2(expect=12271437788530, viz=None):
    counter = Counter(TEMPLATE)
    for i in range(len(TEMPLATE)-1):
        x = rfunc(TEMPLATE[i:i+2], 0)
        counter += x
    return max(counter.values()) - min(counter.values())

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
