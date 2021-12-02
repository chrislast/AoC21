# import our helpers
from utils import load, show, day, TRACE, Map

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.splitlines()

######## Part 1 ##########
def p1(expect=None):
    forward = sum([int(_[8:]) for _ in PARSED if _.startswith('forward ')])
    up = sum([int(_[3:]) for _ in PARSED if _.startswith('up ')])
    down = sum([int(_[5:]) for _ in PARSED if _.startswith('down ')])
    return forward * (down - up)

######## Part 2 ##########
def p2(expect=None):
    depth = hpos = aim = 0
    for step in PARSED:
        if step.startswith("forward "):
            n = int(step[8:])
            hpos += n
            depth += aim * n
        if step.startswith("up "):
            n = int(step[3:])
            aim -= n
        if step.startswith("down "):
            n = int(step[5:])
            aim += n
    return hpos * depth


######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
