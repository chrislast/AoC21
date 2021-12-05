# import our helpers
from utils import load, show, day, TRACE, Map, Path
from collections import Counter

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__))

# parse the input
PARSED = DATA.splitlines()

######## Part 1 ##########
def inc(obj, pos):
    val = obj.get(pos)
    obj.set(pos,val+1)

def mapper(diagonals=False):
    sea = Map([[0]*1000]*1000)
    for line in PARSED:
        start, stop = line.split()[::2]
        x1, y1 = map(int,start.split(","))
        x2, y2 = map(int,stop.split(","))

        if x1>x2:
            xr=range(x1, x2-1, -1)
        elif x2>x1:
            xr=range(x1, x2+1, 1)
        else:
            xr=[x1] * (abs(y2-y1)+1)
        if y1>y2:
            yr=range(y1, y2-1, -1)
        elif y2>y1:
            yr=range(y1, y2+1, 1)
        else:
            yr=[y1] * (abs(x2-x1)+1)
        if x1==x2 or y1==y2 or diagonals:
            for x, y in zip(xr,yr):
                inc(sea, (x, y))
    return sea

def p1(expect=5698, viz=None):
    sea = mapper(diagonals=False)
    count = dict(Counter(sea.img.getdata()))
    count.pop(0)
    count.pop(1)
    if viz:
        sea.save(Path(__file__).parent / 'output' / 'day5a.png')
        sea.img.resize((100,100)).save(Path(__file__).parent / 'output' / 'day5athumb.png')
    return sum(count.values())

######## Part 2 ##########
def p2(expect=15463, viz=None):
    """"""
    sea = mapper(diagonals=True)
    count = dict(Counter(sea.img.getdata()))
    count.pop(0)
    count.pop(1)
    if viz:
        sea.save(Path(__file__).parent / 'output' / 'day5b.png')
        sea.img.resize((100,100)).save(Path(__file__).parent / 'output' / 'day5bthumb.png')
    return sum(count.values())

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    p1(viz=True)
    p2(viz=True)
