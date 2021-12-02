# import our helpers
from utils import load, show, day, Map, TRACE
import yaml
import PIL
from pathlib import Path
####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
depths = [int(d) for d in DATA.splitlines()]

def viz():
    # visualize the depth map
    viz = Map(["~"*x for x in depths])
    viz.setcolour("~",(0,128,128))
    img = viz.img.resize((100, 100))
    img = img.transpose(PIL.Image.TRANSPOSE)
    img.save(Path(__file__).parent / 'output' / 'day1.png')

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
    viz()
