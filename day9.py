# import our helpers
from utils import load, show, day, TRACE, Map, Path

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
MAP = Map(DATA.splitlines())

######## Part 1 ##########
def p1(expect=439, viz=None):
    m = MAP.img.getdata()
    w,h = MAP.img.size
    risk = 0
    # foreach map position
    for y in range(h):
        for x in range(w):
            val = MAP.get((x,y))
            # if a surrounding xy is level or lower then this isn't a local minima
            minima = True
            for xy in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
                if minima and 0<=xy[0]<w and 0<=xy[1]<h and MAP.get(xy) <= val:
                    minima = False
            # otherwise add it's risk level total risk
            if minima:
                risk += val - ord('0') + 1
    return risk

######## Part 2 ##########
WALL = ord('9')
FILL = 255

def flood(pos, viz):
    # fill with a breadth first search queue
    queue = []
    basin_size = 0
    if MAP.get(pos) < WALL:
        queue.append(pos)
    while queue:
        x,y = queue.pop(0)
        for xy in ((x,y), (x-1,y), (x+1,y), (x,y-1), (x,y+1)):
            if 0<=xy[0]<MAP.img.width and 0<=xy[1]<MAP.img.height and MAP.get(xy) < WALL:
                if xy != (x,y):
                    queue.append(xy)
                MAP.set(xy, FILL)
                basin_size += 1
                if viz:
                    MAP.addtogif()
    return basin_size

def p2(expect=900900, viz=None):
    basins = []
    w,h = MAP.img.size
    for y in range(h):
        for x in range(w):
            basins.append(flood((x,y),viz))
    b1, b2, b3 = sorted(basins)[-3:]
    return b1 * b2 * b3

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    # reset MAP to create visualizations
    MAP = Map(DATA.splitlines())
    print("Creating visualizations takes ~30 seconds")
    from visualizations import viz9a, viz9b
    viz9a(p1, MAP)
    viz9b(p2, MAP)
