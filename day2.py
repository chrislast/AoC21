# import our helpers
from utils import load, show, day, TRACE, Map

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

######## Part 1 ##########
def p1(expect=1868935):
    forward = sum([int(_[8:]) for _ in DATA if _.startswith('forward ')])
    up      = sum([int(_[3:]) for _ in DATA if _.startswith('up ')])
    down    = sum([int(_[5:]) for _ in DATA if _.startswith('down ')])
    return forward * (down - up)

######## Part 2 ##########
def p2(expect=1965970888, viz=None):
    depth = hpos = aim = 0
    vizdata = [] # visualisation use only
    for step in DATA:
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

    # visualisation stuff
        vizdata.append((hpos//20, depth//10046))
    if viz:
        viz(vizdata)

    return hpos * depth

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz2b
    p2(viz=viz2b)
