# import our helpers
from utils import load, show, day, Map, TRACE
import numpy as np
import re
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()
PARSER = re.compile(r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")

######## Part 1 ##########
def p1(expect=644257, viz=None):
    arr = np.zeros([101,101,101], dtype=int)
    for line in DATA[:-2]:
        matched = PARSER.match(line)
        onoff = matched.group(1)
        x1, x2, y1, y2, z1, z2 = [int(_)+50 for _ in matched.groups()[1:]]
        val = 0 if onoff == "off" else 1
        arr[z1:z2+1,y1:y2+1,x1:x2+1] = val
    return sum(sum(sum(arr)))

######## Part 2 ##########
def p2(expect=16016, viz=None):
    return 0

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    # from visualizations import viz20a, viz20b
    # p1(viz=viz20a)
    # p2(viz=viz20b)
