# import our helpers
from utils import load, show, day, TRACE, Map, Path
from collections import deque

####### GLOBALS #########

# load todays input data as a docstring
DATA = load(day(__file__)).splitlines()

# parse the input
PARSED = []
for row in DATA:
    PARSED.append([*map(int,row)])
MAP = Map(PARSED)

######## Part 1 ##########
def turn(octopi):
    flashes = 0
    # add all octopi to the queue once
    powerup = deque(range(100))
    while powerup:
        idx = powerup.popleft()
        octopi[idx] += 1
        if octopi[idx] == 10:
            flashes += 1
            yidx, xidx = divmod(idx,10)
            for y in [yidx-1, yidx, yidx+1]:
                for x in [xidx-1, xidx, xidx+1]:
                    neigh = y*10+x
                    if 0<=y<10 and 0<=x<10 and octopi[neigh]<10:
                        # add excited neighbour octopi to the queue again
                        powerup.append(neigh)
    # reset octopi that flashed
    for idx, power in enumerate(octopi):
        if power > 9:
            octopi[idx] = 0
    return flashes

def p1(expect=1652, viz=None):
    flashes = 0
    octopi = list(MAP.img.getdata())
    for i in range(100):
        flashes += turn(octopi)
        if viz:
            MAP.img.putdata(octopi)
            MAP.addtogif()
    return flashes


######## Part 2 ##########
def p2(expect=220, viz=None):
    turns = 0
    octopi = list(MAP.img.getdata())
    while any(octopi):
        turn(octopi)
        turns += 1
        if viz:
            MAP.img.putdata(octopi)
            MAP.addtogif()
    return turns

######### Main ###########
def main():
    show(p1, p2)

if __name__ == "__main__":
    main()
    for _ in range(1,10):
        MAP.setcolour(_,(_*6,_*6,_*6))
    MAP.setcolour(0,(255,255,255))
    p1(viz=True)
    MAP.savegif(Path(__file__).parent / 'output' / 'day11a.gif')
    MAP = Map(PARSED) # reset map
    for _ in range(1,10):
        MAP.setcolour(_,(_*6,_*6,_*6))
    MAP.setcolour(0,(255,255,255))
    p2(viz=True)
    MAP.savegif(Path(__file__).parent / 'output' / 'day11b.gif')
