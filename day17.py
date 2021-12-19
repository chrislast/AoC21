# import our helpers
from utils import load, show, day, Map, TRACE
import re
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input target area: x=240..292, y=-90..-57
PATTERN = re.compile(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)")
XMIN, XMAX, YMIN, YMAX = map(int, re.match(PATTERN, DATA).groups())

######## Part 1 ##########
def fire(xvel,yvel):
    xpos = ypos = 0
    ypeak = 0
    while ypos > YMIN:
        xpos += xvel
        ypos += yvel
        if ypos > ypeak:
            ypeak = ypos
        if XMIN<=xpos<=XMAX and YMIN<=ypos<=YMAX:
            return 1
        xvel -= 1 if xvel>0 else 0 if xvel==0 else 1
        yvel -= 1
    return 0

def p1(expect=4005):
    yvel = abs(YMIN) -1
    return yvel * (yvel//2 + 1)

######## Part 2 ##########
def p2(expect=2953):
    """runs in 30 minutes!!"""
    # the biggest xvel not to overshoot target immediately
    biggestxvel = XMAX
    # find the smallest x velocity able to reach the target
    xvel = 1
    while sum(range(1, xvel+2)) < XMIN:
        xvel += 1
    smallestxvel = xvel
    # the biggest yvel that won't skip over the target
    yvel = abs(YMIN) -1
    biggestyvel =  yvel * (yvel//2 + 1)
    # the smallest yvel that won't be below the target in a single step
    smallestyvel = YMIN

    acc = 0
    for y in range(smallestyvel, biggestyvel+1):
        for x in range(smallestxvel, biggestxvel+1):
            acc += fire(x, y)
    return acc


######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
