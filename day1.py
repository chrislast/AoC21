# import our helpers
from utils import load, show, day, Map, TRACE

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input
depths = [int(d) for d in DATA]

######## Part 1 ##########
def p1(expect=1655):
    return sum([1 for i in range(1,len(depths)) if depths[i]>depths[i-1]])

######## Part 2 ##########
def p2(expect=1683):
    window=3
    d3 = [sum(depths[i:i+window]) for i in range(len(depths)-window+1)]
    return sum([1 for i in range(1,len(d3)) if d3[i]>d3[i-1]])

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz1
    viz1(depths)
