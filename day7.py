# import our helpers
from utils import load, show, day, TRACE, Map, Path
from collections import Counter
from PIL import Image
from matplotlib import pyplot as plt

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.split(',')

######## Part 1 ##########
def p1(expect=360268, viz=None):
    data = dict(Counter(map(int, PARSED)))
    fuel = 0
    while len(data) > 1:
        imax = max(data)
        imin = min(data)
        if data[imax] > data[imin]:
            n = data.pop(imin)
            data[imin+1] = data.get(imin+1,0) + n
            fuel += n
        else:
            n = data.pop(imax)
            data[imax-1] = data.get(imax-1,0) + n
            fuel += n
    return fuel


######## Part 2 ##########
def p2(expect=1632146183902, viz=None):
    pass


######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    p1(viz=viz1)
    p2(viz=viz2)
