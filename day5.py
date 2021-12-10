# import our helpers
from utils import load, show, day, TRACE, Map
from collections import Counter

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

######## Part 1 ##########
def mapper(diagonals=False):
    sea = Map([[0]*1000]*1000)
    for line in DATA:
        start, stop = line.split()[::2]
        x1, y1 = map(int,start.split(","))
        x2, y2 = map(int,stop.split(","))
        # create x values
        if x1>x2:
            xr=range(x1, x2-1, -1)
        elif x2>x1:
            xr=range(x1, x2+1, 1)
        else:
            xr=[x1] * (abs(y2-y1)+1)
        # create y values
        if y1>y2:
            yr=range(y1, y2-1, -1)
        elif y2>y1:
            yr=range(y1, y2+1, 1)
        else:
            yr=[y1] * (abs(x2-x1)+1)
        # zip x,y values together and update map
        if x1==x2 or y1==y2 or diagonals:
            for x, y in zip(xr, yr):
                sea.set((x,y), sea.get((x,y))+1)
    return sea

def p1(expect=5698, viz=None):
    sea = mapper(diagonals=False)
    count = dict(Counter(sea.img.getdata()))
    count.pop(0)
    count.pop(1)
    if viz:
        viz(sea)
    return sum(count.values())

######## Part 2 ##########
def p2(expect=15463, viz=None):
    sea = mapper(diagonals=True)
    count = dict(Counter(sea.img.getdata()))
    count.pop(0)
    count.pop(1)
    if viz:
        viz(sea)
    return sum(count.values())

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    from visualizations import viz5a, viz5b
    p1(viz=viz5a)
    p2(viz=viz5b)
