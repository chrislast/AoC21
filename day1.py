# import our helpers
from utils import load, show, day
import yaml
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
depths = [int(d) for d in DATA.splitlines()]

######## Part 1 ##########
def p1(expect=1655):
    return sum([1 for i in range(1,len(depths)) if depths[i]>depths[i-1]])

######## Part 2 ##########
def p2(expect=1683):
    d3 = [sum(depths[i:i+3]) for i in range(len(depths)-2)]
    return sum([1 for i in range(1,len(d3)) if d3[i]>d3[i-1]])

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
